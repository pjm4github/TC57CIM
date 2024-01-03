package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.DateTime;

/**
 * A Transmission Right(TR) can be a chain of TR's or on individual.
 * 
 * When a transmission right is not a chain, this is formally the ETC/TOR
 * Entitlement for each ETC/TOR contract with the inclusion of CVR(Converted
 * Rights) as an ETC. This is the sum of all entitlements on all related
 * transmission interfaces for the same TR.
 * 
 * When TR is a chain, its entitlement is the minimum of all entitlements for the
 * individual TRs in the chain.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class TREntitlement {

	/**
	 * The entitlement
	 */
	public Float entitlement;
	/**
	 * Operating date and hour when the entitlement applies
	 */
	public DateTime startOperatingDate;

	public TREntitlement(){

	}
}//end TREntitlement