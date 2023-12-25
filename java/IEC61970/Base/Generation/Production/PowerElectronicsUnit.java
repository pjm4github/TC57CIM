package TC57CIM.IEC61970.Base.Generation.Production;

import TC57CIM.IEC61970.Base.Domain.ActivePower;
import TC57CIM.IEC61970.Base.Core.Equipment;

/**
 * A generating unit or battery or aggregation that connects to the AC network
 * using power electronics rather than rotating machines.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class PowerElectronicsUnit extends Equipment {

	/**
	 * Maximum active power limit. This is the maximum (nameplate) limit for the unit.
	 */
	public ActivePower maxP;
	/**
	 * Minimum active power limit. This is the minimum (nameplate) limit for the unit.
	 */
	public ActivePower minP;

	public PowerElectronicsUnit(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}