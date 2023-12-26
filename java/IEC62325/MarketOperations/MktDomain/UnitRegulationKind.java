package IEC62325.MarketOperations.MktDomain;


/**
 * Unit regulation kind.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public enum UnitRegulationKind {
	/**
	 * Unit is not on regulation.
	 */
	0,
	/**
	 * Unit is on AGC and regulating.
	 */
	1,
	/**
	 * Unit is suppose to be on regulation but it is not under regulation now.
	 */
	2
}