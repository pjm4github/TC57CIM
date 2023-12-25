package TC57CIM.IEC61970.Base.Faults;

import TC57CIM.IEC61970.Base.Domain.Resistance;
import TC57CIM.IEC61970.Base.Domain.Reactance;

/**
 * Impedance description for the fault.
 * @author kdemaree
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
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

	public void finalize() throws Throwable {

	}

}