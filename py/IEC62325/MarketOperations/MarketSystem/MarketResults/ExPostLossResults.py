# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

from IEC62325.MarketOperations.MarketSystem.MarketResults.ExPostLoss import ExPostLoss
from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea


class ExPostLossResults:
    """
    Model results of ex-post calculation of MW losses. Summarizes loss in two
    categories losses on the extra high voltage transmission and total losses.
    Calculated for each subcontrol area.
    """

    def __init__(self) -> None:
        self.ehv_loss_mw: float = 0.0  # EHV MW losses in the company
        self.total_loss_mw: float = 0.0  # Total MW losses in the company
        self.sub_control_areaOptional[SubControlArea] = SubControlArea()
        self.ex_post_lossOptional[ExPostLoss] = ExPostLoss()
