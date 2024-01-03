package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * The fossil fuel consumed by the non-nuclear thermal generating unit.   For
 * example, coal, oil, gas, etc.   This a the specific fuels that the generating
 * unit can consume.
 * @created 02-Jan-2024 10:53:13 PM
 */
public class FossilFuel extends IdentifiedObject {

	/**
	 * The type of fossil fuel, such as coal, oil, or gas.
	 */
	public FuelType fossilFuelType;
	/**
	 * The cost in terms of heat value for the given type of fuel.
	 */
	public CostPerHeatUnit fuelCost;
	/**
	 * The cost of fuel used for economic dispatching which includes: fuel cost,
	 * transportation cost,  and incremental maintenance cost.
	 */
	public CostPerHeatUnit fuelDispatchCost;
	/**
	 * The efficiency factor for the fuel (per unit) in terms of the effective energy
	 * absorbed.
	 */
	public PU fuelEffFactor;
	/**
	 * Handling and processing cost associated with this fuel.
	 */
	public CostPerHeatUnit fuelHandlingCost;
	/**
	 * The amount of heat per weight (or volume) of the given type of fuel.
	 */
	public Float fuelHeatContent;
	/**
	 * Relative amount of the given type of fuel, when multiple fuels are being
	 * consumed.
	 */
	public PerCent fuelMixture;
	/**
	 * The fuel's fraction of pollution credit per unit of heat content.
	 */
	public PU fuelSulfur;
	/**
	 * The active power output level of the unit at which the given type of fuel is
	 * switched on. This fuel (e.g., oil) is sometimes used to supplement the base
	 * fuel (e.g., coal) at high active power output levels.
	 */
	public ActivePower highBreakpointP;
	/**
	 * The active power output level of the unit at which the given type of fuel is
	 * switched off. This fuel (e.g., oil) is sometimes used to stabilize the base
	 * fuel (e.g., coal) at low active power output levels.
	 */
	public ActivePower lowBreakpointP;
	/**
	 * A fuel allocation schedule must have a fossil fuel.
	 */
	public FuelAllocationSchedule FuelAllocationSchedules;
	/**
	 * A thermal generating unit may have one or more fossil fuels.
	 */
	public ThermalGeneratingUnit ThermalGeneratingUnit;

	public FossilFuel(){

	}
}//end FossilFuel