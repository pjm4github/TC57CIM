package TC57CIM.IEC61970.Base.DC;

import TC57CIM.IEC61970.Base.Core.EquipmentContainer;

/**
 * A modeling construct to provide a root class for containment of DC as well as
 * AC equipment. The class differ from the EquipmentContaner for AC in that it may
 * also contain DCNodes. Hence it can contain both AC and DC equipment.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class DCEquipmentContainer extends EquipmentContainer {

	/**
	 * The topological nodes which belong to this connectivity node container.
	 */
	public DCTopologicalNode DCTopologicalNode;

	public DCEquipmentContainer(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}