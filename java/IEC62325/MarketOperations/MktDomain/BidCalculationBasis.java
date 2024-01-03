package IEC62325.MarketOperations.MktDomain;


/**
 * The basis used to calculate the bid price curve for an energy default bid.
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum BidCalculationBasis {
	/**
	 * Based on prices paid at particular pricing location.
	 */
	LMP_BASED,
	/**
	 * Based on unit generation characteristics and a cost of fuel.
	 */
	COST_BASED,
	/**
	 * An amount negotiated with the designated Independent Entity.
	 */
	NEGOTIATED
}