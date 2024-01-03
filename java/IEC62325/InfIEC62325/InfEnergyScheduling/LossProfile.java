package IEC62325.InfIEC62325.InfEnergyScheduling;

import IEC62325.InfIEC62325.InfFinancial.TransmissionProvider;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.Profile;

/**
 * LossProfile is associated with an EnerrgyTransaction and must be completely
 * contained within the time frame of the EnergyProfile associated with this
 * EnergyTransaction.
 * @created 03-Jan-2024 1:49:41 PM
 */
public class LossProfile extends Profile {

	/**
	 * Part of the LossProfile for an EnergyTransaction may be a loss for a
	 * TransmissionProvider. If so, the TransmissionProvider must be one of the
	 * participating entities in the EnergyTransaction.
	 */
	public TransmissionProvider HasLoss_;

	public LossProfile(){

	}
}//end LossProfile