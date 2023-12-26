package IEC61968.Metering;

import IEC61970.Base.Domain.Integer;

/**
 * PAN action/command used to issue pricing information to a PAN device.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class PanPricing extends EndDeviceAction {

	/**
	 * Unique identifier for the commodity provider.
	 */
	public Integer providerID;
	/**
	 * All pricing details issued by this PAN pricing command/action.
	 */
	public PanPricingDetail PanPricingDetails;

	public PanPricing(){

	}
}//end PanPricing