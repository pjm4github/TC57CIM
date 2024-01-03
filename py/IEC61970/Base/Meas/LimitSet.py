from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class LimitSet(IdentifiedObject):
    """
    Specifies a set of Limits that are associated with a Measurement. A Measurement
    may have several LimitSets corresponding to seasonal or other changing
    conditions. The condition is captured in the name and description attributes.
    The same LimitSet may be used for several Measurements. In particular
    percentage limits are used this way.
    @created 03-Jan-2024 4:16:31 PM
    """
    def __init__(self):
        super().__init__()
        self.is_percentage_limits = True  # Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls