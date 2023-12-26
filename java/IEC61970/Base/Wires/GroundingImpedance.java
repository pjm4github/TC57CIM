package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Reactance;

/**
 * A fixed impedance device used for grounding.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class GroundingImpedance extends EarthFaultCompensator {

	/**
	 * Reactance of device.
	 */
	public Reactance x;

	public GroundingImpedance(){

	}
}//end GroundingImpedance