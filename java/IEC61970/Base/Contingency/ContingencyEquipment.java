package IEC61970.Base.Contingency;

import IEC61970.Base.Core.Equipment;

/**
 * A equipment to which the in service status is to change such as a power
 * transformer or AC line segment.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class ContingencyEquipment extends ContingencyElement {

	/**
	 * The status for the associated equipment when in the contingency state.   This
	 * status is independent of the case to which the contingency is originally
	 * applied, but defines the equipment status when the contingency is applied.
	 */
	public ContingencyEquipmentStatusKind contingentStatus;
	/**
	 * The single piece of equipment to which to apply the contingency.
	 */
	public Equipment Equipment;

	public ContingencyEquipment(){

	}
}//end ContingencyEquipment