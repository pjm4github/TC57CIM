# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:12:35 2023

from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.InfIEC62325.InfFinancial.TransmissionProvider import TransmissionProvider


class TransmissionProduct(IdentifiedObject):
    """
    Type of the transmission product. This could be a transmission service class
    (firm, total transmission capability, or non-firm), transmission service period
    (on-peak, full-period, off-peak), transmission service increments (yearly
    extended, hourly fixed, monthly sliding, etc.), transmission service type
    (network, available transmission capability, or point-to-point, or a
    transmission service window (fixed hourly, sliding weekly, extended monthly,
    etc.).
    """
    def __init__(self) -> None:
        super().__init__()
        self.transmission_product_typeOptional[str] = ""
        """
        A TransmissionProvider offers a TransmissionProduct.
        """
        self.transmission_providerOptional[TransmissionProvider] = TransmissionProvider()
        """
        A transmission product is located on a transmission path.
        """
        self.location_forOptional[TransmissionPath] = TransmissionPath()
