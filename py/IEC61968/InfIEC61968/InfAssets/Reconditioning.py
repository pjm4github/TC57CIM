# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from IEC61968.InfIEC61968.InfAssets.TransformerObservation import TransformerObservation
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime


class Reconditioning(IdentifiedObject):
    """
    Reconditioning information for an asset.
    @created 29-Dec-2023 6:11:55 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.date_time = DateTime()
        self.transformer_observations = TransformerObservation()
