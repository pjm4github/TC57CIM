package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.Curve;

/**
 * The amount of fuel of a given type which is allocated for consumption over a
 * specified period of time.
 * @created 02-Jan-2024 10:53:25 PM
 */
public class FuelAllocationSchedule extends Curve {

	/**
	 * The end time and date of the fuel allocation schedule.
	 */
	public DateTime fuelAllocationEndDate;
	/**
	 * The start time and date of the fuel allocation schedule.
	 */
	public DateTime fuelAllocationStartDate;
	/**
	 * The type of fuel, which also indicates the corresponding measurement unit.
	 */
	public FuelType fuelType;
	/**
	 * The maximum amount fuel that is allocated for consumption for the scheduled
	 * time period.
	 */
	public Float maxFuelAllocation;
	/**
	 * The minimum amount fuel that is allocated for consumption for the scheduled
	 * time period, e.g., based on a "take-or-pay" contract.
	 */
	public Float minFuelAllocation;

	public FuelAllocationSchedule(){

	}
}//end FuelAllocationSchedule