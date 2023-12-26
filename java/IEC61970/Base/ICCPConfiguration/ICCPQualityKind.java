package IEC61970.Base.ICCPConfiguration;


/**
 * Indicates the type of quality information that is to be exchanged. For
 * protection events the value shall be "none".
 * @author herb
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public enum ICCPQualityKind {
	/**
	 * Indicates that no quality is conveyed with the ICCP point.
	 */
	none,
	/**
	 * Indicates that only quality is to be provided.
	 */
	qualityOnly,
	/**
	 * Indicates that quality and a timestamp are to be provided.
	 */
	qualityAndTime,
	/**
	 * Indicates that only extended information is to be provided.
	 */
	extended,
	/**
	 * Provides quality, timestamp, and extended information.
	 */
	extendedwithQualityTime
}