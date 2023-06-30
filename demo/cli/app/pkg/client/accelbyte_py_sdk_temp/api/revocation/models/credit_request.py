# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
# 
# Code generated. DO NOT EDIT!

# template file: ags_py_codegen

# AccelByte Gaming Services Platform Service (4.30.2)

# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-return-statements
# pylint: disable=too-many-statements
# pylint: disable=unused-import

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import Model
from ....core import StrEnum


class OriginEnum(StrEnum):
    PLAYSTATION = "Playstation"
    XBOX = "Xbox"
    STEAM = "Steam"
    EPIC = "Epic"
    IOS = "IOS"
    GOOGLEPLAY = "GooglePlay"
    TWITCH = "Twitch"
    NINTENDO = "Nintendo"
    SYSTEM = "System"
    OTHER = "Other"


class SourceEnum(StrEnum):
    PURCHASE = "PURCHASE"
    IAP = "IAP"
    PROMOTION = "PROMOTION"
    ACHIEVEMENT = "ACHIEVEMENT"
    REFERRAL_BONUS = "REFERRAL_BONUS"
    REDEEM_CODE = "REDEEM_CODE"
    REWARD = "REWARD"
    GIFT = "GIFT"
    REFUND = "REFUND"
    DLC = "DLC"
    OTHER = "OTHER"
    SELL_BACK = "SELL_BACK"


class CreditRequest(Model):
    """A DTO for wallet's credit (CreditRequest)

    Properties:
        amount: (amount) REQUIRED int

        expire_at: (expireAt) OPTIONAL str

        origin: (origin) OPTIONAL Union[str, OriginEnum]

        reason: (reason) OPTIONAL str

        source: (source) OPTIONAL Union[str, SourceEnum]
    """

    # region fields

    amount: int                                                                                    # REQUIRED
    expire_at: str                                                                                 # OPTIONAL
    origin: Union[str, OriginEnum]                                                                 # OPTIONAL
    reason: str                                                                                    # OPTIONAL
    source: Union[str, SourceEnum]                                                                 # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_amount(self, value: int) -> CreditRequest:
        self.amount = value
        return self

    def with_expire_at(self, value: str) -> CreditRequest:
        self.expire_at = value
        return self

    def with_origin(self, value: Union[str, OriginEnum]) -> CreditRequest:
        self.origin = value
        return self

    def with_reason(self, value: str) -> CreditRequest:
        self.reason = value
        return self

    def with_source(self, value: Union[str, SourceEnum]) -> CreditRequest:
        self.source = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "amount"):
            result["amount"] = int(self.amount)
        elif include_empty:
            result["amount"] = 0
        if hasattr(self, "expire_at"):
            result["expireAt"] = str(self.expire_at)
        elif include_empty:
            result["expireAt"] = ""
        if hasattr(self, "origin"):
            result["origin"] = str(self.origin)
        elif include_empty:
            result["origin"] = Union[str, OriginEnum]()
        if hasattr(self, "reason"):
            result["reason"] = str(self.reason)
        elif include_empty:
            result["reason"] = ""
        if hasattr(self, "source"):
            result["source"] = str(self.source)
        elif include_empty:
            result["source"] = Union[str, SourceEnum]()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        amount: int,
        expire_at: Optional[str] = None,
        origin: Optional[Union[str, OriginEnum]] = None,
        reason: Optional[str] = None,
        source: Optional[Union[str, SourceEnum]] = None,
    **kwargs
    ) -> CreditRequest:
        instance = cls()
        instance.amount = amount
        if expire_at is not None:
            instance.expire_at = expire_at
        if origin is not None:
            instance.origin = origin
        if reason is not None:
            instance.reason = reason
        if source is not None:
            instance.source = source
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> CreditRequest:
        instance = cls()
        if not dict_:
            return instance
        if "amount" in dict_ and dict_["amount"] is not None:
            instance.amount = int(dict_["amount"])
        elif include_empty:
            instance.amount = 0
        if "expireAt" in dict_ and dict_["expireAt"] is not None:
            instance.expire_at = str(dict_["expireAt"])
        elif include_empty:
            instance.expire_at = ""
        if "origin" in dict_ and dict_["origin"] is not None:
            instance.origin = str(dict_["origin"])
        elif include_empty:
            instance.origin = Union[str, OriginEnum]()
        if "reason" in dict_ and dict_["reason"] is not None:
            instance.reason = str(dict_["reason"])
        elif include_empty:
            instance.reason = ""
        if "source" in dict_ and dict_["source"] is not None:
            instance.source = str(dict_["source"])
        elif include_empty:
            instance.source = Union[str, SourceEnum]()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, CreditRequest]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[CreditRequest]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[CreditRequest, List[CreditRequest], Dict[Any, CreditRequest]]:
        if many:
            if isinstance(any_, dict):
                return cls.create_many_from_dict(any_, include_empty=include_empty)
            elif isinstance(any_, list):
                return cls.create_many_from_list(any_, include_empty=include_empty)
            else:
                raise ValueError()
        else:
            return cls.create_from_dict(any_, include_empty=include_empty)

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "amount": "amount",
            "expireAt": "expire_at",
            "origin": "origin",
            "reason": "reason",
            "source": "source",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "amount": True,
            "expireAt": False,
            "origin": False,
            "reason": False,
            "source": False,
        }

    @staticmethod
    def get_enum_map() -> Dict[str, List[Any]]:
        return {
            "origin": ["Playstation", "Xbox", "Steam", "Epic", "IOS", "GooglePlay", "Twitch", "Nintendo", "System", "Other"],
            "source": ["PURCHASE", "IAP", "PROMOTION", "ACHIEVEMENT", "REFERRAL_BONUS", "REDEEM_CODE", "REWARD", "GIFT", "REFUND", "DLC", "OTHER", "SELL_BACK"],
        }

    # endregion static methods
