from IEC61970.Base.Contingency.Contingency import Contingency


class MktContingency(Contingency):
    def __init__(self):
        # load change flag
        # Flag that indicates whether load rollover and load pickup should be processed for this contingency
        super().__init__()
        self.load_rollover_flag = False

        # ltc enable flag
        # Flag that indicates if LTCs regulate voltage during the solution of the contingency
        self.ltc_control_flag = False

        # Participation Factor flag
        # An indication which set of generator participation factors should be used to re-allocate generation in this contingency
        self.participation_factor_set = ""

        # sceening flag for outage
        # Flag that indicated whether screening is bypassed for the contingency
        self.screening_flag = False