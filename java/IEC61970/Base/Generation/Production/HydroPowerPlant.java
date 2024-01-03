package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.VolumeFlowRate;
import IEC61970.Base.Domain.Length;
import IEC61970.Base.Domain.WaterLevel;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * A hydro power station which can generate or pump. When generating, the
 * generator turbines receive water from an upper reservoir. When pumping, the
 * pumps receive their water from a lower reservoir.
 * @created 02-Jan-2024 10:55:30 PM
 */
public class HydroPowerPlant extends PowerSystemResource {

	/**
	 * Water travel delay from tailbay to next downstream hydro power station.
	 */
	public Seconds dischargeTravelDelay;
	/**
	 * The hydro plant's generating rating active power for rated head conditions.
	 */
	public ActivePower genRatedP;
	/**
	 * The type of hydro power plant water storage.
	 */
	public HydroPlantStorageKind hydroPlantStorageType;
	/**
	 * Type and configuration of hydro plant penstock(s).
	 */
	public String penstockType;
	/**
	 * Total plant discharge capacity.
	 */
	public VolumeFlowRate plantDischargeCapacity;
	/**
	 * The plant's rated gross head.
	 */
	public Length plantRatedHead;
	/**
	 * The hydro plant's pumping rating active power for rated head conditions.
	 */
	public ActivePower pumpRatedP;
	/**
	 * A code describing the type (or absence) of surge tank that is associated with
	 * the hydro power plant.
	 */
	public String surgeTankCode;
	/**
	 * The level at which the surge tank spills.
	 */
	public WaterLevel surgeTankCrestLevel;
	/**
	 * The hydro pump may be a member of a pumped storage plant or a pump for
	 * distributing water.
	 */
	public HydroPump HydroPumps;
	/**
	 * Generators discharge water to or pumps are supplied water from a downstream
	 * reservoir.
	 */
	public Reservoir Reservoir;
	/**
	 * Generators are supplied water from or pumps discharge water to an upstream
	 * reservoir.
	 */
	public Reservoir GenSourcePumpDischargeReservoir;
	/**
	 * The hydro generating unit belongs to a hydro power plant.
	 */
	public HydroGeneratingUnit HydroGeneratingUnits;

	public HydroPowerPlant(){

	}
}//end HydroPowerPlant