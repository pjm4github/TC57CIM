package IEC62325.MarketOperations.MktDomain;


/**
 * Market power mitigation test identifier type, for example:
 * 
 * 1 ? Global Price Test
 * 2 ? Global Conduct Test
 * 3 ? Global Impact Test
 * 4 ? Local Price Test
 * 5 ? Local Conduct Test
 * 6 ? Local Impact Test
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum MPMTestIdentifierType {
	/**
	 * 1 - Global Price Test.
	 */
	1,
	/**
	 * 2 - Global Conduct Test.
	 */
	2,
	/**
	 * 3 - Global Impact Test.
	 */
	3,
	/**
	 * 4 - Local Price Test.
	 */
	4,
	/**
	 * 5 - Local Conduct Test.
	 */
	5,
	/**
	 * 6 - Local Impact Test.
	 */
	6
}