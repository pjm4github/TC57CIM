package IEC61970.Base.Generation.GenerationTrainingSimulation;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.RotationSpeed;
import IEC61970.Base.Domain.Seconds;

/**
 * A water driven prime mover. Typical turbine types are: Francis, Kaplan, and
 * Pelton.
 * @created 02-Jan-2024 11:05:55 PM
 */
public class HydroTurbine extends PrimeMover {

	/**
	 * Gate rate limit.
	 */
	public Float gateRateLimit;
	/**
	 * Gate upper limit.
	 */
	public PU gateUpperLimit;
	/**
	 * Maximum efficiency active power at maximum head conditions.
	 */
	public ActivePower maxHeadMaxP;
	/**
	 * Maximum efficiency active power at minimum head conditions.
	 */
	public ActivePower minHeadMaxP;
	/**
	 * Rated speed in number of revolutions.
	 */
	public RotationSpeed speedRating;
	/**
	 * Speed regulation.
	 */
	public PU speedRegulation;
	/**
	 * Transient droop time constant.
	 */
	public Seconds transientDroopTime;
	/**
	 * Transient regulation.
	 */
	public PU transientRegulation;
	/**
	 * Rated turbine active power.
	 */
	public ActivePower turbineRating;
	/**
	 * Type of turbine.
	 */
	public TurbineType turbineType;
	/**
	 * Water starting time.
	 */
	public Seconds waterStartingTime;

	public HydroTurbine(){

	}
}//end HydroTurbine