# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:59:32 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics

class DiscExcContIeeeDec3A(DiscontinuousExcitationControlDynamics):
    """
    The class represents IEEE Type DEC3A model. In some systems, the stabilizer
    output is disconnected from the regulator immediately following a severe fault
    to prevent the stabilizer from competing with action of voltage regulator
    during the first swing.

    Reference: IEEE Standard 421.5-2005 Section 12.4.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.tdrOptional[Seconds] = Seconds()  # Reset time delay (T_DR).
        self.vtminOptional[PU] = PU()  # Terminal undervoltage comparison level (V_TMIN).
