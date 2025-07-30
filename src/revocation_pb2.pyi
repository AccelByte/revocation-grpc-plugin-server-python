from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RevokeCurrencyObject(_message.Message):
    __slots__ = ["balanceOrigin", "currencyCode", "namespace"]
    BALANCEORIGIN_FIELD_NUMBER: _ClassVar[int]
    CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    balanceOrigin: str
    currencyCode: str
    namespace: str
    def __init__(self, namespace: _Optional[str] = ..., currencyCode: _Optional[str] = ..., balanceOrigin: _Optional[str] = ...) -> None: ...

class RevokeEntitlementObject(_message.Message):
    __slots__ = ["entitlementId", "itemId", "sku"]
    ENTITLEMENTID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    entitlementId: str
    itemId: str
    sku: str
    def __init__(self, entitlementId: _Optional[str] = ..., itemId: _Optional[str] = ..., sku: _Optional[str] = ...) -> None: ...

class RevokeItemObject(_message.Message):
    __slots__ = ["entitlementType", "itemId", "itemSku", "itemType", "useCount"]
    ENTITLEMENTTYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMSKU_FIELD_NUMBER: _ClassVar[int]
    ITEMTYPE_FIELD_NUMBER: _ClassVar[int]
    USECOUNT_FIELD_NUMBER: _ClassVar[int]
    entitlementType: str
    itemId: str
    itemSku: str
    itemType: str
    useCount: int
    def __init__(self, itemId: _Optional[str] = ..., itemSku: _Optional[str] = ..., itemType: _Optional[str] = ..., useCount: _Optional[int] = ..., entitlementType: _Optional[str] = ...) -> None: ...

class RevokeRequest(_message.Message):
    __slots__ = ["currency", "entitlement", "item", "namespace", "quantity", "revokeEntryType", "userId"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    REVOKEENTRYTYPE_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    currency: RevokeCurrencyObject
    entitlement: RevokeEntitlementObject
    item: RevokeItemObject
    namespace: str
    quantity: int
    revokeEntryType: str
    userId: str
    def __init__(self, revokeEntryType: _Optional[str] = ..., userId: _Optional[str] = ..., namespace: _Optional[str] = ..., quantity: _Optional[int] = ..., item: _Optional[_Union[RevokeItemObject, _Mapping]] = ..., entitlement: _Optional[_Union[RevokeEntitlementObject, _Mapping]] = ..., currency: _Optional[_Union[RevokeCurrencyObject, _Mapping]] = ...) -> None: ...

class RevokeResponse(_message.Message):
    __slots__ = ["customRevocation", "reason", "status"]
    class CustomRevocationEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CUSTOMREVOCATION_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    customRevocation: _containers.ScalarMap[str, str]
    reason: str
    status: str
    def __init__(self, status: _Optional[str] = ..., reason: _Optional[str] = ..., customRevocation: _Optional[_Mapping[str, str]] = ...) -> None: ...
