package TC57CIM.IEC61970.Base.DC;

import TC57CIM.IEC61970.Base.Domain.Inductance;
import TC57CIM.IEC61970.Base.Domain.Resistance;

/**
 * A ground within a DC system.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class DCGround extends DCConductingEquipment {

	/**
	 * Inductance to ground.
	 */
	public Inductance inductance;
	/**
	 * Resistance to ground.
	 */
	public Resistance r;

	public DCGround(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}