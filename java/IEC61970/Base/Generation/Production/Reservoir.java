package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.Volume;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.WaterLevel;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Length;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * A water storage facility within a hydro system, including: ponds, lakes,
 * lagoons, and rivers. The storage is usually behind some type of dam.
 * @created 02-Jan-2024 10:57:32 PM
 */
public class Reservoir extends PowerSystemResource {

	/**
	 * Storage volume between the full supply level and the normal minimum operating
	 * level.
	 */
	public Volume activeStorageCapacity;
	/**
	 * The reservoir's energy storage rating in energy for given head conditions.
	 */
	public Float energyStorageRating;
	/**
	 * Full supply level, above which water will spill. This can be the spillway crest
	 * level or the top of closed gates.
	 */
	public WaterLevel fullSupplyLevel;
	/**
	 * Total capacity of reservoir.
	 */
	public Volume grossCapacity;
	/**
	 * Normal minimum operating level below which the penstocks will draw air.
	 */
	public WaterLevel normalMinOperateLevel;
	/**
	 * River outlet works for riparian right releases or other purposes.
	 */
	public String riverOutletWorks;
	/**
	 * The spillway water travel delay to the next downstream reservoir.
	 */
	public Seconds spillTravelDelay;
	/**
	 * The flow capacity of the spillway in cubic meters per second.
	 */
	public Float spillwayCapacity;
	/**
	 * The length of the spillway crest.
	 */
	public Length spillwayCrestLength;
	/**
	 * Spillway crest level above which water will spill.
	 */
	public WaterLevel spillwayCrestLevel;
	/**
	 * Type of spillway gate, including parameters.
	 */
	public String spillWayGateType;
	/**
	 * A reservoir may spill into a downstream reservoir.
	 */
	public Reservoir SpillsIntoReservoirs;
	/**
	 * A reservoir may have a level versus volume relationship.
	 */
	public LevelVsVolumeCurve LevelVsVolumeCurves;
	/**
	 * A reservoir may have a "natural" inflow forecast.
	 */
	public InflowForecast InflowForecasts;
	/**
	 * A reservoir may have a water level target schedule.
	 */
	public TargetLevelSchedule TargetLevelSchedule;

	public Reservoir(){

	}
}//end Reservoir