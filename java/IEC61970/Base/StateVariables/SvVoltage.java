package TC57CIM.IEC61970.Base.StateVariables;

import TC57CIM.IEC61970.Base.Domain.AngleDegrees;
import TC57CIM.IEC61970.Base.Wires.SinglePhaseKind;
import TC57CIM.IEC61970.Base.Domain.Voltage;
import TC57CIM.IEC61970.Base.Topology.TopologicalNode;

/**
 * State variable for voltage.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:29 PM
 */
public class SvVoltage extends StateVariable {

	/**
	 * The voltage angle of the topological node complex voltage with respect to
	 * system reference.
	 */
	public AngleDegrees angle;
	/**
	 * If specified the voltage is the line to ground voltage of the individual phase.
	 *  If unspecified, then the voltage is assumed balanced.  
	 */
	public SinglePhaseKind phase;
	/**
	 * The voltage magnitude at the topological node.
	 */
	public Voltage v;
	/**
	 * The topological node associated with the voltage state.
	 */
	public TopologicalNode TopologicalNode;

	public SvVoltage(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}