# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:57:45 2023
from IEC61970.Dynamics.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics import \
    AsynchronousMachineDynamics


class AsynchronousMachineEquivalentCircuit(AsynchronousMachineDynamics):
    """
    The electrical equations of all variations of the asynchronous model are based
    on the AsynchronousEquivalentCircuit diagram for the direct and quadrature axes,
    with two equivalent rotor windings in each axis.
    Equations for conversion between Equivalent Circuit and Time Constant Reactance forms:
    Reactance forms:
    Xs = Xm + Xl
    X' = Xl + Xm * Xlr1 / (Xm + Xlr1)
    X'' = Xl + Xm * Xlr1* Xlr2 / (Xm * (Xlr1 + Xm * Xlr2 + Xlr1 * Xlr2))
    T'o = (Xm + Xlr1) / (omega_0 * Rr1)
    T''o = (Xm * Xlr1 + Xm * Xlr2 + Xlr1 * Xlr2) / (omega_0 * Rr2 * (Xm + Xlr1))
    Same equations using CIM attributes from
    AsynchronousMachineTimeConstantReactance class on left of = sign and
    AsynchronousMachineEquivalentCircuit class on right (except as noted):
    xs = xm + RotatingMachineDynamics.statorLeakageReactance
    xp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1 / (xm + xlr1)
    xpp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1* xlr2 / (xm * (xlr1 + xm * xlr2 + xlr1 * xlr2))
    tpo = (xm + xlr1) / (2* pi* nomimal frequency * rr1)
    tppo = (xm * xlr1 + xm * xlr2 + xlr1 * xlr2) / (2* pi* nomimal frequency * rr2 * (xm + xlr1))
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self):
        super().__init__()
        self.rr1: float = 0.0  # Damper 1 winding resistance
        self.rr2: float = 0.0  # Damper 2 winding resistance
        self.xlr1: float = 0.0  # Damper 1 winding leakage reactance
        self.xlr2: float = 0.0  # Damper 2 winding leakage reactance
        self.xm: float = 0.0  # Magnetizing reactance
