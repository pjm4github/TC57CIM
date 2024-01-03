package IEC62325.MarketOperations.MktDomain;


/**
 * Time of Use used by a CRR definition for specifying the time the CRR spans. ON -
 * CRR spans the on peak hours of the day, OFF - CRR spans the off peak hours of
 * the day, 24HR - CRR spans the entire day.
 * @created 03-Jan-2024 2:12:38 PM
 */
public enum TimeOfUse {
	/**
	 * Time of use spans only the on peak hours of the day.
	 */
	ON,
	/**
	 * Time of use spans only the off peak hours of the day.
	 */
	OFF,
	/**
	 * Time of use spans the entire day, 24 hours.
	 */
	24HR
}