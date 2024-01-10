# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local imports
from IEC61968.AssetMeas.AssetDiscrete import AssetDiscrete
from IEC61968.AssetMeas.OilAnalysisParticleDiscreteKind import OilAnalysisParticleDiscreteKind


class OilAnalysisParticleDiscrete(AssetDiscrete):

    def __init__(self):
        super().__init__()
        self.kind = OilAnalysisParticleDiscreteKind.OPACITY

