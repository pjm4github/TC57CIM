from IEC61968.Assets.Asset import Asset
from IEC61968.InfIEC61968.InfAssets.AnchorKind import AnchorKind
from IEC61968.InfIEC61968.InfAssets.StructureSupportKind import StructureSupportKind
from IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from IEC61970.Base.Domain.Length import Length


class StructureSupport(Asset):
    """
    Support for structure assets.
    @created 29-Dec-2023 5:32:15 PM
    """
    def __init__(self):
        super().__init__()
        self.anchor_kind = AnchorKind.ROD  # (if anchor) Kind of anchor
        self.anchor_rod_count = 0  # (if anchor) Number of rods used
        self.anchor_rod_length = Length()  # (if anchor) Length of rod used
        self.direction = AngleDegrees()  # Direction of this support structure
        self.kind = StructureSupportKind.ANCHOR  # Kind of structure support
        self.length = Length()  # Length of this support structure
        self.size = ""  # Size of this support structure
