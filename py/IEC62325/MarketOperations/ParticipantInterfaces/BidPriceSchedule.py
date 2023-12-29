# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Optional

from IEC61970.Base.Core.RegularIntervalSchedule import RegularIntervalSchedule
from IEC62325.MarketOperations.MktDomain.BidMitigationStatus import BidMitigationStatus
from IEC62325.MarketOperations.MktDomain.BidMitigationType import BidMitigationType


class BidPriceSchedule(RegularIntervalSchedule):
    """
    Defines bid schedules to allow a product bid to use specified bid price curves
    for different time intervals.
    @created 28-Dec-2023 5:19:35 PM
    """

    def __init__(self):
        super().__init__()

        # BID Type:
        # I - Initial Bid;
        # F - Final Bid
        self.bid_type: Optional[BidMitigationType] = BidMitigationType.INITIAL

        # Mitigation Status:
        # 'S' - Mitigated by SMPM because of "misconduct"
        # 'L' - Mitigated by LMPM because of "misconduct"
        # 'R' - Modified by LMPM because of RMR rules
        # 'M' - Mitigated because of "misconduct" both by SMPM and LMPM
        # 'B' - Mitigated because of "misconduct" both by SMPM and modified by LMLM
        #       because of RMR rules
        # 'O' - original
        self.mitigation_status: Optional[BidMitigationStatus] = BidMitigationStatus.S

