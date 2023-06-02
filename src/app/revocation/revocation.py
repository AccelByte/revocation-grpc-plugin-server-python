from abc import abstractclassmethod, ABC

from app.proto.revocation_pb2 import RevokeResponse
from app.object.revocation_status import RevocationStatus

class Revocation(ABC):
    
    def __init__(self) -> None:
        ...

    @abstractclassmethod
    def revoke(self, namespace, userId, quantity, request):
        pass

class CurrencyRevocation(Revocation):
    
    def __init__(self) -> None:
        self.custom_revocation = dict()

        super().__init__()
    
    def revoke(self, namespace, userId, quantity, request):

        currency = request.currency
        self.custom_revocation["namespace"] = namespace
        self.custom_revocation["userId"] = userId
        self.custom_revocation["quantity"] = str(quantity)
        self.custom_revocation["currencyNamespace"] = currency.namespace
        self.custom_revocation["currencyCode"] = currency.currencyCode
        self.custom_revocation["balanceOrigin"] = currency.balanceOrigin

        return RevokeResponse(
            customRevocation = self.custom_revocation,
            status = RevocationStatus.SUCCESS.name,
        )

class EntitlementRevocation(Revocation):

    def __init__(self) -> None:
        self.custom_revocation = dict()

        super().__init__()
    
    def revoke(self, namespace, userId, quantity, request):
        
        entitlement = request.entitlement
        self.custom_revocation["namespace"] = namespace
        self.custom_revocation["userId"] = userId
        self.custom_revocation["quantity"] = str(quantity)
        self.custom_revocation["entitlementId"] = entitlement.entitlementId
        self.custom_revocation["itemId"] = entitlement.itemId
        self.custom_revocation["sku"] = entitlement.sku

        return RevokeResponse(
            customRevocation = self.custom_revocation,
            status = RevocationStatus.SUCCESS.name,
        )

class ItemRevocation(Revocation):

    def __init__(self) -> None:
        self.custom_revocation = dict()

        super().__init__()
    
    def revoke(self, namespace, userId, quantity, request):
        
        item = request.item
        self.custom_revocation["namespace"] = namespace
        self.custom_revocation["userId"] = userId
        self.custom_revocation["quantity"] = str(quantity)
        self.custom_revocation["sku"] = item.itemSku
        self.custom_revocation["itemType"] = item.itemType
        self.custom_revocation["useCount"] = str(item.useCount)
        self.custom_revocation["entitlementType"] = item.entitlementType

        return RevokeResponse(
            customRevocation = self.custom_revocation,
            status = RevocationStatus.SUCCESS.name,
        )