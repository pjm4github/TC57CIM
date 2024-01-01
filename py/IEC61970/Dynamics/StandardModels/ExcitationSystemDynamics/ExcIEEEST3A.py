# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from datetime import datetime
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
        self.ka: Optional[PU] = PU()
        self.kc: Optional[PU] = PU()
        self.kg: Optional[PU] = PU()
        self.ki: Optional[PU] = PU()
        self.km: Optional[PU] = PU()
        self.kp: Optional[PU] = PU()
        self.ta: Optional[Seconds] = Seconds()
        self.tb: Optional[Seconds] = Seconds()
        self.tc: Optional[Seconds] = Seconds()
        self.thetap: Optional[AngleDegrees] = AngleDegrees()
        self.tm: Optional[Seconds] = Seconds()
        self.vbmax: Optional[PU] = PU()
        self.vgmax: Optional[PU] = PU()
        self.vimax: Optional[PU] = PU()
        self.vimin: Optional[PU] = PU()
        self.vmmax: Optional[PU] = PU()
        self.vmmin: Optional[PU] = PU()
        self.vrmax: Optional[PU] = PU()
        self.vrmin: Optional[PU] = PU()
        self.xl: Optional[PU] = PU()
