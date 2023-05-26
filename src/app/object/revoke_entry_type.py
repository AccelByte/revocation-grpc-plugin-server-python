from enum import Enum, auto as enum_auto

class RevokeEntryType(Enum):
    ITEM = enum_auto()
    CURRENCY = enum_auto()
    ENTITLEMENT = enum_auto()