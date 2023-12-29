# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.EnergyProfile import EnergyProfile
from IEC62325.MarketOperations.ParticipantInterfaces import Bid
from typing import Optional

class TransactionBid(Bid):
    """
    Bilateral or scheduled transactions for energy and ancillary services 
    considered by market clearing process.
    @created 28-Dec-2023 5:24:21 PM
    """

    def __init__(self) -> None:
        """
        Constructor for TransactionBid class.
        """
        self.demand_transaction: Optional[bool] = False  # Set true if this is a demand transaction.
        self.dispatchable: Optional[bool] = False  # Set true if this is a dispatchable transaction.
        self.pay_congestion: Optional[bool] = False  # Set true if this is a willing to pay transaction. This flag is used to 
                                                    # determine whether a schedule is willing-to-pay-congestion or not. 
        self.energy_profiles: Optional[EnergyProfile] = EnergyProfile()

