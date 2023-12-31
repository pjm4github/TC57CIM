package IEC61970.Base.StateVariables;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Wires.SinglePhaseKind;
import IEC61970.Base.Domain.ReactivePower;
import IEC61970.Base.Core.Terminal;
import IEC61970.InfIEC61970.EnergyArea.EnergyGroup;

/**
 * State variable for power flow. Load convention is used for flow direction. This
 * means flow out from the TopologicalNode into the equipment is positive.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class SvPowerFlow extends StateVariable {

	/**
	 * The active power flow. Load sign convention is used, i.e. positive sign means
	 * flow out from a TopologicalNode (bus) into the conducting equipment.
	 */
	public ActivePower p;
	/**
	 * The individual phase of the flow.   If unspecified, then assumed to be balanced
	 * among phases.
	 */
	public SinglePhaseKind phase;
	/**
	 * The reactive power flow. Load sign convention is used, i.e. positive sign means
	 * flow out from a TopologicalNode (bus) into the conducting equipment.
	 */
	public ReactivePower q;
	/**
	 * The terminal associated with the power flow state variable.
	 */
	public Terminal Terminal;
	public EnergyGroup m_EnergyGroup;

	public SvPowerFlow(){

	}
}//end SvPowerFlow