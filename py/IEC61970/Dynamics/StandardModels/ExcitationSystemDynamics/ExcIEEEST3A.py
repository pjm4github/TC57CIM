# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST3A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST3A model.  Some static systems
    utilize a field voltage control loop to linearize the exciter control characteristic.
    This also makes the output independent of supply source variations until supply
    limitations are reached.  These systems utilize a variety of controlled-rectifier
    designs: full thyristor complements or hybrid bridges in either series or shunt
    configurations. The power source may consist of only a potential source, either
    fed from the machine terminals or from internal windings. Some designs may have
    compound power sources utilizing both machine potential and current. These power
    sources are represented as phasor combinations of machine terminal current and
    voltage and are accommodated by suitable parameters in model Type ST3A which is
    represented by ExcIEEEST3A.

    Reference: IEEE Standard 421.5-2005 Section 7.3.
    @author: pcha006
    @version: 1.0
    @created: 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.ka: PU = PU()
        self.kc: PU = PU()
        self.kg: PU = PU()
        self.ki: PU = PU()
        self.km: PU = PU()
        self.kp: PU = PU()
        self.ta: Seconds = Seconds()
        self.tb: Seconds = Seconds()
        self.tc: Seconds = Seconds()
        self.thetap: Optional[AngleDegrees] = AngleDegrees()
        self.tm: Seconds = Seconds()
        self.vbmax: PU = PU()
        self.vgmax: PU = PU()
        self.vimax: PU = PU()
        self.vimin: PU = PU()
        self.vmmax: PU = PU()
        self.vmmin: PU = PU()
        self.vrmax: PU = PU()
        self.vrmin: PU = PU()
        self.xl: PU = PU()
