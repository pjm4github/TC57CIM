package IEC61968.AssetInfo;


/**
 * Kind of wire usage.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:26 PM
 */
public enum WireUsageKind {
	/**
	 * Wire is used in extra-high voltage or high voltage network.
	 */
	transmission,
	/**
	 * Wire is used in medium voltage network.
	 */
	distribution,
	/**
	 * Wire is used in low voltage circuit.
	 */
	secondary,
	/**
	 * Other kind of wire usage.
	 */
	other
}