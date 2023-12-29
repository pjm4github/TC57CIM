from IEC61970.Base.Domain.DateTime import DateTime


class MitigatedBidSegment:
    """
    Model of mitigated bid. Indicates segment of piece-wise linear bid, that has been mitigated.
    @created 28-Dec-2023 8:23:55 PM
    """

    def __init__(self):
        self.interval_start_time = DateTime()

        # Mitigated bid segment MW value
        self.segment_mw = 0.0

        # Mitigated Bid Segment Number
        self.segment_number = 0

        self.threshold_type = ""
