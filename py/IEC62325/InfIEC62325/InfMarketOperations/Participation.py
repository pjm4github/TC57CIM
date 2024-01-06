from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject  # Importing IdentifiedObject class from IEC61970.Base.Core module

class Participation(IdentifiedObject):
    """
    Participation level of a given Pnode in a given AggregatePnode.
    @created 28-Dec-2023 7:59:52 PM
    """

    def __init__(self):
        super().__init__()  # Calling the __init__() method of the superclass
        self.factor = 1.0 # Used to calculate "participation" of Pnode in an
        # AggregatePnode. For example, for regulation region this factor is 1 and
        # total sum of all factors for a specific regulation region does not have to be 1.
        # For pricing zone the total sum of all factors has to be 1.