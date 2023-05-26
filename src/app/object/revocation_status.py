from enum import Enum, auto as enum_auto

class RevocationStatus(Enum):
    SUCCESS = enum_auto()
    FAIL = enum_auto()