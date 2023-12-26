package IEC62325.Environmental.EnvDomain;


/**
 * The type of uncertainty for a reading.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public enum UncertaintyKind {
	/**
	 * The value has standard uncertainty consistent with National Weather Service
	 * practises given the instrument and manner of observation.
	 */
	standard,
	/**
	 * The value is interpolated.
	 */
	interpolated,
	/**
	 * The value is estimated.
	 */
	estimated,
	/**
	 * The process of value calculation or measurement is unknown.
	 */
	unknown
}