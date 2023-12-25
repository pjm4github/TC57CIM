# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance


class TransformerStarImpedance:
    """
    Transformer star impedance (Pi-model) that accurately reflects impedance for
    transformers with 2 or 3 windings. For transformers with 4 or more windings,
    you must use TransformerMeshImpedance class.
    For transmission networks use PowerTransformerEnd impedances (r, r0, x, x0, b,
    b0, g and g0).
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:42 PM
    """
    def __init__(self):
        """
        Initialize transformer star impedance
        """
        self.r: Resistance = Resistance()
        self.r0: Resistance = Resistance()
        self.x: Reactance = Reactance()
        self.x0: Reactance = Reactance()

    def get_r(self) -> Resistance:
        """
        Get resistance of the transformer end
        """
        return self.r

    def get_r0(self) -> Resistance:
        """
        Get zero sequence series resistance of the transformer end
        """
        return self.r0

    def get_x(self) -> Reactance:
        """
        Get positive sequence series reactance of the transformer end
        """
        return self.x

    def get_x0(self) -> Reactance:
        """
        Get zero sequence series reactance of the transformer end
        """
        return self.x0

    def set_r(self, new_val: Resistance) -> None:
        """
        Set resistance value for the transformer end
        """
        self.r = new_val

    def set_r0(self, new_val: Resistance) -> None:
        """
        Set zero sequence series resistance value for the transformer end
        """
        self.r0 = new_val

    def set_x(self, new_val: Reactance) -> None:
        """
        Set positive sequence series reactance value for the transformer end
        """
        self.x = new_val

    def set_x0(self, new_val: Reactance) -> None:
        """
        Set zero sequence series reactance value for the transformer end
        """
        self.x0 = new_val
