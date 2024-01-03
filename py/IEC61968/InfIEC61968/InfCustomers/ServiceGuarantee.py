# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:39:47 2023
from IEC61968.Common.Document import Document
from IEC61970.Base.Domain.DateTime import DateTime


class ServiceGuarantee(Document):
    """
    A service guarantee, often imposed by a regulator, defines conditions that, if
    not satisfied, will result in the utility making a monetary payment to the
    customer. Note that guarantee's identifier is in the 'name' attribute and the
    status of the guarantee is in the 'Status.status' attribute.

    Example service requirements include:
    1) If power is not restored within 24 hours, customers can claim $50 for
    residential customers or $100 for commercial and industrial customers. In
    addition for each extra period of 12 hours the customer's supply has not been
    activated, the customer can claim $25.
    2) If a customer has a question about their electricity bill, the utility will
    investigate and respond to the inquiry within 15 working days. If utility
    fails to meet its guarantee, utility will automatically pay the customer $50.
    @created 29-Dec-2023 9:25:49 PM
    """
    
    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.application_period = DateTime()  # Period in which this service guarantee applies
        self.automatic_pay = False  # True if utility must automatically pay the specified amount whenever the condition is not satisfied, otherwise customer must make a claim to receive payment
        self.pay_amount = 1.0  # Amount to be paid by the service provider to the customer for each violation of the 'service_requirement'
        self.service_requirement = ""  # Explanation of the requirement and conditions for satisfying it
