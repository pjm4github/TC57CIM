# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:07:00 2023
from typing import Optional


from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.RotorKind import RotorKind
from IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.SynchronousMachineDetailed import \
    SynchronousMachineDetailed
from IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.SynchronousMachineModelKind import \
    SynchronousMachineModelKind


class SynchronousMachineTimeConstantReactance(SynchronousMachineDetailed):
    """
    Synchronous machine detailed modelling types are defined by the combination of
    the attributes SynchronousMachineTimeConstantReactance.model_type and
    SynchronousMachineTimeConstantReactance.rotor_type.
    
    Parameter notes:
    - The "p" in the time-related attribute names is a substitution for a
    "prime" in the usual parameter notation, e.g. tpdo refers to T'do.
    
    The parameters used for models expressed in time constant reactance form include:
    - RotatingMachine.ratedS (MVA base)
    - RotatingMachineDynamics.damping (D)
    - RotatingMachineDynamics.inertia (H)
    - RotatingMachineDynamics.saturationFactor (S1)
    - RotatingMachineDynamics.saturationFactor120 (S12)
    - RotatingMachineDynamics.statorLeakageReactance (Xl)
    - RotatingMachineDynamics.statorResistance (Rs)
    - SynchronousMachineTimeConstantReactance.ks (Ks)
    - SynchronousMachineDetailed.saturationFactorQAxis (S1q)
    - SynchronousMachineDetailed.saturationFactor120QAxis (S12q)
    - SynchronousMachineDetailed.efdBaseRatio
    - SynchronousMachineDetailed.ifdBaseType
    - SynchronousMachineDetailed.ifdBaseValue, if present
    - xDirectSync (Xd)
    - xDirectTrans (X'd)
    - xDirectSubtrans (X''d)
    - xQuadSync (Xq)
    - xQuadTrans (X'q)
    - xQuadSubtrans (X''q)
    - tpdo (T'do)
    - tppdo (T''do)
    - tpqo (T'qo)
    - tppqo (T''qo)
    - tc.
    """
    
    def __init__(self) -> None:
        """
        Constructor for SynchronousMachineTimeConstantReactance class
        """
        super().__init__()
        self.ks: float = 0.0  # Saturation loading correction factor (Ks) (>= 0). Used only by Type J model. Typical Value = 0.
        self.model_type: Optional[SynchronousMachineModelKind] = SynchronousMachineModelKind.SUBTRANSIENT_TYPE_F  # Type of synchronous machine model used in Dynamic simulation applications.
        self.rotor_type: Optional[RotorKind] = RotorKind.ROUND_ROTOR  # Type of rotor on physical machine.
        self.tc: Seconds = Seconds(0) # Damping time constant for "Canay" reactance. Typical Value = 0.
        self.tpdo: Seconds = Seconds(5) # Direct-axis transient rotor time constant (T'do) (> T''do). Typical Value = 5.
        self.tppdo: Seconds = Seconds(0.03) # Direct-axis subtransient rotor time constant (T''do) (> 0). Typical Value = 0.03.
        self.tppqo: Seconds = Seconds(0.03) # Quadrature-axis subtransient rotor time constant (T''qo) (> 0). Typical Value = 0.03.
        self.tpqo: Seconds = Seconds(0.5) # Quadrature-axis transient rotor time constant (T'qo) (> T''qo). Typical Value = 0.5.
        self.x_direct_subtrans: float = 0.2  # Direct-axis subtransient reactance (unsaturated) (X''d) (> Xl). Typical Value = 0.2.
        self.x_direct_sync: float = 1.8  # Direct-axis synchronous reactance (Xd) (>= X'd). Typical Value = 1.8.
        self.x_direct_trans: float = 0.5  # Direct-axis transient reactance (unsaturated) (X'd) (>= X''d). Typical Value = 0.5.
        self.x_quad_subtrans: float = 0.2  # Quadrature-axis subtransient reactance (X''q) (> Xl). Typical Value = 0.2.
        self.x_quad_sync: float = 1.6  # Quadrature-axis synchronous reactance (Xq) (>= X'q). Typical Value = 1.6.
        self.x_quad_trans: float = 0.3  # Quadrature-axis transient reactance (X'q) (>= X''q). Typical Value = 0.3.
