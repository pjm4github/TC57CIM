# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class Pss1(PowerSystemStabilizerDynamics):
    """
    Italian PSS - three input PSS (speed, frequency, power).
    """
    def __init__(self):
        super().__init__()
        self.kf: float = 5.0  # Frequency power input gain (K<sub>EF</sub>). Typical Value = 5.
        self.kpe: float = 0.3  # Electric power input gain (K<sub>EPE</sub>). Typical Value = 0.3.
        self.ks: float = 1.0  # PSS gain (K<sub>ES</sub>). Typical Value = 1.
        self.kw: float = 0.0  # Shaft speed power input gain (K<sub>EW</sub>). Typical Value = 0.
        self.pmin: PU = PU(0.25)  # Minimum power PSS enabling (P<sub>MIN</sub>). Typical Value = 0.25.
        self.t10: Seconds = Seconds(0)  # Lead/lag time constant (T<sub>10</sub>). Typical Value = 0.
        self.t5: Seconds = Seconds(3.5)  # Washout (T<sub>5</sub>). Typical Value = 3.5.
        self.t6: Seconds = Seconds(0.0)  # Filter time constant (T<sub>6</sub>). Typical Value = 0.
        self.t7: Seconds = Seconds(0.0)  # Lead/lag time constant (T<sub>7</sub>). Typical Value = 0.
        self.t8: Seconds = Seconds(0.0)  # Lead/lag time constant (T<sub>8</sub>). Typical Value = 0.
        self.t9: Seconds = Seconds(0.0)  # Lead/lag time constant (T<sub>9</sub>). Typical Value = 0.
        self.tpe: Seconds = Seconds(0.05)  # Electric power filter time constant (T<sub>EPE</sub>). Typical Value = 0.05.
        self.vadat: bool = True
        self.vsmn: PU = PU(-0.06)  # Stabilizer output max limit (V<sub>SMN</sub>). Typical Value = -0.06.
        self.vsmx: PU = PU(0.06)  # Stabilizer output min limit (V<sub>SMX</sub>). Typical Value = 0.06.
