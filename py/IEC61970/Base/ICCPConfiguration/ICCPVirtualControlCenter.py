# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.IEC62351_6ApplicationSecurityKind import IEC62351_6ApplicationSecurityKind


class IccpVirtualControlCenter:
    def __init__(self) -> None:
        self.application_security_requirement: Optional[IEC62351_6ApplicationSecurityKind] = IEC62351_6ApplicationSecurityKind.NO_SECURITY
        self.calling: Optional[bool] = False
        self.client_and_server: Optional[bool] = False
        self.minimum_update_interval: Optional[int] = 0
        self.name_of_local_icc: Optional[str] = ""
        self.support_for_block1: Optional[bool] = False
        self.support_for_block2: Optional[bool] = False
        self.support_for_block3: Optional[bool] = False
        self.support_for_block4: Optional[bool] = False
        self.support_for_block5: Optional[bool] = False
        self.support_for_depriciated_block8: Optional[bool] = False
        self.transport_security_requirement: Optional[bool] = False
        
