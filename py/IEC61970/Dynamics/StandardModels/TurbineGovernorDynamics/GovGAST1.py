# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGast1(TurbineGovernorDynamics):
    """
    Modified single shaft gas turbine.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.a: float = 0.8  # Turbine power time constant numerator scale factor (a) Typical Value = 0.8
        self.b: float = 1.0  # Turbine power time constant denominator scale factor (b) Typical Value = 1
        self.db1: Frequency = Frequency(0.0)  # Intentional dead-band width (db1) Unit = Hz.  Typical Value = 0
        self.db2: ActivePower = ActivePower(0.0)  # Unintentional dead-band (db2) Unit = MW.  Typical Value = 0
        self.eps: Frequency = Frequency(0.0)  # Intentional db hysteresis (eps) Unit = Hz.  Typical Value = 0
        self.fidle: PU = PU(0.18)  # Fuel flow at zero power output (Fidle) Typical Value = 0.18
        self.gv1: PU = PU(.0)  # Nonlinear gain point 1, PU gv (Gv1) Typical Value = 0
        self.gv2: PU = PU(.0)  # Nonlinear gain point 2, PU gv (Gv2) Typical Value = 0
        self.gv3: PU = PU(.0)  # Nonlinear gain point 3, PU gv (Gv3) Typical Value = 0
        self.gv4: PU = PU(.0)  # Nonlinear gain point 4, PU gv (Gv4) Typical Value = 0
        self.gv5: PU = PU(.0)  # Nonlinear gain point 5, PU gv (Gv5) Typical Value = 0
        self.gv6: PU = PU(.0)  # Nonlinear gain point 6, PU gv (Gv6) Typical Value = 0
        self.ka: PU = PU(.0)  # Governor gain (Ka) Typical Value = 0
        self.kt: PU = PU(3.0)  # Temperature limiter gain (Kt) Typical Value = 3
        self.lmax: PU = PU(1.0)  # Ambient temperature load limit (Lmax) Typical Value = 1
        self.loadinc: PU = PU(0.05)  # Valve position change allowed at fast rate (Loadinc) Typical Value = 0.05
        self.ltrate: float = 0.02  # Maximum long term fuel valve opening rate (Ltrate) Typical Value = 0.02
        self.mwbase: ActivePower = ActivePower(1.0)  # Base for power values (MWbase) (> 0) Unit = MW.
        self.pgv1: PU = PU(.0)  # Nonlinear gain point 1, PU power (Pgv1) Typical Value = 0
        self.pgv2: PU = PU(.0)  # Nonlinear gain point 2, PU power (Pgv2) Typical Value = 0
        self.pgv3: PU = PU(.0)  # Nonlinear gain point 3, PU power (Pgv3) Typical Value = 0
        self.pgv4: PU = PU(.0)  # Nonlinear gain point 4, PU power (Pgv4) Typical Value = 0
        self.pgv5: PU = PU(.0)  # Nonlinear gain point 5, PU power (Pgv5) Typical Value = 0
        self.pgv6: PU = PU(.0)  # Nonlinear gain point 6, PU power (Pgv6) Typical Value = 0
        self.r: PU = PU(.04)  # Permanent droop (R) Typical Value = 0.04
        self.rmax: float = 1.0  # Maximum fuel valve opening rate (Rmax) Unit = PU/sec.  Typical Value = 1
        self.t1: Seconds = Seconds(.5)  # Governor mechanism time constant (T1) Typical Value = 0.5
        self.t2: Seconds = Seconds(.5)  # Turbine power time constant (T2) Typical Value = 0.5
        self.t3: Seconds = Seconds(3)  # Turbine exhaust temperature time constant (T3) Typical Value = 3
        self.t4: Seconds = Seconds(0)  # Governor lead time constant (T4) Typical Value = 0
        self.t5: Seconds = Seconds(0)  # Governor lag time constant (T5) Typical Value = 0
        self.tltr: Seconds = Seconds(10)  # Valve position averaging time constant (Tltr) Typical Value = 10
        self.vmax: PU = PU(1.0)  # Maximum turbine power, PU of MWbase (Vmax) Typical Value = 1
        self.vmin: PU = PU(.0)  # Minimum turbine power, PU of MWbase (Vmin) Typical Value = 0
