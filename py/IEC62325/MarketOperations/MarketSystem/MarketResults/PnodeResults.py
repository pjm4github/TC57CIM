# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime


class PnodeResults:
    """
    Provides the total price, the cost component, the loss component, and the congestion component for Pnodes
    for the forward and real time markets. There are several prices produced based on the run type (MPM, RUC,
    Pricing, or Scheduling/Dispatch).
    @created 28-Dec-2023 8:24:38 PM
    """

    def __init__(self) -> None:
        self.congest_lmp: float = 0.0  # Congestion component of Location Marginal Price (LMP) in monetary units per MW.
        self.cost_lmp: float = 0.0  # Cost component of Locational Marginal Pricing (LMP) in monetary units per MW.
        self.loss_lmp: float = 0.0  # Loss component of Location Marginal Price (LMP) in monetary units per MW.
        self.marginal_clearing_price: float = 0.0  # Locational Marginal Price (LMP) ($/MWh).
        self.scheduled_mw: float = 0.0  # Total MW schedule at the pnode.
        self.update_time_stamp: DateTime = DateTime()
        self.update_type: str = ""
        self.update_user: str = ""
