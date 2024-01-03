from IEC61968.Assets.Asset import Asset
from IEC61968.Assets.MediumKind import MediumKind
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.Volume import Volume


class Medium(IdentifiedObject):
    """
    # A substance that either (1) provides the means of transmission of a force or
    # effect, such as hydraulic fluid, or (2) is used for a surrounding or enveloping
    # substance, such as oil in a transformer or circuit breaker.
    # @created 29-Dec-2023 5:28:56 PM
    """
    def __init__(self):
        super().__init__()
        self.kind = MediumKind.AIR  # Kind of this medium
        self.volume_spec = Volume()  # The volume of the medium specified for this application
        self.asset = Asset()
