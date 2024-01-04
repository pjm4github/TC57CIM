from IEC61968.Operations.SafetyDocument import SafetyDocument
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource


class ClearanceDocument(SafetyDocument):
    def __init__(self):
        super().__init__()
        self.must_be_deenergised = True  # If true, the equipment must be deenergised.
        self.must_be_grounded = True  # If true, the equipment must be grounded.
        self.tagged_psrs = PowerSystemResource()  # All power system resources tagged through this clearance.
