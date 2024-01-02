# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from typing import Optional, Any

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.Temperature import Temperature
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGast3(TurbineGovernorDynamics):
    """
    Generic turbogas with acceleration and temperature controller.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.bca: float = 0.01  # Acceleration limit set-point (Bca).  Unit = 1/s.  Typical Value = 0.01.
        self.bp: PU = PU(0.05)   # Droop (bp).  Typical Value = 0.05.

        # Exhaust temperature variation due to fuel flow increasing from 0 to 1 PU (deltaTc).  Typical Value = 390.
        self.dtc: Optional[Temperature] = Temperature(390)
        self.ka: PU = PU(0.23)     # Minimum fuel flow (Ka).  Typical Value = 0.23.
        self.kac: float = 0.0  # Fuel system feedback (K_AC).  Typical Value = 0.
        self.kca: float = 100.0  # Acceleration control integral gain (Kca). Unit = 1/s.  Typical Value = 100.
        self.ksi: float = 0.0  # Gain of radiation shield (Ksi).  Typical Value = 0.8.
        self.ky: float = 1.0   # Coefficient of transfer function of fuel valve positioner (Ky).  Typical Value = 1.
        self.mnef: PU = PU(-.05)    # Fuel flow maximum negative error value (MN_EF).  Typical Value = -0.05.
        self.mxef: PU = PU(.05)    # Fuel flow maximum positive error value (MX_EF).  Typical Value = 0.05.
        self.rcmn: PU = PU(-.1)    # Minimum fuel flow (RCMN).  Typical Value = -0.1.
        self.rcmx: PU = PU(1)    # Maximum fuel flow (RCMX).  Typical Value = 1.
        self.tac: Seconds = Seconds(.1)  # Fuel control time constant (Tac).  Typical Value = 0.1.
        self.tc: Seconds = Seconds(.2)   # Compressor discharge volume time constant (Tc).  Typical Value = 0.2.
        self.td: Seconds = Seconds(3.3)   # Temperature controller derivative gain (Td).  Typical Value = 3.3.
        self.tfen: Optional[Temperature] = Temperature(540)  # Turbine rated exhaust temperature correspondent to Pm=1 PU (Tfen).  Typical Value = 540.
        self.tg: Seconds = Seconds(.05)    # Time constant of speed governor (Tg).  Typical Value = 0.05.
        self.tsi: Seconds = Seconds(25)   # Time constant of radiation shield (Tsi).  Typical Value = 15.
        self.tt: Optional[Temperature] = Temperature(250)  # Temperature controller integration rate (Tt).  Typical Value = 250.
        self.ttc: Seconds = Seconds(2.5)   # Time constant of thermocouple (Ttc).  Typical Value = 2.5.
        self.ty: Seconds = Seconds(0.2)    # Time constant of fuel valve positioner (Ty).  Typical Value = 0.2
