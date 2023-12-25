# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ConductancePerLength import ConductancePerLength
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactancePerLength import ReactancePerLength
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ResistancePerLength import ResistancePerLength
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.SusceptancePerLength import SusceptancePerLength
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SinglePhaseKind import SinglePhaseKind


# from susceptibility_per_length import SusceptancePerLength
# from single_phase_kind import SinglePhaseKind
# from conductance_per_length import ConductancePerLength
# from resistance_per_length import ResistancePerLength
# from reactance_per_length import ReactancePerLength

class PhaseImpedanceData:
        
    def __init__(self) -> None:
        self.b: SusceptancePerLength = SusceptancePerLength()
        self.from_phase: SinglePhaseKind = SinglePhaseKind.A
        self.g: ConductancePerLength = ConductancePerLength()
        self.r: ResistancePerLength = ResistancePerLength()
        self.to_phase: SinglePhaseKind = SinglePhaseKind.A
        self.x: ReactancePerLength = ReactancePerLength()
    
    def get_b(self) -> SusceptancePerLength:
        return self.b
        
    def get_from_phase(self) -> SinglePhaseKind:
        return self.from_phase
    
    def get_g(self) -> ConductancePerLength:
        return self.g
    
    def get_r(self) -> ResistancePerLength:
        return self.r
    
    def get_to_phase(self) -> SinglePhaseKind:
        return self.to_phase
    
    def get_x(self) -> ReactancePerLength:
        return self.x
    
    def set_b(self, new_val: SusceptancePerLength) -> None:
        self.b = new_val
    
    def set_from_phase(self, new_val: SinglePhaseKind) -> None:
        self.from_phase = new_val
    
    def set_g(self, new_val: ConductancePerLength) -> None:
        self.g = new_val
    
    def set_r(self, new_val: ResistancePerLength) -> None:
        self.r = new_val
    
    def set_to_phase(self, new_val: SinglePhaseKind) -> None:
        self.to_phase = new_val
    
    def set_x(self, new_val: ReactancePerLength) -> None:
        self.x = new_val
