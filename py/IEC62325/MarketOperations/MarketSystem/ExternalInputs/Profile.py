from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.ProfileData import ProfileData


class Profile(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.profile_datas = ProfileData()  # A profile has profile data associated with it.