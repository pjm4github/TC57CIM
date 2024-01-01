# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcIEEEST1AUELselectorKind import \
    ExcIEEEST1AUELselectorKind
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeSt1A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST1A model. This model represents
    systems in which excitation power is supplied through a transformer from the
    generator terminals (or the unit's auxiliary bus) and is regulated by a
    controlled rectifier.  The maximum exciter voltage available from such systems
    is directly related to the generator terminal voltage.
    Reference: IEEE Standard 421.5-2005 Section 7.1.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        """
        Constructor for ExcIEEESt1A
        """
        super().__init__()
        self.ilr: Optional[PU] = PU()  # Exciter output current limit reference (I_LR). Typical Value = 0
        self.ka: Optional[PU] = PU()  # Voltage regulator gain (K_A). Typical Value = 190
        self.kc: Optional[PU] = PU()  # Rectifier loading factor proportional to commutating reactance (K_C). Typical Value = 0.08
        self.kf: Optional[PU] = PU()  # Excitation control system stabilizer gains (K_F). Typical Value = 0
        self.klr: Optional[PU] = PU()  # Exciter output current limiter gain (K_LR). Typical Value = 0
        self.pssin: Optional[bool] = False  # Selector of the Power System Stabilizer (PSS) input (PSSin).
        # True = PSS input (Vs) added to error signal
        # False = PSS input (Vs) added to voltage regulator output. Typical Value = True
        self.ta: Optional[Seconds] = Seconds()  # Voltage regulator time constant (T_A). Typical Value = 0
        self.tb: Optional[Seconds] = Seconds()  # Voltage regulator time constant (T_B). Typical Value = 10
        self.tb1: Optional[Seconds] = Seconds()  # Voltage regulator time constant (T_B1). Typical Value = 0
        self.tc: Optional[Seconds] = Seconds()  # Voltage regulator time constant (T_C). Typical Value = 1
        self.tc1: Optional[Seconds] = Seconds()  # Voltage regulator time constant (T_C1). Typical Value = 0
        self.tf: Optional[Seconds] = Seconds()  # Excitation control system stabilizer time constant (T_F). Typical Value = 1
        self.uelin: Optional[ExcIEEEST1AUELselectorKind] = ExcIEEEST1AUELselectorKind()  # Selector of the connection of the UEL input (UEL_in). Typical Value = ignoreUELsignal.
        self.vamax: Optional[PU] = PU()  # Maximum voltage regulator output (V_AMAX). Typical Value = 14.5
        self.vamin: Optional[PU] = PU()  # Minimum voltage regulator output (V_AMIN). Typical Value = -14.5
        self.vimax: Optional[PU] = PU()  # Maximum voltage regulator input limit (V_IMAX). Typical Value = 999
        self.vimin: Optional[PU] = PU()  # Minimum voltage regulator input limit (V_IMIN). Typical Value = -999
        self.vrmax: Optional[PU] = PU()  # Maximum voltage regulator outputs (V_RMAX). Typical Value = 7.8
        self.vrmin: Optional[PU] = PU()  # Minimum voltage regulator outputs (V_RMIN). Typical Value = -6.7
