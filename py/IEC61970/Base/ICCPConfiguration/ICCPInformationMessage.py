# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.ICCPScope import IccpScope
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.TASE2BilateralTable import Tase2BilateralTable


class IccpInformationMessage(IdentifiedObject):
    """
    This class represents the TASE.2 Information Message Object. The
    IdentifiedObject.name attribute must be non-null. The value of the attribute
    shall be used as the TASE.2 Information Reference, as specified by 60870-6-503.
    """

    def __init__(self) -> None:
        super().__init__()
        self.local_reference: Optional[str] = ""
        self.scope: Optional[IccpScope] = IccpScope.ICC
        self.tase_2_bilateral_table: Optional[Tase2BilateralTable] = Tase2BilateralTable()

