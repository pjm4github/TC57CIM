# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from datetime import datetime
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.ICCPAccessPrivilegeKind import IccpAccessPrivilegeKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.ICCPPointKind import IccpPointKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.ICCPQualityKind import IccpQualityKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.ICCPScope import IccpScope
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.ProvidedBilateralPoint import ProvidedBilateralPoint


class IccpProvidedPoint(ProvidedBilateralPoint):
    """
    The IdentifiedObject.name attribute must have a value.
    The name attribute shall be used as the DataValue name used for the exchange.
    @author: SELAOST1
    @version: 1.0
    @created: 15-Dec-2023 4:38:27 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.access_privilege: IccpAccessPrivilegeKind = IccpAccessPrivilegeKind.READ_ONLY
        self.point_quality: IccpQualityKind = IccpQualityKind.QUALITY_ONLY
        self.point_type: IccpPointKind = IccpPointKind.SINGLE_PROTECTION_EVENT
        self.scope: IccpScope = IccpScope.ICC

