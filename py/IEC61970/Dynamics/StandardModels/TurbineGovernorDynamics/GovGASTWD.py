# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.Temperature import Temperature
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGastwd(TurbineGovernorDynamics):
    """
    Woodward Gas turbine governor model.
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.a: float = 1.0  # Valve positioner (A)
        self.af1: PU = PU(1.0) # Exhaust temperature Parameter (Af1)
        self.af2: PU = PU(1.0) # Coefficient equal to 0.5(1-speed) (Af2)
        self.b: float = 1.0  # Valve positioner (B)
        self.bf1: PU = PU(1.0) # (Bf1). Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x Tr.
        self.bf2: PU = PU(1.0) # Turbine Torque Coefficient K_hhv (depends on heating value of fuel stream in combustion chamber) (Bf2).
        self.c: float = 1.0  # Valve positioner (C)
        self.cf2: PU = PU(1.0) # Coefficient defining fuel flow where power output is 0% (Cf2). Synchronous but no output. Typically 0.23 x K_hhv (23% fuel flow).
        self.ecr: PU = PU(1.0) # Combustion reaction time delay (Ecr).
        self.etd: float = 1.0  # Turbine and exhaust delay (Etd).
        self.k3: PU = PU(1.0) # Ratio of Fuel Adjustment (K3).
        self.k4: PU = PU(1.0) # Gain of radiation shield (K4).
        self.k5: PU = PU(1.0) # Gain of radiation shield (K5).
        self.k6: PU = PU(1.0) # Minimum fuel flow (K6).
        self.kd: PU = PU(1.0) # Drop Governor Gain (Kd).
        self.kdroop: PU = PU(1.0) # (Kdroop).
        self.kf: PU = PU(1.0) # Fuel system feedback (Kf).
        self.ki: PU = PU(1.0) # Isochronous Governor Gain (Ki).
        self.kp: PU = PU(1.0) # PID Proportional gain (Kp).
        self.mwbase: ActivePower = ActivePower(1.0)  # Base for power values (MWbase) (> 0). Unit = MW.
        self.t: Seconds = Seconds() # Fuel Control Time Constant (T).
        self.t3: Seconds = Seconds() # Radiation shield time constant (T3).
        self.t4: Seconds = Seconds() # Thermocouple time constant (T4).
        self.t5: Temperature = Temperature() # Temperature control time constant (T5).
        self.tc: Temperature = Temperature() # Temperature control (Tc).
        self.tcd: Seconds = Seconds() # Compressor discharge time constant (Tcd).
        self.td: Seconds = Seconds() # Power transducer time constant (Td).
        self.tf: Seconds = Seconds() # Fuel system time constant (Tf).
        self.tmax: PU = PU() # Maximum Turbine limit (Tmax).
        self.tmin: PU = PU() # Minimum Turbine limit (Tmin).
        self.tr: Temperature = Temperature() # Rated temperature (Tr).
        self.trate: ActivePower = ActivePower() # Turbine rating (Trate). Unit = MW.
        self.tt: Seconds = Seconds(1.0)  # Temperature controller integration rate (Tt)
