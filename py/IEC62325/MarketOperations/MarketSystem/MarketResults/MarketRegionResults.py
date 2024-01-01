# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

from IEC62325.MarketOperations.MktDomain.ResourceLimitIndicator import ResourceLimitIndicator
from IEC62325.MarketOperations.MktDomain.YesNo import YesNo


class MarketRegionResults:
    """
    Provides all Region Ancillary Service results for the DA and RT markets. The
    specific data is commodity type (Regulation Up, Regulation Down, Spinning
    Reserve, Non-spinning Reserve, or Total Up reserves) based for the cleared MW,
    cleared price, and total capacity required for the region.
    @created 28-Dec-2023 8:23:02 PM
    """

    def __init__(self) -> None:
        """
        Cleared generation Value in MW.  For AS, this value is clearedMW = AS Total.
        For AS, clearedMW - selfScheduleMW = AS Procured
        """
        self.cleared_mw: float = 0.0

        """
        Marginal Price ($/MW) for the commodity (Energy, Regulation Up, Regulation Down,
        Spinning Reserve, or Non-spinning reserve) based on the pricing run.
        """
        self.cleared_price: float = 0.0

        """
        Dispatchable MW for Combustion units.
        """
        self.dispatch_ct_mw: float = 0.0

        """
        Dispatchable MW for Hydro units.
        """
        self.dispatch_hydro_mw: float = 0.0

        """
        Dispatch rate in MW/minutes.
        """
        self.dispatch_rate: float = 0.0

        """
        Dispatchable MW for Steam units.
        """
        self.dispatch_steam_mw: float = 0.0

        """
        Imbalance Energy Bias (MW) by Time Period (5' only)
        """
        self.imbalance_energy_bias: float = 0.0

        """
        Locational AS Flags indicating whether the Upper or Lower Bound limit of the AS
        regional procurment is binding
        """
        self.limit_flagOptional[ResourceLimitIndicator] = ResourceLimitIndicator.LOWER

        """
        The "Lumpy Flag"(Y/N)  indicates whether the resource that sets the price is a
        lumpy generator by hour over the time horizon.
        Only applicable for the Day Ahead Market
        """
        self.lumpy_indicatorOptional[YesNo] = YesNo.NO

        """
        Region requirement maximum limit
        """
        self.max_sufficiency_index: float = 0.0

        """
        Region requirement minimum limit
        """
        self.min_sufficiency_index: float = 0.0

        """
        Region requirement maximum limit
        """
        self.req_max_mw: float = 0.0

        """
        Region requirement minimum limit
        """
        self.req_min_mw: float = 0.0

        """
        Aof AS, selfScheduleMW = AS Self-Provided
        """
        self.self_schedule_mw: float = 0.0
