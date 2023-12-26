package IEC62325.Environmental.EnvDomain;


/**
 * The nature of the location being defined for an environmental entity. Possible
 * values are center, perimeter, primary, secondary.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public enum LocationKind {
	/**
	 * The center of a phenomenon. Will typically be used with a Location with a
	 * single PositionPoint instance.
	 */
	center,
	/**
	 * The area or line of a phenomenon, not the center. Will typically be used with a
	 * Location with multiple PositionPoint instances.
	 */
	extent,
	/**
	 * Primary area to which an environmental alert applies.
	 */
	primary,
	/**
	 * Secondary area to which an environmental alert applies.
	 */
	secondary
}