# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Wires.WindingConnection import WindingConnection
from IEC61970.Base.Domain.ApparentPower import ApparentPower

from IEC61970.Base.Domain.Voltage import Voltage
from IEC61970.Base.Domain.Resistance import Resistance
from IEC61970.Base.Wires.TransformerCoreAdmittance import TransformerCoreAdmittance
from IEC61970.Base.Wires.TransformerMeshImpedance import TransformerMeshImpedance
from IEC61970.Base.Wires.TransformerStarImpedance import TransformerStarImpedance
from IEC61968.Assets.AssetInfo import AssetInfo


class TransformerEndInfo(AssetInfo):

    def __init__(self):
        super().__init__()
        self.connection_kind = WindingConnection.A
        self.emergency_s = ApparentPower()
        self.end_number = 0
        self.insulation_u = Voltage()
        self.phase_angle_clock = 0
        self.r = Resistance()
        self.rated_s = ApparentPower()
        self.rated_u = Voltage()
        self.short_term_s = ApparentPower()
        self.core_admittance = TransformerCoreAdmittance()
        self.from_mesh_impedances = TransformerMeshImpedance()
        self.transformer_star_impedance = TransformerStarImpedance()
        self.to_mesh_impedances = TransformerMeshImpedance()
