package IEC62325.InfIEC62325.InfFinancial;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransmissionPath;

/**
 * 
 * @created 03-Jan-2024 1:52:02 PM
 */
public class TransmissionProduct extends IdentifiedObject {

	/**
	 * Type of the transmission product. This could be a transmission service class
	 * (firm, total transmission capability, or non-firm), transmission service period
	 * (on-peak, full-period, off-peak), transmission service increments (yearly
	 * extended, hourly fixed, monthly sliding, etc.), transmission service type
	 * (network, available transmission capability, or point-to-point, or a
	 * transmission service window (fixed hourly, sliding weekly, extended monthly,
	 * etc.).
	 */
	public String transmissionProductType;
	/**
	 * A TransmissionProvider offers a TransmissionProduct.
	 */
	public TransmissionProvider TransmissionProvider;
	/**
	 * A transmission product is located on a transmission path.
	 */
	public TransmissionPath LocationFor;

	public TransmissionProduct(){

	}
}//end TransmissionProduct