# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetInfo.TransformerEndInfo import TransformerEndInfo
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetInfo.TransformerTest import TransformerTest
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Impedance import Impedance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.KiloActivePower import KiloActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ApparentPower import ApparentPower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PerCent import PerCent


class ShortCircuitTest(TransformerTest):
    def __init__(self):
        super().__init__()
        self.current = CurrentFlow()  # Short circuit current
        self.energised_end_step = 0  # Tap step number for the energised end of the test pair
        self.grounded_end_step = 0  # Tap step number for the grounded end of the test pair
        self.leakage_impedance = Impedance()  # Leakage impedance measured from a positive-sequence or single-phase short-circuit test
        self.leakage_impedance_zero = Impedance()  # Leakage impedance measured from a zero-sequence short-circuit test
        self.loss = KiloActivePower()  # Load losses from a positive-sequence or single-phase short-circuit test
        self.loss_zero = KiloActivePower()  # Load losses from a zero-sequence short-circuit test
        self.power = ApparentPower()  # Short circuit apparent power
        self.voltage = PerCent()  # Short circuit voltage
        self.grounded_ends = TransformerEndInfo()  # All ends short-circuited in this short-circuit test
        self.energised_end = TransformerEndInfo()  # Transformer end that voltage is applied to in this short-circuit test. The test voltage is chosen to induce rated current in the energised end
