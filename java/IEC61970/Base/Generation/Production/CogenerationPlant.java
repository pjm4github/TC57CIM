package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * A set of thermal generating units for the production of electrical energy and
 * process steam (usually from the output of the steam turbines). The steam
 * sendout is typically used for industrial purposes or for municipal heating and
 * cooling.
 * @created 02-Jan-2024 10:51:55 PM
 */
public class CogenerationPlant extends PowerSystemResource {

	/**
	 * The high pressure steam sendout.
	 */
	public Float cogenHPSendoutRating;
	/**
	 * The high pressure steam rating.
	 */
	public Float cogenHPSteamRating;
	/**
	 * The low pressure steam sendout.
	 */
	public Float cogenLPSendoutRating;
	/**
	 * The low pressure steam rating.
	 */
	public Float cogenLPSteamRating;
	/**
	 * The rated output active power of the cogeneration plant.
	 */
	public ActivePower ratedP;
	/**
	 * A thermal generating unit may be a member of a cogeneration plant.
	 */
	public ThermalGeneratingUnit ThermalGeneratingUnits;
	/**
	 * A cogeneration plant has a steam sendout schedule.
	 */
	public SteamSendoutSchedule SteamSendoutSchedule;

	public CogenerationPlant(){

	}
}//end CogenerationPlant