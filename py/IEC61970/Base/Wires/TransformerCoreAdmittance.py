# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Conductance import Conductance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Susceptance import Susceptance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TransformerEnd import TransformerEnd


class TransformerCoreAdmittance:
    """
    The transformer core admittance. Used to specify the core admittance of a
    transformer in a manner that can be shared among power transformers.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:42 PM
    """

    def __init__(self) -> None:
        self.b: Susceptance = Susceptance()
        self.b0: Susceptance = Susceptance()
        self.g: Conductance = Conductance()
        self.g0: Conductance = Conductance()
        self.transformer_end: TransformerEnd = TransformerEnd()

    def get_b(self) -> Susceptance:
        return self.b

    def get_b0(self) -> Susceptance:
        return self.b0

    def get_g(self) -> Conductance:
        return self.g

    def get_g0(self) -> Conductance:
        return self.g0

    def get_transformer_end(self) -> TransformerEnd:
        return self.transformer_end

    def set_b(self, new_val: Susceptance) -> None:
        self.b = new_val

    def set_b0(self, new_val: Susceptance) -> None:
        self.b0 = new_val

    def set_g(self, new_val: Conductance) -> None:
        self.g = new_val

    def set_g0(self, new_val: Conductance) -> None:
        self.g0 = new_val

    def set_transformer_end(self, new_val: TransformerEnd) -> None:
        self.transformer_end = new_val
