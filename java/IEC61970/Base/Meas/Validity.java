package IEC61970.Base.Meas;


/**
 * Validity for MeasurementValue.
 * @created 02-Jan-2024 11:27:03 PM
 */
public enum Validity {
	/**
	 * The value is marked good if no abnormal condition of the acquisition function
	 * or the information source is detected.
	 */
	GOOD,
	/**
	 * The value is marked questionable if a supervision function detects an abnormal
	 * behaviour, however the value could still be valid. The client is responsible
	 * for determining whether or not values marked "questionable" should be used.
	 */
	QUESTIONABLE,
	/**
	 * The value is marked invalid when a supervision function recognises abnormal
	 * conditions of the acquisition function or the information source (missing or
	 * non-operating updating devices). The value is not defined under this condition.
	 * The mark invalid is used to indicate to the client that the value may be
	 * incorrect and shall not be used.
	 */
	INVALID
}