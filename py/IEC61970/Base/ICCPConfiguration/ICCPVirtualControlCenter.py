# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from typing import Optional

from IEC61970.Base.ICCPConfiguration.IEC62351_6ApplicationSecurityKind import IEC62351_6ApplicationSecurityKind


class IccpVirtualControlCenter:
    def __init__(self) -> None:
        self.application_security_requirementOptional[IEC62351_6ApplicationSecurityKind] = IEC62351_6ApplicationSecurityKind.NO_SECURITY
        self.callingOptional[bool] = False
        self.client_and_serverOptional[bool] = False
        self.minimum_update_intervalOptional[int] = 0
        self.name_of_local_iccOptional[str] = ""
        self.support_for_block1Optional[bool] = False
        self.support_for_block2Optional[bool] = False
        self.support_for_block3Optional[bool] = False
        self.support_for_block4Optional[bool] = False
        self.support_for_block5Optional[bool] = False
        self.support_for_depriciated_block8Optional[bool] = False
        self.transport_security_requirementOptional[bool] = False
        
