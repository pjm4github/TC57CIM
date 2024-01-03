package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * A set of combustion turbines and steam turbines where the exhaust heat from the
 * combustion turbines is recovered to make steam for the steam turbines,
 * resulting in greater overall plant efficiency.
 * @created 02-Jan-2024 10:52:09 PM
 */
public class CombinedCyclePlant extends PowerSystemResource {

	/**
	 * The combined cycle plant's active power output rating.
	 */
	public ActivePower combCyclePlantRating;
	/**
	 * A thermal generating unit may be a member of a combined cycle plant.
	 */
	public ThermalGeneratingUnit ThermalGeneratingUnits;

	public CombinedCyclePlant(){

	}
}//end CombinedCyclePlant