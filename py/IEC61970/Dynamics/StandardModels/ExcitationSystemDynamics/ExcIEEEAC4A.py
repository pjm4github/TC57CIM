# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeAc4a(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC4A model. The model represents
    type AC4A alternator-supplied controlled-rectifier excitation system which is
    quite different from the other type ac systems. This high initial response
    excitation system utilizes a full thyristor bridge in the exciter output
    circuit. The voltage regulator controls the firing of the thyristor bridges.
    The exciter alternator uses an independent voltage regulator to control its
    output voltage to a constant value. These effects are not modeled; however,
    transient loading effects on the exciter alternator are included.
    
    Reference: IEEE Standard 421.5-2005 Section 6.4.
    
    author: pcha006
    version: 1.0
    created: 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.ka: float = 200.  # Voltage regulator gain (K_A). Typical Value = 200.
        self.kc: float = 0.0  # Rectifier loading factor proportional to commutating reactance (K_C). Typical Value = 0.
        self.ta: Seconds = Seconds(0.015)  # Voltage regulator time constant (T_A). Typical Value = 0.015.
        self.tb: Seconds = Seconds(10)  # Voltage regulator time constant (T_B). Typical Value = 10.
        self.tc: Seconds = Seconds(1)  # Voltage regulator time constant (T_C). Typical Value = 1.
        self.vimax: float = 10.0  # Maximum voltage regulator input limit (V_IMAX). Typical Value = 10.
        self.vimin: float = -10.0  # Minimum voltage regulator input limit (V_IMIN). Typical Value = -10.
        self.vrmax: float = 5.64  # Maximum voltage regulator output (V_RMAX). Typical Value = 5.64.
        self.vrmin: float = -4.53  # Minimum voltage regulator output (V_RMIN). Typical Value = -4.53.
