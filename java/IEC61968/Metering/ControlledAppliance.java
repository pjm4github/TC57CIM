package IEC61968.Metering;

import IEC61970.Base.Domain.Boolean;

/**
 * Appliance controlled with a PAN device control.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class ControlledAppliance {

	/**
	 * True if the appliance is an electric vehicle.
	 */
	public Boolean isElectricVehicle;
	/**
	 * True if the appliance is exterior lighting.
	 */
	public Boolean isExteriorLighting;
	/**
	 * True if the appliance is a generation system.
	 */
	public Boolean isGenerationSystem;
	/**
	 * True if the appliance is HVAC compressor or furnace.
	 */
	public Boolean isHvacCompressorOrFurnace;
	/**
	 * True if the appliance is interior lighting.
	 */
	public Boolean isInteriorLighting;
	/**
	 * True if the appliance is an irrigation pump.
	 */
	public Boolean isIrrigationPump;
	/**
	 * True if the appliance is managed commercial or industrial load.
	 */
	public Boolean isManagedCommercialIndustrialLoad;
	/**
	 * True if the appliance is a pool, pump, spa or jacuzzi.
	 */
	public Boolean isPoolPumpSpaJacuzzi;
	/**
	 * True if the appliance is a simple miscellaneous load.
	 */
	public Boolean isSimpleMiscLoad;
	/**
	 * True if the appliance is a smart appliance.
	 */
	public Boolean isSmartAppliance;
	/**
	 * True if the appliance is a stip or baseboard heater.
	 */
	public Boolean isStripAndBaseboardHeater;
	/**
	 * True if the appliance is a water heater.
	 */
	public Boolean isWaterHeater;

	public ControlledAppliance(){

	}
}//end ControlledAppliance