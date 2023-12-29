from IEC61970.Base.Domain.DateTime import DateTime


class ChargeProfileData:
    """
    Model of various charges associated with an energy profile to support billing and settlement.
    @created 28-Dec-2023 8:18:48 PM
    """

    def __init__(self):
        # The sequence number of the profile.
        self.sequence = 0

        # The date and time of an interval.
        self.time_stamp = DateTime()

        # The value of an interval given a profile type (amount, price, or quantity), subject to the UOM.
        self.value = 0.0
