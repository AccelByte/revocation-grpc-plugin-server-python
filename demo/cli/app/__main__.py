# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import random
import string
import traceback

import accelbyte_py_sdk as accelbyte_py_sdk
import accelbyte_py_sdk.core as sdk_core
import accelbyte_py_sdk.services.auth as auth_service
import accelbyte_py_sdk.api.iam as iam_service
import accelbyte_py_sdk.api.iam.models as iam_models

from .pkg.config import get_config
from .pkg.demo import PlatformDataUnit


def start_testing(user_info, config, category_path="/pythonRevocationPluginDemo"):
    pdu = PlatformDataUnit(user_info=user_info, config=config, currency_code="VCA")
    success = True
    # noinspection PyBroadException
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
        error = pdu.create_store(True)
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
        items, error = pdu.create_items(
            item_count=1, category_path=category_path, do_publish=True
        )
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        # 7.
        print("Creating order...")
        order_info, error = pdu.create_order(
            user_id=user_info.user_id, item_info=items[0]
        )
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        # 8.
        print("Revoking order...")
        revocation_result, error = pdu.revoke(
            user_id=user_info.user_id,
            order_no=order_info.order_no,
            item_id=order_info.item_id,
        )
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        print("\nRevocation Result: ")
        print(f"Revocation history id: {revocation_result.id_}")
        print(f"Revocation status id: {revocation_result.status}")

        if revocation_result.status != "SUCCESS":
            success = False
            raise Exception()

        for r in revocation_result.item_revocations:
            print(r)

        print("[SUCCESS]")
    except Exception:
        print(traceback.format_exc())
        print("\n[FAILED]")
        success = False
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

    return success


def generate_password(length: int) -> str:
    strings = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%^&*()_+-=",
    ]

    si = 0
    result = ""
    for _ in range(length):
        result += random.choice(strings[si])
        si += 1
        if si == len(strings):
            si = 0

    return result


def create_test_user():
    name_id = sdk_core.generate_id(8)

    username = f"extend_{name_id}_user"
    password = generate_password(16)
    display_name = f"Extend Test User {name_id}"

    user_info, error = iam_service.public_create_test_user_v4(
        body=iam_models.AccountCreateTestUserRequestV4.create(
            auth_type="EMAILPASSWD",
            country="ID",
            date_of_birth="1990-01-01",
            display_name=display_name,
            email_address=f"{username}@dummy.net",
            password=password,
            password_md5_sum=password,
            username=username,
            verified=True,
            unique_display_name=display_name,
        )
    )
    if error:
        raise Exception(error)

    return user_info


def main():
    config = get_config()

    accelbyte_py_sdk.initialize()

    print("# Arrange")
    print("## Login to AccelByte... ")
    _, error = auth_service.login_client()
    if error:
        raise Exception(error)
    print("[OK]")

    print("## Get user info")
    user_info = create_test_user()
    print("[OK]")

    print("# Test Start")
    success = start_testing(user_info, config)

    if not success:
        exit(1)


if __name__ == "__main__":
    main()
