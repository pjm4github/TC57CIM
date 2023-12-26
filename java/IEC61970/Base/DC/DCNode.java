package IEC61970.Base.DC;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * DC nodes are points where terminals of DC conducting equipment are connected
 * together with zero impedance.
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class DCNode extends IdentifiedObject {

	/**
	 * DC base terminals interconnected with zero impedance at a this DC connectivity
	 * node. 
	 */
	public DCBaseTerminal DCTerminals;
	/**
	 * The DC topological node to which this DC connectivity node is assigned.  May
	 * depend on the current state of switches in the network.
	 */
	public DCTopologicalNode DCTopologicalNode;
	/**
	 * The DC container for the DC nodes.
	 */
	public DCEquipmentContainer DCEquipmentContainer;

	public DCNode(){

	}
}//end DCNode