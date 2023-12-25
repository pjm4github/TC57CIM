# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.PhaseCode import PhaseCode
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TransformerEnd import TransformerEnd
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TransformerTank import TransformerTank


class TransformerTankEnd(TransformerEnd):
    """
    Transformer tank end represents an individual winding for unbalanced models or
    for transformer tanks connected into a bank (and bank is modelled with the
    PowerTransformer).
    @author pmora
    @version 1.0
    @created 15-Dec-2023 4:38:30 PM
    """
    def __init__(self):
        super().__init__()
        self.phases: PhaseCode = PhaseCode()
        self.transformer_tank: TransformerTank = TransformerTank()

    def get_phases(self) -> PhaseCode:
        return self.phases

    def get_transformer_tank(self) -> TransformerTank:
        return self.transformer_tank

    def set_phases(self, new_val: PhaseCode) -> None:
        self.phases = new_val

    def set_transformer_tank(self, new_val: TransformerTank) -> None:
        self.transformer_tank = new_val
