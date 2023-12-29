from IEC62325.MarketOperations.MarketOpCommon.MarketLedgerEntry import MarketLedgerEntry


class MarketLedger:
    #  * In accounting transactions, a ledger is a book containing accounts to which
    #  * debits and credits are posted from journals, where transactions are initially
    #  * recorded. Journal entries are periodically posted to the ledger. Ledger actual
    #  * represents actual amounts by account within ledger within company or within
    #  * business area. Actual amounts may be generated in a source application and then
    #  * loaded to a specific ledger within the enterprise general ledger or budget
    #  * application.
    #  * @created 27-Dec-2023 5:15:13 PM
    def __init__(self):
        self.market_ledger_entries = [MarketLedgerEntry()]
