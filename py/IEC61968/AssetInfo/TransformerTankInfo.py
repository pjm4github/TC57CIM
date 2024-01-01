from IEC61968.AssetInfo.PowerTransformerInfo import PowerTransformerInfo
from IEC61968.AssetInfo.TransformerEndInfo import TransformerEndInfo
from IEC61968.Assets.AssetInfo import AssetInfo


class TransformerTankInfo(AssetInfo):
    def __init__(self):
        # Data for all the ends described by this transformer tank data.
        super().__init__()
        self.transformer_end_infos = [TransformerEndInfo()]

        # Power transformer data that this tank description is part of.
        self.power_transformer_info = PowerTransformerInfo()
