# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import asyncio
from typing import List
from unittest import IsolatedAsyncioTestCase
import uuid
import grpc.aio
from app.proto.revocation_pb2 import (
    RevokeRequest,
    RevokeResponse,
    RevokeCurrencyObject,
)
from app.proto.revocation_pb2_grpc import (
    RevocationStub,
    add_RevocationServicer_to_server,
)
from app.services.revocation_service import AsyncRevocationService
from accelbyte_grpc_plugin_tests import create_server


class AsyncRevocationServiceTestCase(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.service = AsyncRevocationService(None)

    async def test_filter_bulk_filters_profanities(self):
       
        request = RevokeRequest(
            revokeEntryType = "CURRENCY",
            namespace = "test",
            userId = "4423f033c38a40b9afdc8844e13647b7",
            quantity = 1,
            currency = RevokeCurrencyObject(
                namespace = "test",
                currencyCode = "VCA",
                balanceOrigin = "SYSTEM"
            ),
        )
        response = await self.service.Revoke(request, None)
        
        # assert
        self.assertIsNotNone(response)
        self.assertIsInstance(response, RevokeResponse)