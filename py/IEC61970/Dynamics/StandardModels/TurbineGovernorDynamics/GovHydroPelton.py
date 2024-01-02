# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from typing import Optional

from IEC61970.Base.Domain.Area import Area
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.Length import Length
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.VolumeFlowRate import VolumeFlowRate
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroPelton(TurbineGovernorDynamics):
    """
    Detailed hydro unit - Pelton model.  This model can be used to represent the dynamic related to water tunnel
    and surge chamber.
    A schematic of the hydraulic system of detailed hydro unit models, like Francis and Pelton, is located under
    the GovHydroFrancis class.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self):
        super().__init__()
        # Area of the surge tank (A_V0). Unit = m^2. Typical Value = 30.
        self.area_v0: Area = Area(1.0)

        # Area of the compensation tank (A_V1). Unit = m^2. Typical Value = 700.
        self.area_v1: Area = Area(1.0)

        # Droop (bp).  Typical Value = 0.05.
        self.bp: PU = PU(1.0)

        # Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0.
        self.db1: Frequency = Frequency(1.0)

        # Intentional dead-band width of valve opening error (DB2). Unit = Hz.  Typical Value = 0.01.
        self.db2: Frequency = Frequency(1.0)

        # Head of compensation chamber water level with respect to the level of penstock (H1).
        # Unit = m. Typical Value = 4.
        self.h1: Length = Length(1.0)

        # Head of surge tank water level with respect to the level of penstock (H2).  Unit = m. Typical Value = 40.
        self.h2: Length = Length(1.0)

        # Rated hydraulic head (H_n).  Unit = m. Typical Value = 250.
        self.hn: Length = Length(1.0)

        # Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025.
        self.kc: PU = PU(1.0)

        # Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical Value = -0.025.
        self.kg: PU = PU(1.0)

        # No-load turbine flow at nominal head (Qc0).  Typical Value = 0.05.
        self.qc0: PU = PU(1.0)

        # Rated flow (Q_n). Unit = m^3/s. Typical Value = 40.
        self.qn: VolumeFlowRate = VolumeFlowRate(1.0)

        # Simplified Pelton model simulation (Sflag).
        # true = enable of simplified Pelton model simulation
        # false = enable of complete Pelton model simulation (non linear gain).
        # Typical Value = false.
        self.simplified_pelton: bool  = False

        # Static compensating characteristic (Cflag).
        # true = enable of static compensating characteristic
        # false = inhibit of static compensating characteristic.
        # Typical Value = false.
        self.static_compensating: bool  = False

        # Derivative gain (accelerometer time constant) (Ta).  Typical Value = 3.
        self.ta: Seconds = Seconds(1.0)

        # Gate servo time constant (Ts).  Typical Value = 0.15.
        self.ts: Seconds = Seconds(1.0)

        # Servomotor integrator time constant (TV).  Typical Value = 0.3.
        self.tv: Seconds = Seconds(1.0)

        # Water inertia time constant (Twnc).  Typical Value = 1.
        self.twnc: Seconds = Seconds(1.0)

        # Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3.
        self.twng: Seconds = Seconds(1.0)

        # Electronic integrator time constant (Tx).  Typical Value = 0.5.
        self.tx: Seconds = Seconds(1.0)

        # Maximum gate opening velocity (Va). Unit = PU/sec.  Typical Value = 0.016.
        self.va: float = 1.0

        # Maximum gate opening (ValvMax).  Typical Value = 1.
        self.valvmax: PU = PU(1.0)

        # Minimum gate opening (ValvMin).  Typical Value = 0.
        self.valvmin: PU = PU(1.0)

        # Maximum servomotor valve opening velocity (Vav).  Typical Value = 0.017.
        self.vav: PU = PU(1.0)

        # Maximum gate closing velocity (Vc). Unit = PU/sec.  Typical Value = -0.016.
        self.vc: float = 1.0

        # Maximum servomotor valve closing velocity (Vcv).  Typical Value = -0.017.
        self.vcv: PU = PU(1.0)

        # Water tunnel and surge chamber simulation (Tflag).
        # true = enable of water tunnel and surge chamber simulation
        # false = inhibit of water tunnel and surge chamber simulation.
        # Typical Value = false.
        self.water_tunnel_surge_chamber_simulation: bool  = False

        # Head of upper water level with respect to the level of penstock (Zsfc).  Unit = m. Typical Value = 25.

        # type zsfc: float = 0.0
        self.zsfc: Length = Length(1.0)
