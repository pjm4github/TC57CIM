package IEC61970.Base.Generation.GenerationTrainingSimulation;

import IEC61970.Base.Domain.Float;

/**
 * The heat recovery system associated with combustion turbines in order to
 * produce steam for combined cycle plants.
 * @created 02-Jan-2024 11:05:44 PM
 */
public class HeatRecoveryBoiler extends FossilSteamSupply {

	/**
	 * The steam supply rating in kilopounds per hour, if dual pressure boiler.
	 */
	public Float steamSupplyRating2;
	/**
	 * A combustion turbine may have a heat recovery boiler for making steam.
	 */
	public CombustionTurbine CombustionTurbines;

	public HeatRecoveryBoiler(){

	}
}//end HeatRecoveryBoiler