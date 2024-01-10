# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime


class TREntitlement:
    """
    A Transmission Right(TR) can be a chain of TR's or an individual.
    
    When a transmission right is not a chain, this is formally the ETC/TOR
    Entitlement for each ETC/TOR contract with the inclusion of CVR(Converted
    Rights) as an ETC. This is the sum of all entitlements on all related
    transmission interfaces for the same TR.
    
    When TR is a chain, its entitlement is the minimum of all entitlements for the
    individual TRs in the chain.
    
    @created 27-Dec-2023 3:32:44 PM
    """

    def __init__(self) -> None:
        """
        The entitlement
        """
        self.entitlement: float = 0.0
        """
        Operating date and hour when the entitlement applies
        """
        self.start_operating_date: Optional[DateTime] = DateTime()
