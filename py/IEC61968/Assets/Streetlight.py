from IEC61968.Assets.Asset import Asset
from IEC61968.InfIEC61968.InfAssets.StreetlightLampKind import StreetlightLampKind
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Length import Length


class Streetlight(Asset):
    """
    Streetlight asset.
    @created 07-Jan-2024 9:48:50 PM
    """
    def __init__(self):
        super().__init__()
        self.arm_length = Length()  # Length of arm. Note that a new light may be placed on an existing ar
        self.lamp_kind = StreetlightLampKind.METAL_HALIDE  # Lamp kind
        self.light_rating = ActivePower()  # Power rating of light
