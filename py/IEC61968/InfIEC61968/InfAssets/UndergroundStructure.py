# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from IEC61968.Assets.Structure import Structure
from IEC61968.InfIEC61968.InfAssets.UndergroundStructureKind import UndergroundStructureKind
from IEC61970.Base.Domain.Date import Date


class UndergroundStructure(Structure):
    """
    Underground structure.
    @created 29-Dec-2023 6:12:28 PM
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.has_ventilation = True  # True if vault is ventilating
        self.kind = UndergroundStructureKind.SUBSURFACE_ENCLOSURE
        self.material = ""  # Primary material of underground structure
        self.sealing_warranty_expires_date = Date() # Date sealing warranty expires
