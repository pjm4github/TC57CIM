package IEC61970.Base.Generation.GenerationTrainingSimulation;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Integer;

/**
 * Fossil fueled boiler (e.g., coal, oil, gas).
 * @created 02-Jan-2024 11:05:29 PM
 */
public class FossilSteamSupply extends SteamSupply {

	/**
	 * Off nominal frequency effect on auxiliary real power. Per unit active power
	 * variation versus per unit frequency variation.
	 */
	public PU auxPowerVersusFrequency;
	/**
	 * Off nominal voltage effect on auxiliary real power. Per unit active power
	 * variation versus per unit voltage variation.
	 */
	public PU auxPowerVersusVoltage;
	/**
	 * The control mode of the boiler.
	 */
	public BoilerControlMode boilerControlMode;
	/**
	 * Active power error bias ratio.
	 */
	public Float controlErrorBiasP;
	/**
	 * Integral constant.
	 */
	public Float controlIC;
	/**
	 * Proportional constant.
	 */
	public Float controlPC;
	/**
	 * Pressure error bias ratio.
	 */
	public Float controlPEB;
	/**
	 * Pressure error deadband.
	 */
	public PU controlPED;
	/**
	 * Time constant.
	 */
	public Float controlTC;
	/**
	 * Feedwater integral gain ratio.
	 */
	public Float feedWaterIG;
	/**
	 * Feedwater proportional gain ratio.
	 */
	public Float feedWaterPG;
	/**
	 * Feedwater time constant rato.
	 */
	public Seconds feedWaterTC;
	/**
	 * Fuel demand limit.
	 */
	public PU fuelDemandLimit;
	/**
	 * Fuel delay.
	 */
	public Seconds fuelSupplyDelay;
	/**
	 * Fuel supply time constant.
	 */
	public Seconds fuelSupplyTC;
	/**
	 * Active power maximum error rate limit.
	 */
	public Float maxErrorRateP;
	/**
	 * Mechanical power sensor lag.
	 */
	public Seconds mechPowerSensorLag;
	/**
	 * Active power minimum error rate limit.
	 */
	public Float minErrorRateP;
	/**
	 * Pressure control derivative gain ratio.
	 */
	public Float pressureCtrlDG;
	/**
	 * Pressure control integral gain ratio.
	 */
	public Float pressureCtrlIG;
	/**
	 * Pressure control proportional gain ratio.
	 */
	public Float pressureCtrlPG;
	/**
	 * Pressure feedback indicator.
	 */
	public Integer pressureFeedback;
	/**
	 * Drum/primary superheater capacity.
	 */
	public Float superHeater1Capacity;
	/**
	 * Secondary superheater capacity.
	 */
	public Float superHeater2Capacity;
	/**
	 * Superheater pipe pressure drop constant.
	 */
	public Float superHeaterPipePD;
	/**
	 * Throttle pressure setpoint.
	 */
	public PU throttlePressureSP;

	public FossilSteamSupply(){

	}
}//end FossilSteamSupply