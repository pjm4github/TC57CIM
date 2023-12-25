from typing import Optional
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PerCent import PerCent
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Frequency import Frequency
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.RotationSpeed import RotationSpeed
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Seconds import Seconds
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.AsynchronousMachineKind import AsynchronousMachineKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RotatingMachine import RotatingMachine


class AsynchronousMachine(RotatingMachine):
    """
    A rotating machine whose shaft rotates asynchronously with the electrical field.
    Also known as an induction machine with no external connection to the rotor
    windings, e.g squirrel-cage induction machine.
    """
    def __init__(self) -> None:
        super().__init__()
        self.asynchronousMachineType: Optional[AsynchronousMachineKind] = AsynchronousMachineKind.MOTOR  # Type of Asynchronous Machine (motor or generator)
        self.converterFedDrive: Optional[bool] = False  # Indicates if the machine is a converter fed drive
        self.efficiency: Optional[PerCent] = PerCent()  # Efficiency of the asynchronous machine at nominal operation in percent
        self.iaIrRatio: Optional[float] = 1.0  # Ratio of locked-rotor current to the rated current of the motor (Ia/Ir)
        self.nominalFrequency: Optional[Frequency] = Frequency()  # Nameplate data indicates if the machine is 50 or 60 Hz
        self.nominalSpeed: Optional[RotationSpeed] = RotationSpeed()  # Nameplate data (depends on the slip and number of pole pairs)
        self.polePairNumber: Optional[int] = 0  # Number of pole pairs of stator
        self.ratedMechanicalPower: Optional[ActivePower] = ActivePower()  # Rated mechanical power (Pr in the IEC 60909-0)
        self.reversible: Optional[bool] = True  # Indicates if the power can be reversible (for converter drive motors)
        self.rr1: Optional[Resistance] = Resistance()  # Damper 1 winding resistance
        self.rr2: Optional[Resistance] = Resistance()  # Damper 2 winding resistance
        self.rxLockedRotorRatio: Optional[float] = 1.0  # Locked rotor ratio (R/X)
        self.tpo: Optional[Seconds] = Seconds()  # Transient rotor time constant (greater than tppo)
        self.tppo: Optional[Seconds] = Seconds()  # Sub-transient rotor time constant (greater than 0)
        self.xlr1: Optional[Reactance] = Reactance()  # Damper 1 winding leakage reactance
        self.xlr2: Optional[Reactance] = Reactance()  # Damper 2 winding leakage reactance
        self.xm: Optional[Reactance] = Reactance()  # Magnetizing reactance
        self.xp: Optional[Reactance] = Reactance()  # Transient reactance (unsaturated) (greater than or equal to xpp)
        self.xpp: Optional[Reactance] = Reactance()  # Sub-transient reactance (unsaturated) (greater than Xl)
        self.xs: Optional[Reactance] = Reactance()  # Synchronous reactance (greater than xp)

    def get_asynchronousMachineType(self) -> Optional[AsynchronousMachineKind]:
        return self.asynchronousMachineType

    def get_converterFedDrive(self) -> Optional[bool]:
        return self.converterFedDrive

    def get_efficiency(self) -> Optional[PerCent]:
        return self.efficiency

    def get_iaIrRatio(self) -> Optional[float]:
        return self.iaIrRatio

    def get_nominalFrequency(self) -> Optional[Frequency]:
        return self.nominalFrequency

    def get_nominalSpeed(self) -> Optional[RotationSpeed]:
        return self.nominalSpeed

    def get_polePairNumber(self) -> Optional[int]:
        return self.polePairNumber

    def get_ratedMechanicalPower(self) -> Optional[ActivePower]:
        return self.ratedMechanicalPower

    def get_reversible(self) -> Optional[bool]:
        return self.reversible

    def get_rr1(self) -> Optional[Resistance]:
        return self.rr1

    def get_rr2(self) -> Optional[Resistance]:
        return self.rr2

    def get_rxLockedRotorRatio(self) -> Optional[float]:
        return self.rxLockedRotorRatio

    def get_tpo(self) -> Optional[Seconds]:
        return self.tpo

    def get_tppo(self) -> Optional[Seconds]:
        return self.tppo

    def get_xlr1(self) -> Optional[Reactance]:
        return self.xlr1

    def get_xlr2(self) -> Optional[Reactance]:
        return self.xlr2

    def get_xm(self) -> Optional[Reactance]:
        return self.xm

    def get_xp(self) -> Optional[Reactance]:
        return self.xp

    def get_xpp(self) -> Optional[Reactance]:
        return self.xpp

    def get_xs(self) -> Optional[Reactance]:
        return self.xs

    def set_asynchronousMachineType(self, new_val: Optional[AsynchronousMachineKind]) -> None:
        self.asynchronousMachineType = new_val

    def set_converterFedDrive(self, new_val: Optional[bool]) -> None:
        self.converterFedDrive = new_val

    def set_efficiency(self, new_val: Optional[PerCent]) -> None:
        self.efficiency = new_val

    def set_iaIrRatio(self, new_val: Optional[float]) -> None:
        self.iaIrRatio = new_val

    def set_nominalFrequency(self, new_val: Optional[Frequency]) -> None:
        self.nominalFrequency = new_val

    def set_nominalSpeed(self, new_val: Optional[RotationSpeed]) -> None:
        self.nominalSpeed = new_val

    def set_polePairNumber(self, new_val: Optional[int]) -> None:
        self.polePairNumber = new_val

    def set_ratedMechanicalPower(self, new_val: Optional[ActivePower]) -> None:
        self.ratedMechanicalPower = new_val

    def set_reversible(self, new_val: Optional[bool]) -> None:
        self.reversible = new_val

    def set_rr1(self, new_val: Optional[Resistance]) -> None:
        self.rr1 = new_val

    def set_rr2(self, new_val: Optional[Resistance]) -> None:
        self.rr2 = new_val

    def set_rxLockedRotorRatio(self, new_val: Optional[float]) -> None:
        self.rxLockedRotorRatio = new_val

    def set_tpo(self, new_val: Optional[Seconds]) -> None:
        self.tpo = new_val

    def set_tppo(self, new_val: Optional[Seconds]) -> None:
        self.tppo = new_val

    def set_xlr1(self, new_val: Optional[Reactance]) -> None:
        self.xlr1 = new_val

    def set_xlr2(self, new_val: Optional[Reactance]) -> None:
        self.xlr2 = new_val

    def set_xm(self, new_val: Optional[Reactance]) -> None:
        self.xm = new_val

    def set_xp(self, new_val: Optional[Reactance]) -> None:
        self.xp = new_val

    def set_xpp(self, new_val: Optional[Reactance]) -> None:
        self.xpp = new_val

    def set_xs(self, new_val: Optional[Reactance]) -> None:
        self.xs = new_val
