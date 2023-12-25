# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:39:55 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ApparentPower import ApparentPower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.OperationalLimits.OperationalLimit import OperationalLimit


class ApparentPowerLimit(OperationalLimit):
    """
    Apparent power limit.
    @author: kdd
    @version: 1.0
    @created: 15-Dec-2023 4:38:26PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.normal_value: ApparentPower = ApparentPower()  # The normal apparent power limit
        self.value: ApparentPower = ApparentPower()  # The apparent power limit

