# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Date import Date
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class Agreement(Document):
    #
    # Formal agreement between two parties defining the terms and conditions for a
    # set of services. The specifics of the services are, in turn, defined via one or
    # more service agreements.
    # @created 20-Dec-2023 5:26:37 PM
    
    def __init__(self):
        # Date this agreement was consummated among associated persons and/or
        # organisations.
        super().__init__()
        self.sign_date = Date()
        # Date and time interval this agreement is valid (from going into effect to
        # termination).
        self.validity_interval = DateTimeInterval()
