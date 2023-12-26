package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Resistance;
import IEC61970.Base.Core.ConductingEquipment;

/**
 * A conducting equipment used to represent a connection to ground which is
 * typically used to compensate earth faults..   An earth fault compensator device
 * modeled with a single terminal implies a second terminal solidly connected to
 * ground.  If two terminals are modeled, the ground is not assumed and normal
 * connection rules apply.
 * @author namstutz
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class EarthFaultCompensator extends ConductingEquipment {

	/**
	 * Nominal resistance of device.
	 */
	public Resistance r;

	public EarthFaultCompensator(){

	}
}//end EarthFaultCompensator