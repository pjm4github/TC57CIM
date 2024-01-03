package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC62325.MarketOperations.MktDomain.SwitchStatusType;

/**
 * Optimal Power Flow or State Estimator Circuit Breaker Status.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class SwitchStatus {

	/**
	 * Circuit Breaker Status (closed or open) of the circuit breaker from the power
	 * flow.
	 */
	public SwitchStatusType switchStatus;
	public MktSwitch MktSwitch;

	public SwitchStatus(){

	}
}//end SwitchStatus