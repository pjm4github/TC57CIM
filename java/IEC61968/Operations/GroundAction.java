package IEC61968.Operations;

import IEC61970.Base.Core.ConductingEquipment;
import IEC61970.Base.Wires.Ground;
import IEC61970.Base.Wires.ACLineSegment;

/**
 * Action on ground as a switching step.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class GroundAction extends SwitchingAction {

	/**
	 * Switching action to perform.
	 */
	public TempEquipActionKind kind;
	/**
	 * Equipment being grounded with this operation. In case of placing a ground
	 * anywhere along a line segment, you must use the clamp (to get the distance from
	 * one terminal), so use the explicit relation with line segment. In all other
	 * cases (including placing the ground at a line segment terminal), reference to
	 * one or more conducting equipment is sufficient.
	 */
	public ConductingEquipment GroundedEquipment;
	/**
	 * Ground on which this action is taken.
	 */
	public Ground Ground;
	/**
	 * The line segment that this ground action will affect. This is the only way to
	 * access relationship to clamp in case the ground needs to be placed along the
	 * line segment.
	 */
	public ACLineSegment AlongACLineSegment;

	public GroundAction(){

	}
}//end GroundAction