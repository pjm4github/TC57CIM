# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.ProcedureDataSet import ProcedureDataSet
from IEC61968.InfIEC61968.InfAssets.Specification import Specification
from IEC61968.PaymentMetering.Transaction import Transaction
from IEC61970.Base.Domain.StringQuantity import StringQuantity


class UserAttribute:
    
    def __init__(self):
        """
        Generic name-value pair class, with optional sequence number and units for
        value; can be used to model parts of information exchange when concrete types
        are not known in advance.
        @created 20-Dec-2023 5:29:26 PM
        """
        # Name of an attribute.
        self.name = ""
        
        # Sequence number for this attribute in a list of attributes.
        self.sequence_number = 0
        
        # Value of an attribute, including unit information.
        self.value = StringQuantity()
        
        self.rating_specification = Specification()
        
        self.property_specification = Specification()
        
        self.procedure_data_sets = ProcedureDataSet()
        
        # Transaction for which this snapshot has been recorded.
        self.transaction = Transaction()
