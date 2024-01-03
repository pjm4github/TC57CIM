package IEC61970.InfIEC61970.InfSIPS;


/**
 * Categorisation of different protective action adjustments that can be performed
 * on equipment.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:36:55 PM
 */
public enum ProtectiveActionAdjustmentKind {
	/**
	 * The adjustment is in percentage of the active value.
	 */
	byPercentage,
	/**
	 * The adjustment is in given by a value that defined the changes that will be
	 * done to the active value.
	 */
	byValue,
	/**
	 * The equipment will operate on the new value.
	 */
	setValue,
	/**
	 * The equipment will operating on a value given by a measurement.
	 */
	measurement
}