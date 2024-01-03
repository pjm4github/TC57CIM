# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:25:13 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineLoadControllerDynamics.TurbineLoadControllerDynamics import \
    TurbineLoadControllerDynamics


class TurbLCFB1(TurbineLoadControllerDynamics):
    """
    Turbine Load Controller model developed in the WECC. This model represents a
    supervisory turbine load controller that acts to maintain turbine power at a
    set value by continuous adjustment of the turbine governor speed-load reference.
    This model is intended to represent slow reset 'outer loop' controllers
    managing the action of the turbine governor.
    """

    def __init__(self):
        super().__init__()
        self.db = PU(0)  # Controller dead band (db). Typical Value = 0
        self.emax = PU(0.02)  # Maximum control error (Emax) (note 4). Typical Value = 0.02
        self.fb = PU(0)  # Frequency bias gain (Fb). Typical Value = 0
        self.fbf = False  # Frequency bias flag (Fbf). True = enable frequency bias, False = disable frequency bias. Typical Value = False
        self.irmax = PU()  # Maximum turbine speed/load reference bias (Irmax) (note 3). Typical Value = 0
        self.ki = PU()  # Integral gain (Ki). Typical Value = 0
        self.kp = PU()  # Proportional gain (Kp). Typical Value = 0
        self.mwbase = ActivePower(.1)  # Base for power values (MWbase) (>0). Unit = MW
        self.pbf = False  # Power controller flag (Pbf). True = enable load controller, False = disable load controller. Typical Value = False
        self.pmwset = ActivePower(0)  # Power controller setpoint (Pmwset) (note 1). Unit = MW. Typical Value = 0
        self.speed_reference_governor = True  # Type of turbine governor reference (Type). True = speed reference governor, False = load reference governor. Typical Value = True
        self.tpelec = Seconds(0)  # Power transducer time constant (Tpelec). Typical Value = 0
