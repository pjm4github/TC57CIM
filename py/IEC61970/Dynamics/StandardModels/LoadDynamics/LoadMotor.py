# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 16:32:51 2023
from typing import Optional

from IEC61970.Dynamics.StandardModels.LoadDynamics.LoadAggregate import LoadAggregate


class LoadMotor:
    """
    Aggregate induction motor load. This model is used to represent a fraction of an ordinary load as "induction motor
    load". It allows load that is treated as ordinary constant power in power flow analysis to be represented by an
    induction motor in dynamic simulation. If Lpp = 0. or Lpp = Lp, or Tppo = 0., only one cage is represented.
    Magnetic saturation is not modelled. Either a "one-cage" or "two-cage" model of the induction machine can be
    modelled. Magnetic saturation is not modelled. This model is intended for representation of aggregations of many
    motors dispersed through a load represented at a high voltage bus but where there is no information on the
    characteristics of individual motors. This model treats a fraction of the constant power part of a load as a motor.
    During initialisation, the initial power drawn by the motor is set equal to Pfrac times the constant P part of the
    static load. The remainder of the load is left as static load. The reactive power demand of the motor is calculated
    during initialisation as a function of voltage at the load bus. This reactive power demand may be less than or greater
    than the constant Q component of the load. If the motor's reactive demand is greater than the constant Q component of
    the load, the model inserts a shunt capacitor at the terminal of the motor to bring its reactive demand down to equal
    the constant Q reactive load. If a motor model and a static load model are both present for a load, the Pfrac is
    assumed to be subtracted from the power flow constant P load before the static load model is applied.
    The remainder of the load, if any, is then represented by the static load model.
    """

    def __init__(self) -> None:
        self.d: Optional[float] = 2.0  # Damping factor (D). Unit = delta P/delta speed. Typical Value = 2.
        self.h: Optional[float] = 0.4  # Inertia constant (H) (not=0). Typical Value = 0.4.
        self.lfac: Optional[float] = 0.8  # Loading factor - ratio of initial P to motor MVA base (Lfac). Typical Value = 0.8.
        self.lp: Optional[float] = 0.15  # Transient reactance (Lp). Typical Value = 0.15.
        self.lpp: Optional[float] = 0.15  # Subtransient reactance (Lpp). Typical Value = 0.15.
        self.ls: Optional[float] = 3.2  # Synchronous reactance (Ls). Typical Value = 3.2.
        self.pfrac: Optional[float] = 0.3  # Fraction of constant-power load to be represented by this motor model (Pfrac) (>=0.0 and <=1.0). Typical Value = 0.3.
        self.ra: Optional[float] = 0.0  # Stator resistance (Ra). Typical Value = 0.
        self.tbkr: Optional[float] = 0.08  # Circuit breaker operating time (Tbkr). Typical Value = 0.08.
        self.tpo: Optional[float] = 1.0  # Transient rotor time constant (Tpo) (not=0). Typical Value = 1.
        self.tppo: Optional[float] = 0.02  # Subtransient rotor time constant (Tppo). Typical Value = 0.02.
        self.tv: Optional[float] = 0.1  # Voltage trip pickup time (Tv). Typical Value = 0.1.
        self.vt: Optional[float] = 0.7  # Voltage threshold for tripping (Vt). Typical Value = 0.7.
        self.load_aggregate: Optional[LoadAggregate] = LoadAggregate()  # Aggregate load to which this aggregate motor (dynamic) load belongs.
