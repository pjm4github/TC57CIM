# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TransformerEnd import TransformerEnd


class TransformerMeshImpedance:
    """
    Transformer mesh impedance (Delta-model) between transformer ends.
    The typical case is that this class describes the impedance between two
    transformer ends pair-wise, i.e. the cardinalities at both tranformer end
    associations are 1. But in cases where two or more transformer ends are modeled
    the cardinalities are larger than 1.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:42 PM
    """

    def __init__(self):
        self.r: Resistance =  Resistance()  # Resistance between the 'from' and the 'to' end, seen from the 'from' end.
        self.r0: Resistance = Resistance()  # Zero-sequence resistance between the 'from' and the 'to' end, seen from the 'from' end.
        self.x: Reactance = Reactance()  # Reactance between the 'from' and the 'to' end, seen from the 'from' end.
        self.x0: Reactance = Reactance()   # Zero-sequence reactance between the 'from' and the 'to' end, seen from the 'from' end.
        self.to_transformer_end: TransformerEnd = TransformerEnd()  # All transformer ends this mesh impedance is connected to.
        self.from_transformer_end: TransformerEnd = TransformerEnd()  # From end this mesh impedance is connected to. It determines the voltage reference.

    def get_from_transformer_end(self) -> TransformerEnd:
        return self.from_transformer_end

    def get_r(self) -> Resistance:
        return self.r

    def get_r0(self) -> Resistance:
        return self.r0

    def get_to_transformer_end(self) -> TransformerEnd:
        return self.to_transformer_end

    def get_x(self) -> Reactance:
        return self.x

    def get_x0(self) -> Reactance:
        return self.x0

    def set_from_transformer_end(self, new_val: TransformerEnd) -> None:
        self.from_transformer_end = new_val

    def set_r(self, new_val: Resistance) -> None:
        self.r = new_val

    def set_r0(self, new_val: Resistance) -> None:
        self.r0 = new_val

    def set_to_transformer_end(self, new_val: TransformerEnd) -> None:
        self.to_transformer_end = new_val

    def set_x(self, new_val: Reactance) -> None:
        self.x = new_val

    def set_x0(self, new_val: Reactance) -> None:
        self.x0 = new_val