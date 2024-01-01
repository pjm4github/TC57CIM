# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from IEC61968.AssetInfo.TransformerTankInfo import TransformerTankInfo
from IEC61968.InfIEC61968.InfAssetInfo.OilPreservationKind import OilPreservationKind
from IEC61968.InfIEC61968.InfAssetInfo.TransformerConstructionKind import TransformerConstructionKind
from IEC61968.InfIEC61968.InfAssetInfo.TransformerCoreKind import TransformerCoreKind
from IEC61968.InfIEC61968.InfAssetInfo.TransformerFunctionKind import TransformerFunctionKind
from IEC61970.Base.Domain.Mass import Mass
from IEC61970.Base.Domain.Voltage import Voltage


class OldTransformerTankInfo(TransformerTankInfo):

    def __init__(self) -> None:
        """
        Kind of construction for this transformer.
        """
        super().__init__()
        self.construction_kind: TransformerConstructionKind = TransformerConstructionKind()

        """
        Weight of core and coils in transformer.
        """
        self.core_coils_weight: Mass = Mass()

        """
        Core kind of this transformer product.
        """
        self.core_kind: TransformerCoreKind = TransformerCoreKind.core

        """
        Function of this transformer.
        """
        self.function: TransformerFunctionKind = TransformerFunctionKind.power_transformer

        """
        Basic insulation level of neutral.
        """
        self.neutral_bil: Voltage = Voltage()

        """
        Kind of oil preservation system.
        """
        self.oil_preservation_kind: OilPreservationKind = OilPreservationKind.FREE_BREATHING

