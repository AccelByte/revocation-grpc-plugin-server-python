# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import json
from logging import Logger
from typing import Optional

from google.protobuf.json_format import MessageToDict

from accelbyte_py_sdk import AccelByteSDK

from ..proto.revocation_pb2 import (
    RevokeRequest,
    RevokeResponse,
    DESCRIPTOR,
)
from ..proto.revocation_pb2_grpc import RevocationServicer

from ..object.revoke_entry_type import RevokeEntryType
from ..object.revocation_status import RevocationStatus
from ..revocation.revocations import Revocations


class AsyncRevocationService(RevocationServicer):
    full_name: str = DESCRIPTOR.services_by_name["Revocation"].full_name

    def __init__(self, sdk: Optional[AccelByteSDK] = None, logger: Optional[Logger] = None) -> None:
        self.sdk = sdk
        self.logger = logger
            
    async def Revoke(self, request: RevokeRequest, context):
        self.log_payload(f'{self.Revoke.__name__} request: %s', request)
        response: RevokeResponse
        try:
            namespace = request.namespace
            user_id = request.userId
            quantity = request.quantity
            revoke_entry_type = RevokeEntryType[request.revokeEntryType.upper()]
            revocation = Revocations().get_revocation(revoke_entry_type)
            response = revocation.revoke(namespace, user_id, quantity, request)
        except Exception as e:
            response = RevokeResponse(
                reason=f"Revocation method {str(e)} not supported",
                status=RevocationStatus.FAIL.name,
            )
        self.log_payload(f'{self.Revoke.__name__} response: %s', response)
        return response

    # noinspection PyShadowingBuiltins
    def log_payload(self, format : str, payload):
        if not self.logger:
            return
        payload_dict = MessageToDict(payload, preserving_proto_field_name=True)
        payload_json = json.dumps(payload_dict)
        self.logger.info(format % payload_json)
