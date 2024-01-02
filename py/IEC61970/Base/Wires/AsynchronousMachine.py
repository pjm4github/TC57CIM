from typing import Optional
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.RotationSpeed import RotationSpeed
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Resistance import Resistance
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.Reactance import Reactance

from IEC61970.Base.Wires.AsynchronousMachineKind import AsynchronousMachineKind
from IEC61970.Base.Wires.RotatingMachine import RotatingMachine


class AsynchronousMachine(RotatingMachine):
    """
    A rotating machine whose shaft rotates asynchronously with the electrical field.
    Also known as an induction machine with no external connection to the rotor
    windings, e.g squirrel-cage induction machine.
    """
    def __init__(self) -> None:
        super().__init__()
        self.asynchronousMachineTypeOptional[AsynchronousMachineKind] = AsynchronousMachineKind.MOTOR  # Type of Asynchronous Machine (motor or generator)
        self.converterFedDrivebool = False  # Indicates if the machine is a converter fed drive
        self.efficiencyOptional[PerCent] = PerCent()  # Efficiency of the asynchronous machine at nominal operation in percent
        self.iaIrRatiofloat = 1.0  # Ratio of locked-rotor current to the rated current of the motor (Ia/Ir)
        self.nominalFrequencyOptional[Frequency] = Frequency()  # Nameplate data indicates if the machine is 50 or 60 Hz
        self.nominalSpeedOptional[RotationSpeed] = RotationSpeed()  # Nameplate data (depends on the slip and number of pole pairs)
        self.polePairNumberOptional[int] = 0  # Number of pole pairs of stator
        self.ratedMechanicalPowerOptional[ActivePower] = ActivePower()  # Rated mechanical power (Pr in the IEC 60909-0)
        self.reversiblebool = True  # Indicates if the power can be reversible (for converter drive motors)
        self.rr1Optional[Resistance] = Resistance()  # Damper 1 winding resistance
        self.rr2Optional[Resistance] = Resistance()  # Damper 2 winding resistance
        self.rxLockedRotorRatiofloat = 1.0  # Locked rotor ratio (R/X)
        self.tpoSeconds = Seconds()  # Transient rotor time constant (greater than tppo)
        self.tppoSeconds = Seconds()  # Sub-transient rotor time constant (greater than 0)
        self.xlr1Optional[Reactance] = Reactance()  # Damper 1 winding leakage reactance
        self.xlr2Optional[Reactance] = Reactance()  # Damper 2 winding leakage reactance
        self.xmOptional[Reactance] = Reactance()  # Magnetizing reactance
        self.xpOptional[Reactance] = Reactance()  # Transient reactance (unsaturated) (greater than or equal to xpp)
        self.xppOptional[Reactance] = Reactance()  # Sub-transient reactance (unsaturated) (greater than Xl)
        self.xsOptional[Reactance] = Reactance()  # Synchronous reactance (greater than xp)

    def get_asynchronousMachineType(self) -> Optional[AsynchronousMachineKind]:
        return self.asynchronousMachineType

    def get_converterFedDrive(self) -> bool:
        return self.converterFedDrive

    def get_efficiency(self) -> Optional[PerCent]:
        return self.efficiency

    def get_iaIrRatio(self) -> float:
        return self.iaIrRatio

    def get_nominalFrequency(self) -> Optional[Frequency]:
        return self.nominalFrequency

    def get_nominalSpeed(self) -> Optional[RotationSpeed]:
        return self.nominalSpeed

    def get_polePairNumber(self) -> Optional[int]:
        return self.polePairNumber

    def get_ratedMechanicalPower(self) -> Optional[ActivePower]:
        return self.ratedMechanicalPower

    def get_reversible(self) -> bool:
        return self.reversible

    def get_rr1(self) -> Optional[Resistance]:
        return self.rr1

    def get_rr2(self) -> Optional[Resistance]:
        return self.rr2

    def get_rxLockedRotorRatio(self) -> float:
        return self.rxLockedRotorRatio

    def get_tpo(self) -> Seconds:
        return self.tpo

    def get_tppo(self) -> Seconds:
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

    def set_asynchronousMachineType(self, new_valOptional[AsynchronousMachineKind]) -> None:
        self.asynchronousMachineType = new_val

    def set_converterFedDrive(self, new_valbool) -> None:
        self.converterFedDrive = new_val

    def set_efficiency(self, new_valOptional[PerCent]) -> None:
        self.efficiency = new_val

    def set_iaIrRatio(self, new_valfloat) -> None:
        self.iaIrRatio = new_val

    def set_nominalFrequency(self, new_valOptional[Frequency]) -> None:
        self.nominalFrequency = new_val

    def set_nominalSpeed(self, new_valOptional[RotationSpeed]) -> None:
        self.nominalSpeed = new_val

    def set_polePairNumber(self, new_valOptional[int]) -> None:
        self.polePairNumber = new_val

    def set_ratedMechanicalPower(self, new_valOptional[ActivePower]) -> None:
        self.ratedMechanicalPower = new_val

    def set_reversible(self, new_valbool) -> None:
        self.reversible = new_val

    def set_rr1(self, new_valOptional[Resistance]) -> None:
        self.rr1 = new_val

    def set_rr2(self, new_valOptional[Resistance]) -> None:
        self.rr2 = new_val

    def set_rxLockedRotorRatio(self, new_valfloat) -> None:
        self.rxLockedRotorRatio = new_val

    def set_tpo(self, new_valSeconds) -> None:
        self.tpo = new_val

    def set_tppo(self, new_valSeconds) -> None:
        self.tppo = new_val

    def set_xlr1(self, new_valOptional[Reactance]) -> None:
        self.xlr1 = new_val

    def set_xlr2(self, new_valOptional[Reactance]) -> None:
        self.xlr2 = new_val

    def set_xm(self, new_valOptional[Reactance]) -> None:
        self.xm = new_val

    def set_xp(self, new_valOptional[Reactance]) -> None:
        self.xp = new_val

    def set_xpp(self, new_valOptional[Reactance]) -> None:
        self.xpp = new_val

    def set_xs(self, new_valOptional[Reactance]) -> None:
        self.xs = new_val
