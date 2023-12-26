package IEC61968.Metering;


/**
 * Kind of meter multiplier.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public enum MeterMultiplierKind {
	/**
	 * Meter kh (watthour) constant. The number of watthours that must be applied to
	 * the meter to cause one disk revolution for an electromechanical meter or the
	 * number of watthours represented by one increment pulse for an electronic meter.
	 */
	kH,
	/**
	 * Register multiplier. The number to multiply the register reading by in order to
	 * get kWh.
	 */
	kR,
	/**
	 * Test constant.
	 */
	kE,
	/**
	 * Current transformer ratio used to convert associated quantities to real
	 * measurements.
	 */
	ctRatio,
	/**
	 * Potential transformer ratio used to convert associated quantities to real
	 * measurements.
	 */
	ptRatio,
	/**
	 * Product of the CT ratio and PT ratio.
	 */
	transformerRatio
}