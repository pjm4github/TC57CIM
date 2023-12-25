# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.BilateralExchangeAgreement import BilateralExchangeAgreement


class Tase2BilateralTable(BilateralExchangeAgreement):
    """
    This class describe the sending (providing) side in a bilateral ICCP data
    exchange. Hence the ICCP bilateral (table) descriptions are created by
    exchanging ICCP Provider data between the parties.
    @author SELAOST1
    @version 1.0
    @created 15-Dec-2023 4:38:30 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.bilateral_table_id: Optional[str] = ""
        self.bilateral_table_version: Optional[str] = ""
        self.tase2_version: Optional[str] = ""

