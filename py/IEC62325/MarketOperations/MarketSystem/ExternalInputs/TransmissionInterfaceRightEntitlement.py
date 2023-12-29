# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.ReferenceData.ContractRight import ContractRight


class TransmissionInterfaceRightEntitlement:
    def __init__(self):
        self.entitlement = 0.0  # the entitlement
        self.pod = ""  # point of delivery
        self.por = ""  # point of receipt
        self.start_operating_date = DateTime()  # Operating date and hour when the entitlement applies
        self.contract_right = ContractRight()