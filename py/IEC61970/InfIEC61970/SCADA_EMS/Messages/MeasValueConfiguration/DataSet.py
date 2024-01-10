# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:08:40 2024
# Class representing a data set
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Part303.GenericDataset.Profile import Profile


class DataSet(IdentifiedObject):
    """
    @author selaost1
    @version 1.0
    @created 25-Dec-2023 8:31:55 PM
    """

    def __init__(self):
        super().__init__()
        self.profile = Profile()  # Initialize profile attribute as Profile class instance
