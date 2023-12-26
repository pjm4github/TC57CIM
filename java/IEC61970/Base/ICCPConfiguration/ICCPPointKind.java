package IEC61970.Base.ICCPConfiguration;


/**
 * This specifies the type of ICCP point that is to be conveyed
 * @author herb
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public enum ICCPPointKind {
	/**
	 * Indicates that an ICCP discrete type is to be conveyed.
	 */
	discrete,
	/**
	 * Indicates that an ICCP real type is to be conveyed.
	 */
	real,
	/**
	 * Indicates that an ICCP state type is to be conveyed.
	 */
	state,
	stateSupplemental,
	/**
	 * Indicates that an ICCP single Protection Event  type is to be conveyed.
	 */
	singleProtectionEvent,
	/**
	 * Indicates that an ICCP packed Protection Event is to be conveyed.
	 */
	packedProtectionEvent
}