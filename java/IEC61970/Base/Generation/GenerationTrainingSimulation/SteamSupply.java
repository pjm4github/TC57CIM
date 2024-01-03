package IEC61970.Base.Generation.GenerationTrainingSimulation;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * Steam supply for steam turbine.
 * @created 02-Jan-2024 11:06:31 PM
 */
public class SteamSupply extends PowerSystemResource {

	/**
	 * Rating of steam supply.
	 */
	public Float steamSupplyRating;
	/**
	 * Steam turbines may have steam supplied by a steam supply.
	 */
	public SteamTurbine SteamTurbines;

	public SteamSupply(){

	}
}//end SteamSupply