# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.ActivePower import ActivePower


class RegulatingLimit(IdentifiedObject):
    """
    * This class represents the physical characteristic of a generator regarding the
    * regulating limit.
    * @created 28-Dec-2023 12:22:11 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.high_limit: ActivePower = ActivePower()
        self.low_limit: ActivePower = ActivePower()
