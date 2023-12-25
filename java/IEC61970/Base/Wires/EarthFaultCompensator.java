package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.Resistance;
import TC57CIM.IEC61970.Base.Core.ConductingEquipment;

/**
 * A conducting equipment used to represent a connection to ground which is
 * typically used to compensate earth faults..   An earth fault compensator device
 * modeled with a single terminal implies a second terminal solidly connected to
 * ground.  If two terminals are modeled, the ground is not assumed and normal
 * connection rules apply.
 * @author namstutz
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class EarthFaultCompensator extends ConductingEquipment {

	/**
	 * Nominal resistance of device.
	 */
	public Resistance r;

	public EarthFaultCompensator(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}