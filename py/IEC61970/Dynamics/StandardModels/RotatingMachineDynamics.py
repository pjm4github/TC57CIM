# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:55:16 2023
from typing import Optional

class RotatingMachineDynamics:
    """
    Abstract parent class for all synchronous and asynchronous machine standard
    models.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        """
        Constructor for the RotatingMachineDynamics class.
        """
        self.damping: Optional[float] = 0.0  # Damping torque coefficient
        """
        Damping torque coefficient (D). A proportionality constant that, when
        multiplied by the angular velocity of the rotor poles with respect to the
        magnetic field (frequency), results in the damping torque. This value is
        often zero when the sources of damping torques (generator damper windings,
        load damping effects, etc.) are modelled in detail. Typical Value = 0.
        """

        self.inertia: Optional[float] = 3.0  # Inertia constant
        """
        Inertia constant of generator or motor and mechanical load (H) (>0). This is
        the specification for the stored energy in the rotating mass when operating
        at rated speed. For a generator, this includes the generator plus all other
        elements (turbine, exciter) on the same shaft and has units of MW*sec. For a
        motor, it includes the motor plus its mechanical load. Conventional units
        are per unit on the generator MVA base, usually expressed as MW*second/MVA or
        just second. This value is used in the accelerating power reference frame for
        operator training simulator solutions. Typical Value = 3.
        """

        self.saturation_factor: Optional[float] = 0.02  # Saturation factor at rated terminal voltage (S_1) (>=0)
        """
        Saturation factor at rated terminal voltage (S1) (> or = 0). Not used by
        simplified model. Defined by defined by S(E1) in the
        SynchronousMachineSaturationParameters diagram. Typical Value = 0.02.
        """

        self.saturation_factor120: Optional[float] = 0.12  # Saturation factor at 120% of rated terminal voltage (S12) (> or = S1)
        """
        Saturation factor at 120% of rated terminal voltage (S12) (> or = S1). Not used
        by the simplified model, defined by S(E2) in the
        SynchronousMachineSaturationParameters diagram. Typical Value = 0.12.
        """

        self.stator_leakage_reactance: Optional[float] = 0.15  # Stator leakage reactance (Xl) (> or = 0)
        """
        Stator leakage reactance (Xl) (> or = 0). Typical Value = 0.15.
        """

        self.stator_resistance: Optional[float] = 0.005  # Stator (armature) resistance (Rs) (> or = 0)
        """
        Stator (armature) resistance (Rs) (> or = 0). Typical Value = 0.005.
        """  
