package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.Reactance;

/**
 * A fixed impedance device used for grounding.
 * @author kdemaree
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class GroundingImpedance extends EarthFaultCompensator {

	/**
	 * Reactance of device.
	 */
	public Reactance x;

	public GroundingImpedance(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}