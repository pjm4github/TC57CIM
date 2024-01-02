# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from typing import Optional

from IEC61970.Base.Domain.Area import Area
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.Length import Length
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.VolumeFlowRate import VolumeFlowRate
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.FrancisGovernorControlKind import \
    FrancisGovernorControlKind
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroFrancis(TurbineGovernorDynamics):
    def __init__(self):
        super().__init__()
        self.am = PU(.7)  # Opening section S<sub>eff</sub> at the maximum efficiency (Am).  Typical Value = 0.7.
        self.av0 = Area(30)  # Area of the surge tank (A<sub>V0</sub>). Unit = m<sup>2</sup>. Typical Value = 30.
        self.av1 = Area(700)  # Area of the compensation tank (A<sub>V1</sub>). Unit = m<sup>2</sup>. Typical Value = 700.
        self.bp = PU(.05)  # Droop (Bp).  Typical Value = 0.05.
        self.db1 = Frequency(0)  # Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0.
        self.etamax = PU(1.05)  # Maximum efficiency (EtaMax).  Typical Value = 1.05.
        self.governor_control = FrancisGovernorControlKind.MECHANIC_HYDRAULIC_TRANSIENT_FEEDBACK  # Governor control flag (Cflag).  Typical Value = mechanicHydrolicTachoAccelerator.
        self.h1 = Length(4)  # Head of compensation chamber water level with respect to the level of penstock (H<sub>1</sub>).  Unit = m. Typical Value = 4.
        self.h2 = Length(40)  # Head of surge tank water level with respect to the level of penstock (H<sub>2</sub>).  Unit = m. Typical Value = 40.
        self.hn = Length(250)  # Rated hydraulic head (H<sub>n</sub>).  Unit = m. Typical Value = 250.
        self.kc = PU(0.025)  # Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025.
        self.kg = PU(0.025)  # Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical Value = 0.025.
        self.kt = PU(.25)  # Washout gain (Kt).  Typical Value = 0.25.
        self.qc0 = PU(.21)  # No-load turbine flow at nominal head (Qc0).  Typical Value = 0.21.
        self.qn = VolumeFlowRate(40)  # Rated flow (Q<sub>n</sub>). Unit = m<sup>3</sup>/s. Typical Value = 40.
        self.ta = Seconds(3)  # Derivative gain (Ta).  Typical Value = 3.
        self.td = Seconds(3)  # Washout time constant (Td).  Typical Value = 3.
        self.ts = Seconds(.5)  # Gate servo time constant (Ts).  Typical Value = 0.5.
        self.twnc = Seconds(1)  # Water inertia time constant (Twnc).  Typical Value = 1.
        self.twng = Seconds(3)  # Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3.
        self.tx = Seconds(1)  # Derivative feedback gain (Tx).  Typical Value = 1.
        self.va: float = 0.011  # Maximum gate opening velocity (Va). Unit = PU/sec. Typical Value = 0.011.
        self.valvmax = PU(1)  # Maximum gate opening (ValvMax).  Typical Value = 1.
        self.valvmin = PU(0)  # Minimum gate opening (ValvMin).  Typical Value = 0.
        self.vc: float = -0.011  # Maximum gate closing velocity (Vc). Unit = PU/sec. Typical Value = -0.011.
        self.water_tunnel_surge_chamber_simulation: bool  = False  # Water tunnel and surge chamber simulation (Tflag). True = enable of water tunnel and surge chamber simulation, False = inhibit of water tunnel and surge chamber simulation. Typical Value = False.
        self.zsfc = Length(25)  # Head of upper water level with respect to the level of penstock (Zsfc).  Unit = m.  Typical Value = 25.
