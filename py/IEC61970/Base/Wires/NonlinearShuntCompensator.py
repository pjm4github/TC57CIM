# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.NonlinearShuntCompensatorPoint import NonlinearShuntCompensatorPoint
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ShuntCompensator import ShuntCompensator


class NonlinearShuntCompensator(ShuntCompensator):

    def __init__(self) -> None:
        super().__init__()
        self.nonlinear_shunt_compensator_points = NonlinearShuntCompensatorPoint()

    def get_nonlinear_shunt_compensator_points(self) -> NonlinearShuntCompensatorPoint:
        return self.nonlinear_shunt_compensator_points

    def set_nonlinear_shunt_compensator_points(self, new_val: NonlinearShuntCompensatorPoint) -> None:
        self.nonlinear_shunt_compensator_points = new_val
