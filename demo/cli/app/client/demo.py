from client.model import SimpleItemInfo
from client.utils import random_string

import accelbyte_py_sdk.api.platform as platform_service
import accelbyte_py_sdk.api.platform.models as platform_models

AB_STORE_NAME = "Python Revocation Plugin Demo Store"
ALPHA_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

ERR_EMPTY_STORE_ID = "error empty store id, create_store first"

class PlatformDataUnit:
    def __init__(self, user_info, config, currency_code) -> None:
        self.user_info = user_info
        self.config = config
        self.currency_code = currency_code
        self.store_id = None
    
    def creat_store(self, do_publish : bool):         
        result, error = platform_service.create_store(
            namespace=self.config.ABNamespace,
            body=platform_models.StoreCreate.create(
                title=AB_STORE_NAME,
                description="Description for %s" % AB_STORE_NAME,
                default_language="en",
                default_region="US",
                supported_languages=["en"],
                supported_regions=["US"]
            )
        )
        if error:
            return error

        self.store_id = result.store_id
        
        if do_publish:
            error = self.publish_store_change()
            if error:
                return error

        return error
    
    def set_platform_service_grpc_target(self):
        print(f"(Custom Host: {self.config.GRPCServerURL})")

        _, error = platform_service.update_service_plugin_config(
            namespace=self.config.ABNamespace,
            body=platform_models.ServicePluginConfigUpdate.create(
                grpc_server_address=self.config.GRPCServerURL
            )
        )
        return error
    
    def publish_store_change(self):
        if not self.store_id:
            return None, ERR_EMPTY_STORE_ID
        
        _, error = platform_service.publish_all(
            namespace=self.config.ABNamespace,
            store_id=self.store_id
        )
        return error

    def create_category(self, category_path : str, do_publish : bool):
        if not self.store_id:
            return None, ERR_EMPTY_STORE_ID
        
        _, error = platform_service.create_category(
            namespace=self.config.ABNamespace,
            store_id=self.store_id,
            body=platform_models.CategoryCreate.create(
                category_path=category_path,
                localization_display_names={"en" : category_path}
            )
        )
        if error:
            return error

        if do_publish:
            error = self.publish_store_change()
            if error:
                return error

        return error
    
    def update_revocation_config(self):
        _, error = platform_service.update_revocation_config(
            namespace=self.config.ABNamespace,
            body=platform_models.RevocationConfigUpdate.create(
                entitlement=platform_models.EntitlementRevocationConfig.create(
                    consumable=None,
                    durable=platform_models.DurableEntitlementRevocationConfig.create(
                        enabled=False,
                        strategy=platform_models.DurableEntitlementRevocationConfigStrategyEnum.CUSTOM
                    )
                ),
                wallet=platform_models.WalletRevocationConfig.create(
                    enabled=True,
                    strategy=platform_models.WalletRevocationConfigStrategyEnum.CUSTOM
                )
            )
        )
        return error

    def create_currency(self):
        # result, error = platform_service.get_currency_summary(
        #     namespace=self.config.ABNamespace,
        #     currency_code=self.currency_code
        # )
        # if not error and result:
        #     # already exists
        #     return None
        
        _, error = platform_service.create_currency(
            namespace=self.config.ABNamespace,
            body=platform_models.CurrencyCreate.create(
                currency_code=self.currency_code,
                currency_symbol="$V",
                currency_type=platform_models.CurrencyCreateCurrencyTypeEnum.REAL,
                decimals=2
            ),
        )
        return error
    
    def delete_currency(self):
        return platform_service.delete_currency(
            namespace=self.config.ABNamespace,
            currency_code=self.currency_code
        )

    def unset_platform_service_grpc_target(self):
        _, error = platform_service.delete_service_plugin_config(
            namespace=self.config.ABNamespace
        )
        return error
    
    def delete_store(self):
        if not self.store_id:
            return None, ERR_EMPTY_STORE_ID
        
        _, error = platform_service.delete_store(
            namespace=self.config.ABNamespace,
            store_id=self.store_id
        )
        return error

    
    def create_items(self, item_count : int, category_path : str, do_publish : bool):
        if not self.store_id:
            return None, ERR_EMPTY_STORE_ID
        
        items = []
        item_diff = random_string(ALPHA_CHARS, 6)
        for i in range(item_count):
            item_info = SimpleItemInfo(
                title=f"Item {item_diff} Titled {i+1}",
                sku=f"SKU_{item_diff}_{i+1}"
            )

            newItem, error = platform_service.create_item(
                namespace=self.config.ABNamespace,
                store_id=self.store_id,
                body=platform_models.ItemCreate.create(
                    name=item_info.title,
                    item_type=platform_models.ItemCreateItemTypeEnum.COINS,
                    category_path=category_path,
                    entitlement_type=platform_models.ItemCreateEntitlementTypeEnum.CONSUMABLE,
                    season_type=platform_models.ItemCreateSeasonTypeEnum.TIER,
                    status=platform_models.ItemCreateStatusEnum.ACTIVE,
                    use_count=1,
                    target_currency_code=self.currency_code,
                    listable=True,
                    purchasable=True,
                    sku=item_info.sku,
                    localizations={ "en" : platform_models.Localization.create(title=item_info.title) },
                    region_data={ "US" : [platform_models.RegionDataItemDTO.create(
                        currency_code=self.currency_code,
                        currency_namespace=self.config.ABNamespace,
                        currency_type=platform_models.RegionDataItemDTOCurrencyTypeEnum.VIRTUAL,
                        price=0
                    )]}
                )
            )
            if error:
                return None, "could not create new store item: " + str(error)
            
            item_info.id = newItem.item_id
            items.append(item_info)
                
        if do_publish:
            error = self.publish_store_change()
            if error:
                return None, error

        return items, None

    def create_order(self, user_id : str, item_info : SimpleItemInfo):
        return platform_service.public_create_user_order(
            namespace=self.config.ABNamespace,
            user_id=user_id,
            body=platform_models.OrderCreate.create(
                currency_code=self.currency_code,
                item_id=item_info.id,
                price=0,
                quantity=1,
                discounted_price=0
            )
        )
    
    def revoke(self, user_id : str, order_no : str, item_id : str):
        return platform_service.do_revocation(
            namespace=self.config.ABNamespace,
            user_id=user_id,
            body=platform_models.RevocationRequest.create(
                source=platform_models.RevocationRequestSourceEnum.ORDER,
                transaction_id=order_no,
                revoke_entries=[platform_models.RevokeEntry.create(
                    quantity=1,
                    type_=platform_models.RevokeEntryTypeEnum.ITEM,
                    item=platform_models.RevokeItem.create(
                        item_identity_type=platform_models.RevokeItemItemIdentityTypeEnum.ITEM_ID,
                        item_identity=item_id
                    )
                )]
            )
        )

    