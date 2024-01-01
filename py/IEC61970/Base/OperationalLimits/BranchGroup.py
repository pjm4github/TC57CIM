# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:39:55 2023
from datetime import datetime
from typing import Optional
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.ReactivePower import ReactivePower
from IEC61970.Base.OperationalLimits.BranchGroupTerminal import BranchGroupTerminal


class BranchGroup(IdentifiedObject):
    """A group of branch terminals whose directed flow summation is to be monitored. A
    branch group need not form a cutset of the network.
    @ author kdd
    @ version 1.0
    @ created 15-Dec-2023 4:38:26 PM
    """
    
    def __init__(self) -> None:
        """Default constructor
        """
        super().__init__()
        self.maximum_active_powerOptional[ActivePower] = ActivePower()  # The maximum active power flow.
        self.maximum_reactive_powerOptional[ReactivePower] = ReactivePower()  # The maximum reactive power flow.
        self.minimum_active_powerOptional[ActivePower] = ActivePower()  # The minimum active power flow.
        self.minimum_reactive_powerOptional[ReactivePower] = ReactivePower()  # The minimum reactive power flow.
        self.monitor_active_powerOptional[bool] = False  # Monitor the active power flow.
        self.monitor_reactive_powerOptional[bool] = False  # Monitor the reactive power flow.
        self.branch_group_terminalOptional[BranchGroupTerminal] = BranchGroupTerminal()  # The directed branch group terminals to be summed.
