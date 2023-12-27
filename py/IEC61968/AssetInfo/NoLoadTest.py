# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.AssetInfo.TransformerEndInfo import TransformerEndInfo
from IEC61968.AssetInfo.TransformerTest import TransformerTest
from IEC61970.Base.Domain.KiloActivePower import KiloActivePower
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Domain.Voltage import Voltage


class NoLoadTest(TransformerTest):

    def __init__(self):
        super().__init__()
        self.energised_end_voltage = Voltage()
        self.exciting_current = PerCent()
        self.exciting_current_zero = PerCent()
        self.loss = KiloActivePower()
        self.loss_zero = KiloActivePower()
        self.energised_end = TransformerEndInfo()
