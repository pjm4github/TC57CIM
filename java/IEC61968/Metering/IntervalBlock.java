package IEC61968.Metering;


/**
 * Time sequence of readings of the same reading type. Contained interval readings
 * may need conversion through the application of an offset and a scalar defined
 * in associated pending.
 * @created 25-Dec-2023 8:45:22 PM
 */
public class IntervalBlock {

	/**
	 * Pending calculation to apply to interval reading values contained by this block
	 * (after which the resulting reading type is different than the original because
	 * it reflects the conversion result).
	 */
	public PendingCalculation PendingCalculation;
	/**
	 * Interval reading contained in this block.
	 */
	public IntervalReading IntervalReadings;
	/**
	 * Type information for interval reading values contained in this block.
	 */
	public ReadingType ReadingType;
	/**
	 * Meter reading containing this interval block.
	 */
	public MeterReading MeterReading;

	public IntervalBlock(){

	}
}//end IntervalBlock