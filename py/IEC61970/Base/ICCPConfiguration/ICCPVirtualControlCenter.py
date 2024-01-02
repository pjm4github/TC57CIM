# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from typing import Optional

from IEC61970.Base.ICCPConfiguration.IEC62351_6ApplicationSecurityKind import IEC62351_6ApplicationSecurityKind


class IccpVirtualControlCenter:
    def __init__(self) -> None:
        self.application_security_requirementOptional[IEC62351_6ApplicationSecurityKind] = IEC62351_6ApplicationSecurityKind.NO_SECURITY
        self.callingbool = False
        self.client_and_serverbool = False
        self.minimum_update_intervalOptional[int] = 0
        self.name_of_local_iccOptional[str] = ""
        self.support_for_block1bool = False
        self.support_for_block2bool = False
        self.support_for_block3bool = False
        self.support_for_block4bool = False
        self.support_for_block5bool = False
        self.support_for_depriciated_block8bool = False
        self.transport_security_requirementbool = False
        
