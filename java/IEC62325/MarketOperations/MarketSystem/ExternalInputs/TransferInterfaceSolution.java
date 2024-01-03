package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.ReferenceData.MktContingency;

/**
 * TNA Interface Definitions from OPF for VSA.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class TransferInterfaceSolution {

	/**
	 * The margin for the interface
	 */
	public Float interfaceMargin;
	/**
	 * Post Transfer MW for step
	 */
	public Float postTransferMW;
	/**
	 * Transfer Interface + Limit
	 * Attribute Usage: The absoloute of the maximum flow on the transfer interface.
	 * This is a positive MW value.
	 */
	public Float transferLimit;
	public MktContingency  MktContingencyA;
	public MktContingency MktContingencyB;
	public TransferInterface TransferInterface;

	public TransferInterfaceSolution(){

	}
}//end TransferInterfaceSolution