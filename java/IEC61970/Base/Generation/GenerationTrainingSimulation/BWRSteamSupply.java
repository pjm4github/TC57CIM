package IEC61970.Base.Generation.GenerationTrainingSimulation;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Float;

/**
 * Boiling water reactor used as a steam supply to a steam turbine.
 * @created 02-Jan-2024 11:04:03 PM
 */
public class BWRSteamSupply extends SteamSupply {

	/**
	 * High power limit.
	 */
	public PU highPowerLimit;
	/**
	 * In-core thermal time constant.
	 */
	public Seconds inCoreThermalTC;
	/**
	 * Integral gain.
	 */
	public Float integralGain;
	/**
	 * Initial lower limit.
	 */
	public PU lowerLimit;
	/**
	 * Low power limit.
	 */
	public PU lowPowerLimit;
	/**
	 * Pressure limit.
	 */
	public PU pressureLimit;
	/**
	 * Pressure setpoint gain adjuster.
	 */
	public Float pressureSetpointGA;
	/**
	 * Pressure setpoint time constant.
	 */
	public Seconds pressureSetpointTC1;
	/**
	 * Pressure setpoint time constant.
	 */
	public Seconds pressureSetpointTC2;
	/**
	 * Proportional gain.
	 */
	public Float proportionalGain;
	/**
	 * Coefficient for modeling the effect of off-nominal frequency and voltage on
	 * recirculation and core flow, which affects the BWR power output.
	 */
	public PU rfAux1;
	/**
	 * Coefficient for modeling the effect of off-nominal frequency and voltage on
	 * recirculation and core flow, which affects the BWR power output.
	 */
	public PU rfAux2;
	/**
	 * Coefficient for modeling the effect of off-nominal frequency and voltage on
	 * recirculation and core flow, which affects the BWR power output.
	 */
	public PU rfAux3;
	/**
	 * Coefficient for modeling the effect of off-nominal frequency and voltage on
	 * recirculation and core flow, which affects the BWR power output.
	 */
	public PU rfAux4;
	/**
	 * Coefficient for modeling the effect of off-nominal frequency and voltage on
	 * recirculation and core flow, which affects the BWR power output.
	 */
	public PU rfAux5;
	/**
	 * Coefficient for modeling the effect of off-nominal frequency and voltage on
	 * recirculation and core flow, which affects the BWR power output.
	 */
	public PU rfAux6;
	/**
	 * Coefficient for modeling the effect of off-nominal frequency and voltage on
	 * recirculation and core flow, which affects the BWR power output.
	 */
	public PU rfAux7;
	/**
	 * Coefficient for modeling the effect of off-nominal frequency and voltage on
	 * recirculation and core flow, which affects the BWR power output.
	 */
	public PU rfAux8;
	/**
	 * Rod pattern.
	 */
	public PU rodPattern;
	/**
	 * Constant associated with rod pattern.
	 */
	public Float rodPatternConstant;
	/**
	 * Initial upper limit.
	 */
	public PU upperLimit;

	public BWRSteamSupply(){

	}
}//end BWRSteamSupply