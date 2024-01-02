# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023

from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from IEC62325.MarketOperations.ReferenceData.RegisteredGenerator import RegisteredGenerator
from IEC62325.MarketOperations.MktDomain.EnergyPriceIndexType import EnergyPriceIndexType


class EnergyPriceIndex(IdentifiedObject):
    """
    An Energy Price Index for each Resource is valid for a period (e.g. daily) that
    is identified by a Valid Period Start Time and a Valid Period End Time. An
    Energy Price Index is in $/MWh.
    @created 27-Dec-2023 3:27:44 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.energy_price_indexfloat = 0.0  # Energy price index
        self.energy_price_index_typeOptional[EnergyPriceIndexType] = EnergyPriceIndexType()  # EPI type such as wholesale or retail
        self.last_modifiedOptional[DateTime] = DateTime()  # Time updated
        self.valid_periodOptional[DateTimeInterval] = DateTimeInterval()  # Valid period for which the energy price index is valid.
        self.registered_generatorOptional[RegisteredGenerator] = RegisteredGenerator()
