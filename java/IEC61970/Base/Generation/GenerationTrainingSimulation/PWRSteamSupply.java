package IEC61970.Base.Generation.GenerationTrainingSimulation;

import IEC61970.Base.Domain.PU;

/**
 * Pressurized water reactor used as a steam supply to a steam turbine.
 * @created 02-Jan-2024 11:06:06 PM
 */
public class PWRSteamSupply extends SteamSupply {

	/**
	 * Cold leg feedback lag time constant.
	 */
	public PU coldLegFBLagTC;
	/**
	 * Cold leg feedback lead time constant.
	 */
	public PU coldLegFBLeadTC1;
	/**
	 * Cold leg feedback lead time constant.
	 */
	public PU coldLegFBLeadTC2;
	/**
	 * Cold leg feedback gain 1.
	 */
	public PU coldLegFG1;
	/**
	 * Cold leg feedback gain 2.
	 */
	public PU coldLegFG2;
	/**
	 * Cold leg lag time constant.
	 */
	public PU coldLegLagTC;
	/**
	 * Core heat transfer lag time constant.
	 */
	public PU coreHTLagTC1;
	/**
	 * Core heat transfer lag time constant.
	 */
	public PU coreHTLagTC2;
	/**
	 * Core neutronics effective time constant.
	 */
	public PU coreNeutronicsEffTC;
	/**
	 * Core neutronics and heat transfer.
	 */
	public PU coreNeutronicsHT;
	/**
	 * Feedback factor.
	 */
	public PU feedbackFactor;
	/**
	 * Hot leg lag time constant.
	 */
	public PU hotLegLagTC;
	/**
	 * Hot leg steam gain.
	 */
	public PU hotLegSteamGain;
	/**
	 * Hot leg to cold leg gain.
	 */
	public PU hotLegToColdLegGain;
	/**
	 * Pressure control gain.
	 */
	public PU pressureCG;
	/**
	 * Steam flow feedback gain.
	 */
	public PU steamFlowFG;
	/**
	 * Steam pressure drop lag time constant.
	 */
	public PU steamPressureDropLagTC;
	/**
	 * Steam pressure feedback gain.
	 */
	public PU steamPressureFG;
	/**
	 * Throttle pressure factor.
	 */
	public PU throttlePressureFactor;
	/**
	 * Throttle pressure setpoint.
	 */
	public PU throttlePressureSP;

	public PWRSteamSupply(){

	}
}//end PWRSteamSupply