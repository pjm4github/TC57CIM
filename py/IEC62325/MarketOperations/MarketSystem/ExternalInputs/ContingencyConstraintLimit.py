# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023

from IEC61970.Base.Core.Curve import Curve
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.MWLimitSchedule import MWLimitSchedule
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.SecurityConstraintSum import SecurityConstraintSum
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransferInterfaceSolution import MktContingency


class ContingencyConstraintLimit(Curve):

    def __init__(self) -> None:
        super().__init__()
        self._mkt_contingency: MktContingency = MktContingency()
        self.mw_limit_schedules: MWLimitSchedule = MWLimitSchedule()
        self.security_constraint_sum: SecurityConstraintSum = SecurityConstraintSum()
