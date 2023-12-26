package IEC61968.Metering;


/**
 * Kind of service multiplier.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public enum ServiceMultiplierKind {
	/**
	 * Current transformer ratio used to convert associated quantities to real
	 * measurements.
	 */
	ctRatio,
	/**
	 * Voltage transformer ratio used to convert associated quantities to real
	 * measurements.
	 */
	ptRatio,
	/**
	 * Product of the CT ratio and PT ratio.
	 */
	transformerRatio
}