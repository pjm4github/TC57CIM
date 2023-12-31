package IEC61970.Base.DC;

import IEC61970.Base.Core.EquipmentContainer;

/**
 * A modeling construct to provide a root class for containment of DC as well as
 * AC equipment. The class differ from the EquipmentContaner for AC in that it may
 * also contain DCNodes. Hence it can contain both AC and DC equipment.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class DCEquipmentContainer extends EquipmentContainer {

	/**
	 * The topological nodes which belong to this connectivity node container.
	 */
	public DCTopologicalNode DCTopologicalNode;

	public DCEquipmentContainer(){

	}
}//end DCEquipmentContainer