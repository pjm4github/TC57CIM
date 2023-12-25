# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum

class PhaseShuntConnectionKind(Enum):
    """
    The configuration of phase connections for a single terminal device such as a
    load or capacitor.
    """
    
    D = 1  # "Delta connection."
    Y = 2  # "Wye connection."
    Yn = 3  # "Wye, with neutral brought out for grounding."
    I = 4  # "Independent winding, for single-phase connections."
    G = 5  # "Ground connection; use when explicit connection to ground needs to be expressed in
           # combination with the phase code, such as for electrical wire/cable or for meters."

