
"""
Dynamic flows and ratings associated with a branch end.
"""
from IEC62325.MarketOperations.MarketOpCommon.MktPowerTransformer import MktPowerTransformer
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.MktACLineSegment import MktACLineSegment
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.MktSeriesCompensator import MktSeriesCompensator


class BranchEndFlow:


    def __init__(self) -> None:
        pass

        """
        The Load Dump Rating for the branch
        """
        self.load_dump_rating: float

        """
        The Long Term Rating for the branch
        """
        self.long_term_rating: float = 0.0

        """
        The MVAR flow on the branch
        Attribute Usage: Reactive power flow at the series device, transformer, phase
        shifter, or line end
        """
        self.mvar_flow: float = 0.0

        """
        The MW flow on the branch
        Attribute Usage: Active power flow at the series device, transformer, phase
        shifter, or line end
        """
        self.mw_flow: float = 0.0

        """
        The Normal Rating for the branch
        """
        self.normal_rating: float = 0.0

        """
        The Short Term Rating for the branch
        """
        self.short_term_rating: float = 0.0

        self.mkt_ac_line_segment_end_a_flow: MktACLineSegment = MktACLineSegment()
        self.mkt_ac_line_segment_end_b_flow: MktACLineSegment = MktACLineSegment()
        self.mkt_series_compensator_end_b_flow: MktSeriesCompensator = MktSeriesCompensator()
        self.mkt_serires_compensator_end_a_flow: MktSeriesCompensator = MktSeriesCompensator()
        self.mkt_power_transformer_end_b_flow: MktPowerTransformer = MktPowerTransformer()
        self.mkt_power_transformer_end_a_flow: MktPowerTransformer = MktPowerTransformer()
