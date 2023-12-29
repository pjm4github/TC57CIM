from IEC61968.Common.Status import Status
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Money import Money
from IEC62325.MarketOperations.MktDomain.MktAccountKind import MktAccountKind
from IEC62325.MarketOperations.MarketSystem.MarketResults.Settlement import Settlement


class MarketLedgerEntry:
    #  * Details of an individual entry in a ledger, which was posted from a journal on
    #  * the posted date.
    #  * @created 27-Dec-2023 5:15:25 PM
    def __init__(self):
        self.account_id = ""  # Account identifier for this entry.
        self.account_kind = MktAccountKind()  # Kind of account for this entry.
        self.amount = Money()  # The amount of the debit or credit for this account.
        self.posted_date_time = DateTime()  # Date and time this entry was posted to the ledger.
        self.status = Status()  # Status of ledger entry.
        self.transaction_date_time = DateTime()  # Date and time journal entry was recorded.
        self.settlement = Settlement()