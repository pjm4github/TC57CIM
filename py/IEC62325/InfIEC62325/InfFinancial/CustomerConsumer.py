# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:12:35 2023
from typing import Optional

from IEC61968.Common.Organisation import Organisation
from IEC62325.InfIEC62325.InfEnergyScheduling.TieLine import TieLine


class CustomerConsumer(Organisation):
    """
    The energy buyer in the energy marketplace.
    @created 27-Dec-2023 3:10:15 PM
    """

    def __init__(self) -> None:
        # 	 * A  ControlAreaOperator or CustomerConsumer may ring their perimeter with
        # 	 * metering, which can create a unique SubControlArea at the collection of
        # 	 * metering points, called a TieLine.
        super().__init__()
        self.cust_child_of: Optional[TieLine] = TieLine()
