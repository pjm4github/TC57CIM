package IEC61970.Base.Generation.Production;


/**
 * Type of fuel.
 * @created 02-Jan-2024 11:00:26 PM
 */
public enum FuelType {
	/**
	 * Generic coal, not including lignite type.
	 */
	coal,
	/**
	 * Oil.
	 */
	oil,
	/**
	 * Natural gas.
	 */
	gas,
	/**
	 * The fuel is lignite coal.  Note that this is a special type of coal, so the
	 * other enum of coal is reserved for hard coal types or if the exact type of coal
	 * is not known.
	 */
	lignite,
	/**
	 * Hard coal
	 */
	hardCoal,
	/**
	 * Oil Shale
	 */
	oilShale
}