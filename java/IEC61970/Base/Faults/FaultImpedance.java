package IEC61970.Base.Faults;

import IEC61970.Base.Domain.Resistance;
import IEC61970.Base.Domain.Reactance;

/**
 * Impedance description for the fault.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class FaultImpedance {

	/**
	 * The resistance of the fault between phases and ground.
	 */
	public Resistance rGround;
	/**
	 * The resistance of the fault between phases.
	 */
	public Resistance rLineToLine;
	/**
	 * The reactance of the fault between phases and ground.
	 */
	public Reactance xGround;
	/**
	 * The reactance of the fault between phases.
	 */
	public Reactance xLineToLine;

	public FaultImpedance(){

	}
}//end FaultImpedance