# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Optional


class BidSelfSched:

    def __init__(self) -> None:
        self.balancing_flag: Optional[str] = ""  # This is a Y/N flag for a self-schedule of a resource per market per date and hour, using a specific TR ID. It indicates whether a self-schedule using a TR is balanced with another self-schedule using the same TR ID.
        self.bid_type: Optional[str] = ""  # bidType has two types as the required output of requirements and qualified pre-dispatch.
        self.priority_flag: Optional[str] = ""  # This is a Y/N flag for a self-schedule of a resource per market per date and hour, using a specific TR ID. It indicates whether a self-schedule using a TR has scheduling priority in DAM/RTM.
        self.pump_self_sched_mw: float = 0.0  # Contains the PriceTaker, ExistingTransmissionContract, TransmissionOwnershipRights pumping self-schedule quantity. If this value is not null, then the unit is in pumping mode.
        self.reference_type: Optional[str] = ""  # Indication of which type of self-schedule is being referenced.
        self.self_sched_mw: float = 0.0  # Self scheduled value
        self.self_sched_spt_resource: Optional[str] = ""  # Price Taker Export Self Sched Support Resource
        self.self_sched_type: Optional[str] = ""  # This attribute is used to specify if a bid includes a self-sched bid. If so, what self-sched type is it. (ETC, TOR, RMR, RGMR, RMT, PT, LPT, SP, RA)
        self.update_type: Optional[str] = ""
        self.wheeling_transaction_reference: Optional[str] = ""  # A unique identifier of a wheeling transaction. A wheeling transaction is a balanced Energy exchange among Supply and Demand Resources.
