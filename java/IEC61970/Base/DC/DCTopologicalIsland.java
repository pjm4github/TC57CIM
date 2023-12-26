package IEC61970.Base.DC;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * An electrically connected subset of the network. DC topological islands can
 * change as the current network state changes: e.g. due to
 * - disconnect switches or breakers change state in a SCADA/EMS
 * - manual creation, change or deletion of topological nodes in a planning tool.
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class DCTopologicalIsland extends IdentifiedObject {

	/**
	 * The DC topological nodes in a DC topological island.
	 */
	public DCTopologicalNode DCTopologicalNodes;

	public DCTopologicalIsland(){

	}
}//end DCTopologicalIsland