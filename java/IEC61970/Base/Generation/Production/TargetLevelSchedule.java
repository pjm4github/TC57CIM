package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.WaterLevel;
import IEC61970.Base.Core.Curve;

/**
 * Reservoir water level targets from advanced studies or "rule curves". Typically
 * in one hour increments for up to 10 days.
 * @created 02-Jan-2024 10:59:19 PM
 */
public class TargetLevelSchedule extends Curve {

	/**
	 * High target level limit, above which the reservoir operation will be penalized.
	 */
	public WaterLevel highLevelLimit;
	/**
	 * Low target level limit, below which the reservoir operation will be penalized.
	 */
	public WaterLevel lowLevelLimit;

	public TargetLevelSchedule(){

	}
}//end TargetLevelSchedule