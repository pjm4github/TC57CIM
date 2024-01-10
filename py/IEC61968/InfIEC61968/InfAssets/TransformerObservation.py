# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfAssets.WindingInsulation import WindingInsulation
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.Temperature import Temperature
from IEC61970.Base.Domain.Voltage import Voltage
from IEC61970.Base.Wires.TransformerTank import TransformerTank


class TransformerObservation(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.bushing_temp = Temperature()  # Bushing temperature
        self.dga = ""  # Dissolved Gas Analysis
        self.freq_resp = ""  # Frequency Response Analysis
        self.furfural_dp = ""  # Overall measure of furfural in oil and mechanical strength of paper
        self.hot_spot_temp = Temperature()  # Hotspot oil temperature
        self.oil_color = ""  # Oil Quality Analysis-Color
        self.oil_dielectric_strength = Voltage()  # Oil Quality Analysis-Dielectric Strength
        self.oil_ift = ""  # Oil Quality Analysis, interfacial tension (IFT) - number-Dynes/CM
        self.oil_level = ""  # The level of oil in the transformer
        self.oil_neutralization_number = ""  # Oil Quality Analysis-Neutralization Number - Number - Mg KOH
        self.pump_vibration = ""  # Pump vibration
        self.status = Status()
        self.top_oil_temp = Temperature()  # Top oil temperature
        self.water_content = ""  # Water Content expressed in parts per million
        self.winding_insulation_pfs = WindingInsulation()
        self.transformer = TransformerTank()
