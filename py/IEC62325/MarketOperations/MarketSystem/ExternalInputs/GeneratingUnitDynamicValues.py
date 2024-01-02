# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.Flowgate import Flowgate
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.MktGeneratingUnit import MktGeneratingUnit

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
        self.loss_factorfloat = 0.0  # Loss Factor
        self.maximum_mwfloat = 0.0  # The maximum active power generation of the unit in MW
        self.minimum_mwfloat = 0.0  # The minimum active power generation of the unit in MW
        self.mvarfloat = 0.0  # Unit reactive power generation in MVAR
        self.mwfloat = 0.0  # Unit active power generation in MW
        self.sensitivityfloat = 0.0  # Unit sensitivity factor. The distribution factors (DFAX) for the unit
        self.flowgateOptional[Flowgate] = Flowgate()
        self.mkt_generating_unitOptional[MktGeneratingUnit] = MktGeneratingUnit()
