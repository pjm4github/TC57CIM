# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from IEC61968.Assets.CatalogAssetType import CatalogAssetType
from IEC61968.Assets.Procedure import Procedure
from IEC61968.InfIEC61968.InfWork.CUGroup import CUGroup
from IEC61968.InfIEC61968.InfWork.DesignLocationCU import DesignLocationCU
from IEC61968.InfIEC61968.InfWork.WorkDocument import WorkDocument
from IEC61970.Base.Domain.Money import Money


class CompatibleUnit(WorkDocument):
    """
    A pre-planned job model containing labor, material, and accounting requirements
    for standardized job planning.
    """

    def __init__(self) -> None:
        super().__init__()
        self.est_cost: Money = Money()  # Estimated total cost for performing CU
        self.quantity: str = ""  # The quantity, unit of measure, and multiplier at the CU level that applies to the
        # materials
        self.design_location_cus: DesignLocationCU = DesignLocationCU()
        self.cu_group: CUGroup = CUGroup()
        self.procedures: Procedure = Procedure()
        self.generic_asset_model: CatalogAssetType = CatalogAssetType()
