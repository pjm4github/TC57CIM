# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:39:55 2023
from typing import Any, Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Terminal import Terminal


class BranchGroupTerminal:
    """
    A specific directed terminal flow for a branch group.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """

        # The flow into the terminal is summed if set true.
        # The flow out of the terminal is summed if set false.
        self.positive_flow_in: Optional[bool] = False

        # The terminal to be summed.
        self.terminal: Optional[Any] = Terminal()
