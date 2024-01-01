# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.ReferenceData.RegisteredGenerator import RegisteredGenerator


class FuelRegion(IdentifiedObject):
    """
    Indication of region for fuel inventory purposes.
    @updated 28-Dec-2023 12:14:44 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.fuel_region_typeOptional[str] = ""
        self.last_modifiedOptional[DateTime] = DateTime()
        self.registered_generatorOptional[RegisteredGenerator] = RegisteredGenerator()
