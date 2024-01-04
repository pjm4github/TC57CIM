from IEC62325.MarketOperations.MarketSystem.ExternalInputs.Profile import Profile


class DataSet:
    """
    Represents a generic container of a version of instance data.
    A generic container of a version of instance data. The MRID can be used in an
    audit trail, not in reusable script intended to work with new versions of data.

    A dataset could be serialized multiple times and in multiple technologies, yet
    retain the same identity.
    @author SELAOST1
    @version 1.0
    @created 22-Dec-2023 4:59:45 PM
    """
    def __init__(self):
        self.description = ""  # The description is a free human-readable text describing or naming the object.
        self.mRID = ""  # Master resource identifier issued by a model authority.
        self.name = ""  # The name is any free human-readable and possibly non-unique text naming the object.
        self.profile = Profile()  # The profiles that describe the contents of the data set and the rules governing the contents of the data set.

# end DataSet
