package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC62325.MarketOperations.ParticipantInterfaces.TransactionBid;

/**
 * A transmission reservation is obtained from the OASIS system to reserve
 * transmission for a specified time period, transmission path and transmission
 * product.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class TransmissionReservation {

	public TransactionBid TransactionBid;
	public EnergyTransaction EnergyTransaction;

	public TransmissionReservation(){

	}
}//end TransmissionReservation