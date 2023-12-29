# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

class GenDistributionFactor:
    """
    This class models the generation distribution factors. This class needs to be
    used along with the AggregatedPnode and the IndividualPnode to show the
    distribution of each individual party.
    @created 27-Dec-2023 3:28:35 PM
    """

    def __init__(self) -> None:
        """
        Used to calculate generation "participation" of an individual pnode in an
        AggregatePnode.
        """
        self.factor: Optional[float] = 0.0
