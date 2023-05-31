# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

from logging import Logger, getLogger
from typing import Optional

from app.proto.revocation_pb2 import (
    RevokeRequest,
    RevokeResponse,
    DESCRIPTOR,
)

from app.proto.revocation_pb2_grpc import RevocationServicer

from app.object.revoke_entry_type import RevokeEntryType
from app.object.revocation_status import RevocationStatus
from app.revocation.revocations import Revocations

class AsyncRevocationService(RevocationServicer):
    full_name: str = DESCRIPTOR.services_by_name["Revocation"].full_name

    def __init__(self, logger: Optional[Logger] = None) -> None:
        self.logger = (
            logger if logger is not None else getLogger(self.__class__.__name__)
        )
            
    async def Revoke(self, request: RevokeRequest, context):
        self.logger.info("Received revoke request")

        response : RevokeResponse

        try:
            namespace = request.namespace
            userId = request.userId
            quantity = request.quantity

            revoke_entry_type = RevokeEntryType[request.revokeEntryType.upper()]
            revocation = Revocations().get_revocation(revoke_entry_type)
            response = revocation.revoke(namespace, userId, quantity, request)
        except Exception as e:
            response = RevokeResponse(
                reason = f"Revocation method {str(e)} not supported",
                status = RevocationStatus.FAIL.name,
            )

        return response