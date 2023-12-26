package IEC61970.Base.StateVariables;

import IEC61970.Base.Wires.SinglePhaseKind;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.ReactivePower;
import IEC61970.Base.Topology.TopologicalNode;

/**
 * The SvInjection is reporting the calculated bus injection minus the sum of the
 * terminal flows. The terminal flow is positive out from the bus (load sign
 * convention) and bus injection has positive flow into the bus. SvInjection may
 * have the remainder after state estimation or slack after power flow calculation.
 * 
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class SvInjection extends StateVariable {

	/**
	 * The terminal phase at which the connection is applied.   If missing, the
	 * injection is assumed to be balanced among non-neutral phases.
	 */
	public SinglePhaseKind phase;
	/**
	 * The active power mismatch between calculated injection and initial injection.
	 * Positive sign means injection into the TopologicalNode (bus).
	 */
	public ActivePower pInjection;
	/**
	 * The reactive power mismatch between calculated injection and initial injection.
	 * Positive sign means injection into the TopologicalNode (bus).
	 */
	public ReactivePower qInjection;
	/**
	 * The topological node associated with the flow injection state variable.
	 */
	public TopologicalNode TopologicalNode;

	public SvInjection(){

	}
}//end SvInjection