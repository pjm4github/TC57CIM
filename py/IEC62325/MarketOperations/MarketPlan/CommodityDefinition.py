# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.Currency import Currency
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC62325.MarketOperations.ReferenceData.Pnode import Pnode
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.MarketPlan.MarketProduct import MarketProduct


class CommodityDefinition(IdentifiedObject):
    """
    Commodities in the context of IEC 62325 are MarketProducts (energy, regulation,
    reserve, etc) traded at a specific location, which in this case is a Pnode
    (either a specific pricing node or a pricing area or zone defined as a
    collection of pricing nodes).  The CommodityDefinition is a container for these
    two parameters, plus the unit of measure and the currency in which the
    Commodity is traded.  Each CommodityDefinition should be relatively static;
    defined once and rarely changed.
    @author Margaret
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        super().__init__()
        # 	 * The currency in which the Commodity is traded, using the standard conventions
        # 	 * associated with the Currency enumeration.
        self.commodity_currency = Currency()
        # 	 * The unit of measure in which the Commodity is traded, using the standard
        # 	 * conventions associated with the UnitSymbol enumeration.
        self.commodity_unit = UnitSymbol.none
        # 	 * The unit multiplier, e.g. "k" to convert the unit "W-h" to "kW-h", using the
        # 	 * standard conventions associated with the UnitMultiplier enumeration.
        self.commodity_unit_multiplier = UnitMultiplier.none
        self.pnode = Pnode()
        self.market_product = MarketProduct()
