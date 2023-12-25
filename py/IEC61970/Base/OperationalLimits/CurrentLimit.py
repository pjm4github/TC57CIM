# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:39:55 2023
# local import of CurrentFlow from the IEC61970.Base package
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.OperationalLimits.OperationalLimit import OperationalLimit


class CurrentLimit(OperationalLimit):
    """
    Operational limit on current.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """

    def __init__(self) -> None:
        """
        Constructor for CurrentLimit
        """
        super().__init__()
        self.normal_value: CurrentFlow = CurrentFlow()
        self.value: CurrentFlow = CurrentFlow()
