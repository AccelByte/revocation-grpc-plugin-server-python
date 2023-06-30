# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import traceback

import pkg.client.accelbyte_py_sdk_temp as accelbyte_py_sdk
import pkg.client.accelbyte_py_sdk_temp.services.auth as auth_service
import pkg.client.accelbyte_py_sdk_temp.api.iam as iam_service

from pkg.config import get_config
from pkg.demo import PlatformDataUnit

def start_testing(user_info, config, category_path="/pythonRevocationPluginDemo"):
    pdu = PlatformDataUnit(
        user_info=user_info, 
        config=config, 
        currency_code="VCA"
    )
    try:
        # 1.
        print("Configuring platform service grpc target... ")
        error = pdu.set_platform_service_grpc_target()
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")
        
        # 2.
        print("Creating store... ")
        error = pdu.creat_store(True)
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        # 3.
        print("Creating category... ")
        error = pdu.create_category(category_path=category_path, do_publish=True)
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        # 4.
        print("Updating Revocation config... ")
        error = pdu.update_revocation_config()
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        # 5.
        print(f"Setting up currency ({pdu.currency_code})... ")
        error = pdu.create_currency()
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        # 6.
        print("Creating items...")
        items, error = pdu.create_items(item_count=1, category_path=category_path, do_publish=True)
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        # 7.
        print("Creating order...")
        order_info, error = pdu.create_order(user_id=user_info.user_id, item_info=items[0])
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        # 8.
        print("Revoking order...")
        revocation_result, error = pdu.revoke(user_id=user_info.user_id, order_no=order_info.order_no, item_id=order_info.item_id)
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")
        
        print("\nRevocation Result: ")
        print(f"Revocation history id: {revocation_result.id_}")
        print(f"Revocation status id: {revocation_result.status}")
        for r in revocation_result.item_revocations:
            print(r)

        print("[SUCCESS]")
    except:
        print(traceback.format_exc())
        print("\n[FAILED]")
    finally:
        print("# Cleaning Up")
        print("Deleting currency... ")
        _, error = pdu.delete_currency()
        if error:
            print(error)
            return
        print("[OK]")
        if pdu.store_id:
            print("Deleting store...")
            error = pdu.delete_store()
            if error:
                print(error)
                return
            print("[OK]")
        
        if config.GRPCServerURL:
            print("Unset platform service grpc target... ")
            error = pdu.unset_platform_service_grpc_target()
            if error:
                print("failed to unset platform service grpc plugin url")
                return
            print("[OK]")
        print("[CLEAN UP FINISHED]")

def main():
    config = get_config()

    accelbyte_py_sdk.initialize()

    print("# Arrange")
    print("## Login to AccelByte... ")
    _, error = auth_service.login_user(username=config.ABUsername, password=config.ABPassword)
    if error:
        raise Exception(error)
    print("[OK]")

    print("## Get user info")
    user_info, error = iam_service.public_get_my_user_v3() 
    if error:
        raise Exception(error)
    print("[OK]")
    
    print("# Test Start")
    start_testing(user_info, config)
            
if __name__ == "__main__":
    main()