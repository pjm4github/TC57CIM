# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:08:40 2024
# public class DataSetMember extends IdentifiedObject {
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class DataSetMember(IdentifiedObject):
    """
    @author selaost1
    @version 1.0
    @created 25-Dec-2023 8:31:55 PM
    """
    def __init__(self):
        super().__init__()
        self.properties_object = IdentifiedObject()  # // attribute initialized to the class type as a method call
        self.target_object = IdentifiedObject()  # // attribute initialized to the class type as a method call

