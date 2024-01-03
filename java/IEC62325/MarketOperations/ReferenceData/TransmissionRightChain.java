package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * Allows chaining of TransmissionContractRights. Many individual contract rights
 * can be included in the definition of a TransmissionRightChain. A
 * TransmissionRightChain is also defined as a TransmissionContractRight itself.
 * @created 03-Jan-2024 2:15:34 PM
 */
public class TransmissionRightChain extends IdentifiedObject {

	public ContractRight Ind_ContractRight;
	public ContractRight Chain_ContractRight;

	public TransmissionRightChain(){

	}
}//end TransmissionRightChain