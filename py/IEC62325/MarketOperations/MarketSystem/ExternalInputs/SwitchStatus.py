# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.MktSwitch import MktSwitch
from IEC62325.MarketOperations.MktDomain.SwitchStatusType import SwitchStatusType

class SwitchStatus:
    """
    Optimal Power Flow or State Estimator Circuit Breaker Status.
    @created 27-Dec-2023 3:32:25 PM
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of SwitchStatus.
        """ 
        self.switch_status: SwitchStatusType = SwitchStatusType.OPEN
        self.mkt_switch: MktSwitch = MktSwitch()
