package IEC62325.MarketOperations.MarketPlan;

import IEC61970.Base.Domain.Currency;
import IEC61970.Base.Domain.UnitSymbol;
import IEC61970.Base.Domain.UnitMultiplier;
import IEC62325.MarketOperations.ReferenceData.Pnode;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Commodities in the context of IEC 62325 are MarketProducts (energy, regulation,
 * reserve, etc) traded at a specific location, which in this case is a Pnode
 * (either a specific pricing node or a pricing area or zone defined as a
 * collection of pricing nodes).  The CommodityDefinition is a container for these
 * two parameters, plus the unit of measure and the currency in which the
 * Commodity is traded.  Each CommodityDefinition should be relatively static;
 * defined once and rarely changed.
 * @author Margaret
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class CommodityDefinition extends IdentifiedObject {

	/**
	 * The currency in which the Commodity is traded, using the standard conventions
	 * associated with the Currency enumeration.
	 */
	public Currency commodityCurrency;
	/**
	 * The unit of measure in which the Commodity is traded, using the standard
	 * conventions associated with the UnitSymbol enumeration.
	 */
	public UnitSymbol commodityUnit;
	/**
	 * The unit multiplier, e.g. "k" to convert the unit "W-h" to "kW-h", using the
	 * standard conventions associated with the UnitMultiplier enumeration.
	 */
	public UnitMultiplier commodityUnitMultiplier;
	public Pnode Pnode;
	public MarketProduct MarketProduct;

	public CommodityDefinition(){

	}
}//end CommodityDefinition