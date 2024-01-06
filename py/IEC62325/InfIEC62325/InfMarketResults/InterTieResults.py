
class InterTieResults:
    """
    Provides the tie point specific output from the market applications. Currently,
    this is defined as the loop flow compensation MW value.
    @created 28-Dec-2023 8:01:14 PM
    """
    def __init__(self):
        self.base_mw = 1.0  # Float, Net Actual MW Flow
        self.cleared_value = 1.0  # Float, Net Dispatched MW


