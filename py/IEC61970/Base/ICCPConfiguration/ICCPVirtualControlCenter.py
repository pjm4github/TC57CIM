# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from typing import Optional

from IEC61970.Base.ICCPConfiguration.Iec623516applicationsecuritykind import Iec623516applicationsecuritykind


class IccpVirtualControlCenter:
    def __init__(self) -> None:
        self.application_security_requirement: Optional[Iec623516applicationsecuritykind] = Iec623516applicationsecuritykind.NO_SECURITY
        self.calling: bool = False
        self.client_and_server: bool = False
        self.minimum_update_interval: Optional[int] = 0
        self.name_of_local_icc: Optional[str] = ""
        self.support_for_block1: bool = False
        self.support_for_block2: bool = False
        self.support_for_block3: bool = False
        self.support_for_block4: bool = False
        self.support_for_block5: bool = False
        self.support_for_depriciated_block8: bool = False
        self.transport_security_requirement: bool = False
        
