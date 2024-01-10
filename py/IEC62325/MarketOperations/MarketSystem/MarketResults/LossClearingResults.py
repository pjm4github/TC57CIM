# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea


class LossClearingResults:
    """
    Provides the MW loss for RUC Zones, subcontrol areas, and the total loss.
    @created 28-Dec-2023 8:22:26 PM
    """

    def __init__(self) -> None:
        self.loss_mw: float = 0.0
        self.sub_control_area: Optional[SubControlArea] = SubControlArea()

