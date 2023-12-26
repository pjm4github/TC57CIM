package IEC61968.Metering;


/**
 * Kind of aggregation for read / measured values from multiple end points.
 * @author Marty
 * @version 1.0
 * @created 25-Dec-2023 8:45:18 PM
 */
public enum AggregateKind {
	/**
	 * Not applicable.
	 */
	none,
	/**
	 * The value represents average.
	 */
	average,
	/**
	 * The value represents an amount over which a threshold was exceeded.
	 */
	excess,
	/**
	 * The value represents a programmed high threshold. 
	 */
	highThreshold,
	/**
	 * The value represents a programmed low threshold. 
	 */
	lowThreshold,
	/**
	 * The highest value observed.
	 */
	maximum,
	/**
	 * The smallest value observed.
	 */
	minimum,
	/**
	 * The nominal value.
	 */
	nominal,
	/**
	 * The normal value.
	 */
	normal,
	/**
	 * The second highest value observed.
	 */
	secondMaximum,
	/**
	 * The second smallest value observed.
	 */
	secondMinimum,
	/**
	 * The third highest value observed.
	 */
	thirdMaximum,
	/**
	 * The fourth highest value observed.
	 */
	fourthMaximum,
	/**
	 * The fifth highest value observed.
	 */
	fifthMaximum,
	/**
	 * The accumulated sum.
	 */
	sum
}