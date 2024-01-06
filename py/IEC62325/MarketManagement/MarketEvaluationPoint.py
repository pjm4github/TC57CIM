from IEC61968.Metering.UsagePoint import UsagePoint


class MarketEvaluationPoint(UsagePoint):
    """
    The identification of an entity where energy products are measured or computed.
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
