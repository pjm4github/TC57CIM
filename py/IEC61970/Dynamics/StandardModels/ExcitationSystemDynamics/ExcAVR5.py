# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from datetime import timedelta

from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAvr5(ExcitationSystemDynamics):
    """
    Manual excitation control with field circuit resistance. This model can be used
    as a very simple representation of manual voltage control.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.ka: PU = PU()
        """Gain (Ka)"""
        
        self.rex: PU = PU()
        """Effective Output Resistance (Rex). Rex represents the effective output
        resistance seen by the excitation system."""
        
        self.ta: timedelta
        """Time constant (Ta)"""
