package IEC61970.Base.Topology;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * An electrically connected subset of the network. Topological islands can change
 * as the current network state changes: e.g. due to
 * - disconnect switches or breakers change state in a SCADA/EMS
 * - manual creation, change or deletion of topological nodes in a planning tool.
 * @created 02-Jan-2024 11:32:33 PM
 */
public class TopologicalIsland extends IdentifiedObject {

	/**
	 * The angle reference for the island.   Normally there is one TopologicalNode
	 * that is selected as the angle reference for each island.   Other reference
	 * schemes exist, so the association is typically optional.
	 */
	public TopologicalNode AngleRefTopologicalNode;
	/**
	 * A topological node belongs to a topological island.
	 */
	public TopologicalNode TopologicalNodes;

	public TopologicalIsland(){

	}
}//end TopologicalIsland