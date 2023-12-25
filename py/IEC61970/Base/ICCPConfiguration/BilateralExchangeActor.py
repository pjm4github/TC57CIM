# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.BilateralExchangeAgreement import BilateralExchangeAgreement


class BilateralExchangeActor(IdentifiedObject):

    def __init__(self) -> None:
        super().__init__()
        self.provider_bilateral_exchange = BilateralExchangeAgreement()
