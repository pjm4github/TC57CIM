# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023

from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.ReferenceData.MktContingency import MktContingency


class ConstraintResults:
    def __init__(self) -> None:
        self.base_flow: float = 0.0
        self.bg_limit: float = 0.0
        self.bgtr_res_cap: float = 0.0
        self.binding_limit: float = 0.0
        self.cleared_value: float = 0.0
        self.competitive_path_constraint: str = ""
        self.constraint_type: str = ""
        self.limit_flag: str = ""
        self.optimization_flag: str = ""
        self.overload_mw: float = 0.0
        self.percent_mw: float = 0.0
        self.shadow_price: float = 0.0
        self.update_time_stamp: DateTime = DateTime()
        self.update_type: str = ""
        self.update_user: str = ""
        self.mkt_contingency: MktContingency = MktContingency()
