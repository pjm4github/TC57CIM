package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.CostPerVolume;

/**
 * A generating unit whose prime mover is a hydraulic turbine (e.g., Francis,
 * Pelton, Kaplan).
 * @created 02-Jan-2024 10:55:18 PM
 */
public class HydroGeneratingUnit extends GeneratingUnit {

	/**
	 * Energy conversion capability for generating.
	 */
	public HydroEnergyConversionKind energyConversionCapability;
	/**
	 * The equivalent cost of water that drives the hydro turbine.
	 */
	public CostPerVolume hydroUnitWaterCost;
	/**
	 * A hydro generating unit has a tailbay loss curve.
	 */
	public TailbayLossCurve TailbayLossCurve;
	/**
	 * A hydro generating unit has an efficiency curve.
	 */
	public HydroGeneratingEfficiencyCurve HydroGeneratingEfficiencyCurves;
	/**
	 * A hydro generating unit has a penstock loss curve.
	 */
	public PenstockLossCurve PenstockLossCurve;

	public HydroGeneratingUnit(){

	}
}//end HydroGeneratingUnit