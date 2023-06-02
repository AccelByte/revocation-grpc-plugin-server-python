from app.object.revoke_entry_type import RevokeEntryType
from app.revocation.revocation import CurrencyRevocation, EntitlementRevocation, ItemRevocation

class Revocations:
    
    def __init__(self) -> None:
        self.REVOCATIONS = {
            RevokeEntryType.ITEM: ItemRevocation(),
            RevokeEntryType.CURRENCY: CurrencyRevocation(),
            RevokeEntryType.ENTITLEMENT: EntitlementRevocation(),
        }

    def get_revocation(self, type: RevokeEntryType):
        revocation = self.REVOCATIONS[type]
        if reversed is None:
            raise TypeError(f"Revocation method {type.name} not supported")
        
        return revocation
