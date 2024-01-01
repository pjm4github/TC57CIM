# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC62325.MarketOperations.ParticipantInterfaces.TransactionBid import TransactionBid
from IEC62325.MarketOperations.MarketSystem.EnergyTransaction import EnergyTransaction


class TransmissionReservation:
    """
    A transmission reservation is obtained from the OASIS system to reserve
    transmission for a specified time period, transmission path and transmission
    product.
    @created 27-Dec-2023 3:33:59 PM
    """
    def __init__(self) -> None:
        self.transaction_bidOptional[TransactionBid] = TransactionBid()
        self.energy_transactionOptional[EnergyTransaction] = EnergyTransaction()
