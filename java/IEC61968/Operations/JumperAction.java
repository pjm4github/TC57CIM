package IEC61968.Operations;

import IEC61970.Base.Wires.Jumper;
import IEC61970.Base.Wires.ACLineSegment;
import IEC61970.Base.Core.ConductingEquipment;

/**
 * Action on jumper as a switching step.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class JumperAction extends SwitchingAction {

	/**
	 * Switching action to perform.
	 */
	public TempEquipActionKind kind;
	/**
	 * Jumper on which this action is taken.
	 */
	public Jumper Jumper;
	/**
	 * The line segment that this jumper action will affect. This is the only way to
	 * access relationship to clamp in case the jumper needs to connect along the line
	 * segment.
	 */
	public ACLineSegment AlongACLineSegments;
	/**
	 * The conducting equipment that this jumper action will affect. In case of
	 * placing a jumper anywhere along a line segment, you must use the clamp (to get
	 * the distance from one terminal), so use the explicit relation with line segment.
	 * In all other cases (including placing the jumper at a line segment terminal),
	 * reference to one or more conducting equipment is sufficient.
	 */
	public ConductingEquipment JumpedEquipments;

	public JumperAction(){

	}
}//end JumperAction