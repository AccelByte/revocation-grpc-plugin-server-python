from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RevokeRequest(_message.Message):
    __slots__ = ("revokeEntryType", "userId", "namespace", "quantity", "item", "entitlement", "currency")
    REVOKEENTRYTYPE_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    revokeEntryType: str
    userId: str
    namespace: str
    quantity: int
    item: RevokeItemObject
    entitlement: RevokeEntitlementObject
    currency: RevokeCurrencyObject
    def __init__(self, revokeEntryType: _Optional[str] = ..., userId: _Optional[str] = ..., namespace: _Optional[str] = ..., quantity: _Optional[int] = ..., item: _Optional[_Union[RevokeItemObject, _Mapping]] = ..., entitlement: _Optional[_Union[RevokeEntitlementObject, _Mapping]] = ..., currency: _Optional[_Union[RevokeCurrencyObject, _Mapping]] = ...) -> None: ...

class RevokeResponse(_message.Message):
    __slots__ = ("status", "reason", "customRevocation")
    class CustomRevocationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    CUSTOMREVOCATION_FIELD_NUMBER: _ClassVar[int]
    status: str
    reason: str
    customRevocation: _containers.ScalarMap[str, str]
    def __init__(self, status: _Optional[str] = ..., reason: _Optional[str] = ..., customRevocation: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RevokeItemObject(_message.Message):
    __slots__ = ("itemId", "itemSku", "itemType", "useCount", "entitlementType")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMSKU_FIELD_NUMBER: _ClassVar[int]
    ITEMTYPE_FIELD_NUMBER: _ClassVar[int]
    USECOUNT_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENTTYPE_FIELD_NUMBER: _ClassVar[int]
    itemId: str
    itemSku: str
    itemType: str
    useCount: int
    entitlementType: str
    def __init__(self, itemId: _Optional[str] = ..., itemSku: _Optional[str] = ..., itemType: _Optional[str] = ..., useCount: _Optional[int] = ..., entitlementType: _Optional[str] = ...) -> None: ...

class RevokeEntitlementObject(_message.Message):
    __slots__ = ("entitlementId", "itemId", "sku")
    ENTITLEMENTID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    entitlementId: str
    itemId: str
    sku: str
    def __init__(self, entitlementId: _Optional[str] = ..., itemId: _Optional[str] = ..., sku: _Optional[str] = ...) -> None: ...

class RevokeCurrencyObject(_message.Message):
    __slots__ = ("namespace", "currencyCode", "balanceOrigin")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    BALANCEORIGIN_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    currencyCode: str
    balanceOrigin: str
    def __init__(self, namespace: _Optional[str] = ..., currencyCode: _Optional[str] = ..., balanceOrigin: _Optional[str] = ...) -> None: ...
