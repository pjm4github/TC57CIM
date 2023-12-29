# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.AreaLoadCurve import AreaLoadCurve

class TACArea(IdentifiedObject):
    """
    * Transmission Access Charge Area. Charges assessed, on behalf of the
    * Participating Transmission Owner, to parties who require access to the
    * controlled grid.
    * @created 28-Dec-2023 12:24:17 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.area_load_curve: AreaLoadCurve = AreaLoadCurve()
