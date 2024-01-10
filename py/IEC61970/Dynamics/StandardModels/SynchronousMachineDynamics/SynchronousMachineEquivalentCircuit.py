# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:07:00 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.SynchronousMachineDetailed import \
    SynchronousMachineDetailed


class SynchronousMachineEquivalentCircuit(SynchronousMachineDetailed):
    """
    The electrical equations for all variations of the synchronous models are based
    on the SynchronousEquivalentCircuit diagram for the direct and quadrature axes.
    
    
    Equations for conversion between Equivalent Circuit and Time Constant Reactance forms:

    Xd = Xad + Xl
    X'd = Xl + Xad * Xfd / (Xad + Xfd)
    X"d = Xl + Xad * Xfd * X1d / (Xad * Xfd + Xad * X1d + Xfd * X1d)
    Xq = Xaq + Xl
    X'q = Xl + Xaq * X1q / (Xaq+ X1q)
    X"q = Xl + Xaq * X1q* X2q / (Xaq * X1q + Xaq * X2q + X1q * X2q)

    T'do = (Xad + Xfd) / (omega_0 * Rfd)
    T"do = (Xad * Xfd + Xad * X1d + Xfd * X1d) / (omega_0 * R1d * (Xad + Xfd))
    T'qo = (Xaq + X1q) / (omega_0 * R1q)
    T"qo = (Xaq * X1q + Xaq * X2q + X1q * X2q)/ (omega_0 * R2q * (Xaq + X1q))
    
    Same equations using CIM attributes from
    SynchronousMachineTimeConstantReactance class on left of = sign and
    SynchronousMachineEquivalentCircuit class on right (except as noted):
    xDirectSync = xad + RotatingMachineDynamics.statorLeakageReactance
    xDirectTrans = RotatingMachineDynamics.statorLeakageReactance +
                xad * xfd / (xad + xfd)
    xDirectSubtrans = RotatingMachineDynamics.statorLeakageReactance +
                xad * xfd * x1d / (xad * xfd + xad * x1d + xfd * x1d)
    xQuadSync = xaq + RotatingMachineDynamics.statorLeakageReactance
    xQuadTrans = RotatingMachineDynamics.statorLeakageReactance +
                xaq * x1q / (xaq+ x1q)
    xQuadSubtrans = RotatingMachineDynamics.statorLeakageReactance +
                xaq * x1q * x2q / (xaq * x1q + xaq * x2q + x1q * x2q)
    tpdo = (xad + xfd) / (2*pi*nominal frequency * rfd)
    tppdo = (xad * xfd + xad * x1d + xfd * x1d) /
                (2*pi*nominal frequency * r1d * (xad + xfd))
    tpqo = (xaq + x1q) / (2*pi*nominal frequency * r1q)
    tppqo = (xaq * x1q + xaq * x2q + x1q * x2q)/
                (2*pi*nominal frequency * r2q * (xaq + x1q))
    
    Are only valid for a simplified model where "Canay" reactance is zero.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.r1d: PU = PU()  # D-axis damper 1 winding resistance
        self.r1q: PU = PU()  # Q-axis damper 1 winding resistance
        self.r2q: PU = PU()  # Q-axis damper 2 winding resistance
        self.rfd: PU = PU()  # Field winding resistance
        self.x1d: PU = PU()  # D-axis damper 1 winding leakage reactance
        self.x1q: PU = PU()  # Q-axis damper 1 winding leakage reactance
        self.x2q: PU = PU()  # Q-axis damper 2 winding leakage reactance
        self.xad: PU = PU()  # D-axis mutual reactance
        self.xaq: PU = PU()  # Q-axis mutual reactance
        self.xf1d: PU = PU()  # Differential mutual ("Canay") reactance
        self.xfd: PU = PU()  # Field winding leakage reactance
