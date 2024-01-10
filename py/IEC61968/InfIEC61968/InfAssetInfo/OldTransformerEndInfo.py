# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from IEC61968.AssetInfo.TransformerEndInfo import TransformerEndInfo
from IEC61968.InfIEC61968.InfAssetInfo.WindingInsulationKind import WindingInsulationKind
from IEC61970.Base.Domain.ApparentPower import ApparentPower
from IEC61970.Base.Domain.Mass import Mass


class OldTransformerEndInfo(TransformerEndInfo):

    def __init__(self) -> None:
        super().__init__()
        """
        Overload rating for 24 hours.
        """
        self.day_overload_rating: ApparentPower = ApparentPower()

        """
        Overload rating for 1 hour.
        """
        self.hour_overload_rating: ApparentPower = ApparentPower()

        """
        Weight of solid insulation in transformer.
        """
        self.solid_insulation_weight: Mass = Mass()

        """
        Type of insulation used for transformer windings.
        """
        self.winding_insulation_kind: WindingInsulationKind = WindingInsulationKind.NOMEX
