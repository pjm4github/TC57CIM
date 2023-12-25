# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:39:55 2023
# Local imports
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.OperationalLimits.OperationalLimit import OperationalLimit


class VoltageLimit(OperationalLimit):
    """
    Operational limit applied to voltage.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:30 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.normal_value: Voltage = Voltage()
        self.value: Voltage = Voltage()
