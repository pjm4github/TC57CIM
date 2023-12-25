# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:39:55 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.OperationalLimits import OperationalLimit


class ActivePowerLimit(OperationalLimit):
    """
    Limit on active power flow.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.normal_value: ActivePower = ActivePower()
        self.value: ActivePower = ActivePower()

