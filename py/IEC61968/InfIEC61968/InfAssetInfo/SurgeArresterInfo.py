# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from typing import Union

from IEC61968.Assets.AssetInfo import AssetInfo
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from IEC61970.Base.Domain.Voltage import Voltage


class SurgeArresterInfo(AssetInfo):

    def __init__(self) -> None:
        super().__init__()

        self.continuous_operating_voltage: Union[
            Voltage, None] = Voltage()  # Maximum continuous power frequency voltage allowed on the surge arrester.

        self.is_polymer: Union[bool, None]  # If True, the arrester has a polymer housing, porcelain otherwise.

        self.lightning_impulse_discharge_voltage: Union[
            Voltage, None] = Voltage()  # Residual voltage during an 8x20 microsecond current impulse at the nominal discharge current level.

        self.line_discharge_class: Union[
            int, None]  # Determines the arrester energy discharge capability. Choices are limited to 0 (none) through 5 (highest) by IEC 60099. Classes 1..3 require a 10-kA nominal discharge current. Classes 4..5 require a 20-kA nominal discharge current. Lower nominal discharge currents must use class 0.

        self.nominal_discharge_current: Union[
            CurrentFlow, None] = CurrentFlow()  # The lightning discharge current used to classify the arrester. Choices are limited to 1.5, 2.5, 5, 10, and 20 kA by IEC 60099.

        self.pressure_relief_class: Union[
            CurrentFlow, None] = CurrentFlow()  # Fault current level at which all parts of the failed arrester lie within a circle prescribed by IEC 60099.

        self.rated_voltage: Union[
            Voltage, None] = Voltage()  # The temporary overvoltage (TOV) level at power frequency that the surge arrester withstands for 10 seconds.

        self.steep_front_discharge_voltage: Union[
            Voltage, None] = Voltage()  # Residual voltage during a current impulse with front time of 1 microsecond, and magnitude equal to the nominal discharge current level.

        self.switching_impulse_discharge_voltage: Union[
            Voltage, None] = Voltage()  # Residual voltage during a current impulse with front time of at least 30 micro: Seconds, and magnitude specified in IEC 60099 for the line discharge class. Does not apply to line discharge class 0.
