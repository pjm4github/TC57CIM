# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PerCent import PerCent


class TapChangerTablePoint:
    """
    The magnetizing branch susceptance deviation in percent of nominal value. The actual susceptance is calculated as follows:
    calculated magnetizing susceptance = b(nominal) * (1 + b(from this class)/100). The b(nominal) is defined as the static magnetizing susceptance on the associated power transformer end or ends.  This model assumes the star impedance (pi model) form.
    """
    def __init__(self) -> None:
        self.b: Optional[PerCent] = PerCent()  # The magnetizing branch susceptance deviation in percent of nominal value
        self.g: Optional[PerCent] = PerCent()  # The magnetizing branch conductance deviation in percent of nominal value
        self.r: Optional[PerCent] = PerCent()  # The resistance deviation in percent of nominal value
        self.ratio: Optional[float] = 1.0  # The voltage at the tap step divided by rated voltage of the transformer end
        self.step: Optional[int] = 1  # The tap step
        self.x: Optional[PerCent] = PerCent()  # The series reactance deviation in percent of nominal value

    def get_b(self) -> Optional[float]:  # public PerCent getb()
        return self.b

    def set_b(self, new_val: Optional[float]) -> None:  # public void setb(PerCent newVal)
        self.b = new_val

    """
    The magnetizing branch conductance deviation in percent of nominal value. The actual conductance is calculated as follows:
    calculated magnetizing conductance = g(nominal) * (1 + g(from this class)/100). The g(nominal) is defined as the static magnetizing conductance on the associated power transformer end or ends.  This model assumes the star impedance (pi model) form.
    """
    def get_g(self) -> Optional[float]:  # public PerCent getg()
        return self.g

    def set_g(self, new_val: Optional[float]) -> None:  # public void setg(PerCent newVal)
        self.g = new_val

    """
    The resistance deviation in percent of nominal value. The actual reactance is calculated as follows:
    calculated resistance = r(nominal) * (1 + r(from this class)/100).  The r(nominal) is defined as the static resistance on the associated power transformer end or ends.  This model assumes the star impedance (pi model) form.
    """
    def get_r(self) -> Optional[float]:  # public PerCent getr()
        return self.r

    def set_r(self, new_val: Optional[float]) -> None:  # public void setr(PerCent newVal)
        self.r = new_val

    """
    The voltage at the tap step divided by rated voltage of the transformer end having the tap changer. Hence this is a value close to one.
    For example, if the ratio at step 1 is 1.01, and the rated voltage of the transformer end is 110kV, then the voltage obtained by setting the tap changer to step 1 to is 111.1kV.
    """
    def get_ratio(self) -> Optional[float]:  # public float getratio()
        return self.ratio

    def set_ratio(self, new_val: Optional[float]) -> None:  # public void setratio(float newVal)
        self.ratio = new_val

    """
    The tap step.
    """
    def get_step(self) -> Optional[int]:  # public int getstep()
        return self.step

    def set_step(self, new_val: Optional[int]) -> None:  # public void setstep(int newVal)
        self.step = new_val

    """
    The series reactance deviation in percent of nominal value. The actual reactance is calculated as follows:
    calculated reactance = x(nominal) * (1 + x(from this class)/100).  The x(nominal) is defined as the static series reactance on the associated power transformer end or ends.  This model assumes the star impedance (pi model) form.
    """
    def get_x(self) -> Optional[float]:  # public PerCent getx()
        return self.x

    def set_x(self, new_val: Optional[float]) -> None:  # public void setx(PerCent newVal)
        self.x = new_val
