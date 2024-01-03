package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.ReferenceData.ContractRight;

/**
 * This is formally called the branch group ETC/TOR entitlement with the inclusion
 * of CVR as ETC. This could be also used to represent the TR entitlement on a
 * POR/POD.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class TransmissionInterfaceRightEntitlement {

	/**
	 * the entitlement
	 */
	public Float entitlement;
	/**
	 * point of delivery
	 */
	public String POD;
	/**
	 * point of receipt
	 */
	public String POR;
	/**
	 * Operating date and hour when the entitlement applies
	 */
	public DateTime startOperatingDate;
	public ContractRight ContractRight;

	public TransmissionInterfaceRightEntitlement(){

	}
}//end TransmissionInterfaceRightEntitlement