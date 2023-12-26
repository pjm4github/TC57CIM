package IEC61968.Operations;


/**
 * Kind of action on temporary equipment (such as cut, jumper, ground, energy
 * source).
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public enum TempEquipActionKind {
	/**
	 * Place the jumper (close) or the cut (open).
	 */
	place,
	/**
	 * Remove the jumper (open) or the cut (close).
	 */
	remove
}