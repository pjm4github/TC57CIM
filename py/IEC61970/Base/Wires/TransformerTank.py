# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PowerTransformer import PowerTransformer


class TransformerTank:
    """
    An assembly of two or more coupled windings that transform electrical power
    between voltage levels. These windings are bound on a common core and place in
    the same tank. Transformer tank can be used to model both single-phase and 3-
    phase transformers.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:42 PM
    """

    def __init__(self) -> None:
        """
        Constructor for TransformerTank class.
        """
        self.power_transformer: PowerTransformer = PowerTransformer()

    def get_power_transformer(self) -> PowerTransformer:
        return self.power_transformer

    def set_power_transformer(self, new_val: PowerTransformer) -> None:
        self.power_transformer = new_val
