package IEC62325.MarketOperations.MktDomain;


/**
 * Bid self schedule type has two types as the required output of requirements and
 * qualified pre-dispatch.
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum BidTypeRMR {
	/**
	 * Qualified pre-dispatch bid self schedule type.
	 */
	REQUIREMENTS,
	/**
	 * Output of requirements bid self schedule type.
	 */
	QUALIFIED_PREDISPATCH
}