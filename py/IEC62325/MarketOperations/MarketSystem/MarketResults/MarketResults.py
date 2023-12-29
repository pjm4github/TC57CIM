# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

class MarketResults:
    """
    This class holds elements that are single values for the entire market time horizon. That is, for the Day Ahead market, there is 1 value for each element,
    not hourly based. Is a summary of the market run.
    @created 28-Dec-2023 8:23:09 PM
    """

    def __init__(self) -> None:
        self.ancillary_svc_cost: float = 0.0  # Total AS Cost (i.e., payment) ($) over the time horizon
        self.contingent_operating_res_avail: str = ""  # Global Contingent Operating Reserve Availability Indicator (Yes/No)
        self.energy_cost: float = 0.0  # Total Energy Cost ($) over the time horizon
        self.minimum_load_cost: float = 0.0  # Total Minimum Load Cost ($) over the time horizon
        self.start_up_cost: float = 0.0  # Total Start-up Cost ($) over the time horizon
        self.total_cost: float = 0.0  # Total Cost (Energy + AS) cost ($) over the time horizon
        self.total_ruc_cost: float = 0.0  # The total RUC capacity cost for this interval

