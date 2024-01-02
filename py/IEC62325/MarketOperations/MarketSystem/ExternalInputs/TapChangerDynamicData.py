# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC62325.MarketOperations.MarketSystem.ExternalInputs.MktTapChanger import MktTapChanger


class TapChangerDynamicData:
    """
    Optimal Power Flow or State Estimator Phase Shifter Data. This is used for
    RealTime, Study and Maintenance Users. SE Solution Phase Shifter Measurements
    from the last run of SE.
    @created 27-Dec-2023 3:32:52 PM
    """

    def __init__(self) -> None:
        """
        Constructor for TapChangerDynamicData class
        """

        self.angle_regulation_statusbool = False  # True means the phase shifter is regulating
        self.desired_mwfloat = 0.0  # Phase Shifter Desired MW. The active power regulation setpoint of the phase shifter
        self.desired_voltagefloat = 0.0  # The desired voltage for the LTC
        self.maximum_anglefloat = 0.0  # The maximum phase angle shift of the phase shifter
        self.minimum_anglefloat = 0.0  # The minimum phase angle shift of the phase shifter
        self.solved_anglefloat = 0.0  # Phase Shifter Angle. The solved phase angle shift of the phase shifter
        self.tap_positionfloat = 0.0  # Tap position of the phase shifter, high-side tap position of the transformer, or low-side tap position of the transformer
        self.voltage_regulation_statusbool = False  # Indicator if the LTC transformer is regulating True = Yes, False = No
        self.mkt_tap_changerOptional[MktTapChanger] = MktTapChanger()

