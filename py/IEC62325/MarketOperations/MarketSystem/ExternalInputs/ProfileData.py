from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.RealEnergy import RealEnergy


class ProfileData:
    def __init__(self):
        self.bid_price = 0.0  # Bid price associated with contract
        self.capacity_level = ActivePower()  # Capacity level for the profile, in MW.
        self.energy_level = RealEnergy()  # Energy level for the profile, in MWH.
        self.minimum_level = 0.0  # Minimum MW value of contract
        self.sequence_number = 0  # Sequence to provide item numbering for the profile. { greater than or equal to 1 }
        self.start_date_time = DateTime()  # Start date/time for this profile.
        self.stop_date_time = DateTime()  # Stop date/time for this profile.