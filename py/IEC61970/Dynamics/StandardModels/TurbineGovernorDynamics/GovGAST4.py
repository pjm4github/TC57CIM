# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from typing import ClassVar

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGast4(TurbineGovernorDynamics):
    """
    Generic turbogas.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """
    def __init__(self):
        super().__init__()
        self.bp = PU(.05)  # Droop (bp).  Typical Value = 0.05.
        self.ktm = PU(0)  # Compressor gain (K<sub>tm</sub>).  Typical Value = 0.
        self.mnef = PU(-.05)  # Fuel flow maximum negative error value (MN<sub>EF</sub>).  Typical Value = -0.05.
        self.mxef = PU(.05)  # Fuel flow maximum positive error value (MX<sub>EF</sub>).  Typical Value = 0.05.
        self.rymn = PU(0)  # Minimum valve opening (RYMN).  Typical Value = 0.
        self.rymx = PU(1.1)  # Maximum valve opening (RYMX).  Typical Value = 1.1.
        self.ta = Seconds(3)  # Maximum gate opening velocity (T<sub>A</sub>).  Typical Value = 3.
        self.tc = Seconds(0.5)  # Maximum gate closing velocity (T<sub>c</sub>).  Typical Value = 0.5.
        self.tcm = Seconds(0.1)  # Fuel control time constant (T<sub>cm</sub>).  Typical Value = 0.1.
        self.tm = Seconds(0.2)  # Compressor discharge volume time constant (T<sub>m</sub>).  Typical Value = 0.2.
        self.tv = Seconds(0.1)  # Time constant of fuel valve positioner (T<sub>y</sub>).  Typical Value = 0.1.
