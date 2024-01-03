package IEC61970.Base.Generation.Production;


/**
 * A generating unit whose prime mover could be a steam turbine, combustion
 * turbine, or diesel engine.
 * @created 02-Jan-2024 10:59:32 PM
 */
public class ThermalGeneratingUnit extends GeneratingUnit {

	/**
	 * Operating and maintenance cost for the thermal unit.
	 */
	public CostPerHeatUnit oMCost;
	/**
	 * A thermal generating unit may have a heat rate curve.
	 */
	public HeatRateCurve HeatRateCurve;
	/**
	 * A thermal generating unit may have one or more fuel allocation schedules.
	 */
	public FuelAllocationSchedule FuelAllocationSchedules;
	/**
	 * A thermal generating unit may have a startup model.
	 */
	public StartupModel StartupModel;
	/**
	 * A thermal generating unit may have  one or more emission curves.
	 */
	public EmissionCurve EmissionCurves;
	/**
	 * A thermal generating unit may have a shutdown curve.
	 */
	public ShutdownCurve ShutdownCurve;
	/**
	 * A thermal generating unit may have an incremental heat rate curve.
	 */
	public IncrementalHeatRateCurve IncrementalHeatRateCurve;
	/**
	 * A thermal generating unit may have one or more emission allowance accounts.
	 */
	public EmissionAccount EmmissionAccounts;
	/**
	 * A thermal generating unit may have a heat input curve.
	 */
	public HeatInputCurve HeatInputCurve;

	public ThermalGeneratingUnit(){

	}
}//end ThermalGeneratingUnit