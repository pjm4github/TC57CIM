# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.ReferenceData.ContractRight import ContractRight


class TransmissionRightChain(IdentifiedObject):
    def __init__(self) -> None:
        super().__init__()
        self.ind_contract_rightOptional[ContractRight] = ContractRight()
        self.chain_contract_rightOptional[ContractRight] = ContractRight()

