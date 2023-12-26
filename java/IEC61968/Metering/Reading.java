package IEC61968.Metering;


/**
 * Specific value measured by a meter or other asset, or calculated by a system.
 * Each Reading is associated with a specific ReadingType.
 * @created 25-Dec-2023 8:45:24 PM
 */
public class Reading extends BaseReading {

	/**
	 * Reason for this reading being taken.
	 */
	public ReadingReasonKind reason;
	/**
	 * Type information for this reading value.
	 */
	public ReadingType ReadingType;
	/**
	 * All meter readings (sets of values) containing this reading value.
	 */
	public MeterReading MeterReadings;

	public Reading(){

	}
}//end Reading