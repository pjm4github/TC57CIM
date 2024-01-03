package IEC61970.Base.Topology;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.ReactivePower;
import IEC61970.Base.Core.ReportingGroup;
import IEC61970.Base.Core.ConnectivityNodeContainer;
import IEC61970.Base.Core.BaseVoltage;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61970.Base.Core.ConnectivityNode;
import IEC61970.Base.Core.Terminal;

/**
 * For a detailed substation model a topological node is a set of connectivity
 * nodes that, in the current network state, are connected together through any
 * type of closed switches, including  jumpers. Topological nodes change as the
 * current network state changes (i.e., switches, breakers, etc. change state).
 * For a planning model, switch statuses are not used to form topological nodes.
 * Instead they are manually created or deleted in a model builder tool.
 * Topological nodes maintained this way are also called "busses".
 * @created 02-Jan-2024 11:32:49 PM
 */
public class TopologicalNode extends IdentifiedObject {

	/**
	 * The active power injected into the bus at this location in addition to
	 * injections from equipment.  Positive sign means injection into the
	 * TopologicalNode (bus).
	 * Starting value for a steady state solution. 
	 */
	public ActivePower pInjection;
	/**
	 * The reactive power injected into the bus at this location in addition to
	 * injections from equipment. Positive sign means injection into the
	 * TopologicalNode (bus).
	 * Starting value for a steady state solution.
	 */
	public ReactivePower qInjection;
	/**
	 * The reporting group to which the topological node belongs.
	 */
	public ReportingGroup ReportingGroup;
	/**
	 * The connectivity node container to which the toplogical node belongs.
	 */
	public ConnectivityNodeContainer ConnectivityNodeContainer;
	/**
	 * The base voltage of the topologocial node.
	 */
	public BaseVoltage BaseVoltage;
	/**
	 * The connectivity nodes combine together to form this topological node.  May
	 * depend on the current state of switches in the network.
	 */
	public ConnectivityNode ConnectivityNodes;
	/**
	 * The terminals associated with the topological node.   This can be used as an
	 * alternative to the connectivity node path to terminal, thus making it
	 * unneccesary to model connectivity nodes in some cases.   Note that if
	 * connectivity nodes are in the model, this association would probably not be
	 * used as an input specification.
	 */
	public Terminal Terminal;

	public TopologicalNode(){

	}
}//end TopologicalNode