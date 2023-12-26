package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.Equipment;

/**
 * A generating unit or battery or aggregation that connects to the AC network
 * using power electronics rather than rotating machines.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
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
}//end PowerElectronicsUnit