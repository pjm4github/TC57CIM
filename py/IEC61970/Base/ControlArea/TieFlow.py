# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:02:59 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ControlArea.AltTieMeas import AltTieMeas
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Terminal import Terminal


class TieFlow:
    """
    A flow specification in terms of location and direction for a control area.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:30 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.positive_flow_in: Optional[bool] = True
        """True if the flow into the terminal (load convention) is also flow into the control area.
        For example, this attribute should be true if using the tie line terminal further away
        from the control area. For example to represent a tie to a shunt component (like a load
        or generator) in another area, this is the near end of a branch and this attribute would
        be specified as false."""

        self.terminal: Optional[Terminal] = Terminal()
        """The terminal to which this tie flow belongs."""

        self.alt_tie_meas: Optional[AltTieMeas] = AltTieMeas()
        """The primary and alternate tie flow measurements associated with the tie flow."""



