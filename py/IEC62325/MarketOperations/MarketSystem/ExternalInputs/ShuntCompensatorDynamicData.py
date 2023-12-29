# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC62325.MarketOperations.MarketSystem.ExternalInputs.MktShuntCompensator import MktShuntCompensator


class ShuntCompensatorDynamicData:
    """
    Optimal Power Flow or State Estimator Filter Bank Data for OTS. This is used for RealTime,
    Study and Maintenance Users.
    @created 27-Dec-2023 3:32:15 PM
    """

    def __init__(self) -> None:
        """
        Constructor for ShuntCompensatorDynamicData.
        """
        self.connection_status: Optional[int] = 0  # The current status for the Voltage Control Capacitor 1= Connected 0 = Disconnected
        self.desired_voltage: Optional[float] = 0.0  # The desired voltage for the Voltage Control Capacitor
        self.mVar_injection: Optional[float] = 0.0  # The injection of reactive power of the filter bank in the NA solution or VCS reactive power production
        self.step_position: Optional[int] = 0  # Voltage control capacitor step position
        self.voltage_regulation_status: Optional[bool] = False  # Indicator if the voltage control this is regulating True = Yes, False = No
        self.mkt_shunt_compensator: Optional[MktShuntCompensator] = MktShuntCompensator()
