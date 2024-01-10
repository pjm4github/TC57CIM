# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC62325.MarketCommon.MktGeneratingUnit import MktGeneratingUnit
from IEC62325.MarketOperations.ReferenceData.Flowgate import Flowgate


class GeneratingUnitDynamicValues:
    """
    Optimal Power Flow or State Estimator Unit Data for Operator Training Simulator.
    This is used for RealTime, Study and Maintenance Users.
    @created 27-Dec-2023 3:28:44 PM
    """

    def __init__(self) -> None:
        """
        Constructor for GeneratingUnitDynamicValues
        """
        self.loss_factor: float = 0.0  # Loss Factor
        self.maximum_mw: float = 0.0  # The maximum active power generation of the unit in MW
        self.minimum_mw: float = 0.0  # The minimum active power generation of the unit in MW
        self.mvar: float = 0.0  # Unit reactive power generation in MVAR
        self.mw: float = 0.0  # Unit active power generation in MW
        self.sensitivity: float = 0.0  # Unit sensitivity factor. The distribution factors (DFAX) for the unit
        self.flowgate: Optional[Flowgate] = Flowgate()
        self.mkt_generating_unit: Optional[MktGeneratingUnit] = MktGeneratingUnit()
