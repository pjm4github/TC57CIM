package TC57CIM.IEC61970.Base.DC;

import TC57CIM.IEC61970.Base.Core.IdentifiedObject;

/**
 * An electrically connected subset of the network. DC topological islands can
 * change as the current network state changes: e.g. due to
 * - disconnect switches or breakers change state in a SCADA/EMS
 * - manual creation, change or deletion of topological nodes in a planning tool.
 * @author SELAOST1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class DCTopologicalIsland extends IdentifiedObject {

	/**
	 * The DC topological nodes in a DC topological island.
	 */
	public DCTopologicalNode DCTopologicalNodes;

	public DCTopologicalIsland(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}