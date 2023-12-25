# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.NonlinearShuntCompensatorPhasePoint import \
    NonlinearShuntCompensatorPhasePoint
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ShuntCompensatorPhase import ShuntCompensatorPhase


class NonlinearShuntCompensatorPhase(ShuntCompensatorPhase):
    """
    A per phase non-linear shunt compensator has bank or section admittance values
    that differs.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    """
    def __init__(self):
        super().__init__()
        self.nonlinear_shunt_compensator_phase_points = NonlinearShuntCompensatorPhasePoint()

    def get_nonlinear_shunt_compensator_phase_points(self) -> NonlinearShuntCompensatorPhasePoint:
        return self.nonlinear_shunt_compensator_phase_points

    def set_nonlinear_shunt_compensator_phase_points(self, new_val: NonlinearShuntCompensatorPhasePoint):
        self.nonlinear_shunt_compensator_phase_points = new_val
