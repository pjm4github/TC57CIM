package IEC61970.InfIEC61970.InfSIPS;


/**
 * Categories of analog to digital (or logical result) comparison.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:35:35 PM
 */
public enum AnalogToDigitalLogicKind {
	/**
	 * Not equal (unlike) comparison operation.
	 */
	ne,
	/**
	 * Equal (like) comparison operation.
	 */
	eq,
	/**
	 * Less or equal comparison operation.
	 */
	le,
	/**
	 * Less than comparison operation.
	 */
	lt,
	/**
	 * Greater or equal comparison operation.
	 */
	ge,
	/**
	 * Greater than comparison operation.
	 */
	gt
}