package IEC62325.MarketOperations.MarketQualitySystem;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Float;

/**
 * Models Market clearing results in terms of price and MW values.
 * @created 03-Jan-2024 2:07:09 PM
 */
public class AllocationResultValues {

	/**
	 * "1" --  "Detail",
	 * "2" --  "Aggregate by Market service type", in which case, the
	 * "AllocationEnergyType" field will not be filled;
	 * "3" --  "Aggregate by "AllocationEnergyType", in which case "MarketServiceType"
	 * will not be filled.
	 */
	public String aggregateType;
	public Float allocationMwHour;
	public Float allocationPrice;
	public String energyTypeCode;
	/**
	 * Choices are:
	 * ME - Market Energy Capacity;
	 * SR - Spinning Reserve Capacity;
	 * NR - Non-Spinning Reserve Capacity;
	 * DAC - Day Ahead Capacity;
	 * DEC - Derate Capacity
	 */
	public String marketServiceType;

	public AllocationResultValues(){

	}
}//end AllocationResultValues