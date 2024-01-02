# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.Temperature import Temperature
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGast2(TurbineGovernorDynamics):
    """
    Gas turbine model.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.a: float = 0.0  # Valve positioner (A).

        # Exhaust temperature Parameter (Af1).  Unit = per unit temperature.
        # Based on temperature in degrees C.
        self.af1: PU = PU(0.0)
        self.af2: PU = PU(0.0)  # Coefficient equal to 0.5(1-speed) (Af2).
        self.b: float = 0.0  # Valve positioner (B).

        # (Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x Tr.
        # Unit = per unit temperature. Based on temperature in degrees C.
        self.bf1: PU = PU(0.0)

        # Turbine Torque Coefficient Khhv (depends on heating value of fuel stream in
        # combustion chamber) (Bf2).
        self.bf2: PU = PU(0.0)
        self.c: float = 0.0  # Valve positioner (C).

        # Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but no output.
        # Typically, 0.23 x Khhv (23% fuel flow).
        self.cf2: PU = PU(0.0)
        self.ecr: Seconds = Seconds(0.0)  # Combustion reaction time delay (Ecr).
        self.etd: Seconds = Seconds(0.0)  # Turbine and exhaust delay (Etd).
        self.k3: PU = PU(0.0)  # Ratio of Fuel Adjustment (K3).
        self.k4: PU = PU(0.0)  # Gain of radiation shield (K4).
        self.k5: PU = PU(0.0)  # Gain of radiation shield (K5).
        self.k6: PU = PU(0.0)  # Minimum fuel flow (K6).
        self.kf: PU = PU(0.0)  # Fuel system feedback (Kf).
        self.mwbase: ActivePower = ActivePower(0.1)  # Base for power values (MWbase) (> 0).  Unit = MW.
        self.t: Seconds = Seconds(0.0)  # Fuel Control Time Constant (T).
        self.t3: Seconds = Seconds(0.0)  # Radiation shield time constant (T3).
        self.t4: Seconds = Seconds(0.0)  # Thermocouple time constant (T4).
        self.t5: Seconds = Seconds(0.0)  # Temperature control time constant (T5).
        # Temperature control (Tc).  Unit = degF or degC depending on constants Af1 and Bf1.
        self.tc: Temperature = Temperature(0.0)
        self.tcd: Seconds = Seconds(0.0)  # Compressor discharge time constant (Tcd).
        self.tf: Seconds = Seconds(0.0)  # Fuel system time constant (Tf).
        self.tmax: PU = PU(0.0)  # Maximum Turbine limit (Tmax).
        self.tmin: PU = PU(0.0)  # Minimum Turbine limit (Tmin).
        # Rated temperature (Tr).  Unit = degC depending on parameters Af1 and Bf1.
        self.tr: Temperature = Temperature(0.0)
        self.trate: ActivePower = ActivePower(0.0)  # Turbine rating (Trate).  Unit = MW.
        self.tt: Seconds = Seconds(0.0)  # Temperature controller integration rate (Tt).
        self.w: PU = PU(0.0)  # Governor gain (1/droop) on turbine rating (W).
        self.x: Seconds = Seconds(0.0)  # Governor lead time constant (X).
        self.y: Seconds = Seconds(0.1)  # Governor lag time constant (Y) (>0).
        self.z: bool = False # Governor mode (Z).  True = Droop.  False = ISO.
