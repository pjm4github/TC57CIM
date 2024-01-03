# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from typing import Optional

from IEC61968.InfIEC61968.InfAssets.Specification import Specification
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.Length import Length


class DimensionsInfo(IdentifiedObject):
    """
    As applicable, the basic linear, area, or volume dimensions of an asset, asset
    type (AssetModel) or other type of object (such as land area). Units and
    multipliers are specified per dimension.
    @created 29-Dec-2023 6:11:33 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.orientation: Optional[str] = ""  # A description of the orientation of the object relative to the dimensions.
        self.size_depth: Optional[Length] = Length()  # Depth measurement
        self.size_diameter: Optional[Length] = Length()  # Diameter measurement
        self.size_length: Optional[Length] = Length()  # Length measurement
        self.size_width: Optional[Length] = Length()  # Width measurement
        self.specifications: Optional[Specification] = Specification()
