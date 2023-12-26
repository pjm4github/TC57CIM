package IEC61968.AssetInfo;


/**
 * Kind of cable outer jacket.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public enum CableOuterJacketKind {
	/**
	 * Cable has no outer jacket.
	 */
	none,
	/**
	 * Linear low density polyethylene cable outer jacket.
	 */
	linearLowDensityPolyethylene,
	/**
	 * PVC cable outer jacket.
	 */
	pvc,
	/**
	 * Polyethylene cable outer jacket.
	 */
	polyethylene,
	/**
	 * Insulating cable outer jacket.
	 */
	insulating,
	/**
	 * Semiconducting cable outer jacket.
	 */
	semiconducting,
	/**
	 * Pther kind of cable outer jacket.
	 */
	other
}