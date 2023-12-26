package IEC61970.Base.DC;

import IEC61970.Base.Domain.Inductance;
import IEC61970.Base.Domain.Resistance;

/**
 * A ground within a DC system.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
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
}//end DCGround