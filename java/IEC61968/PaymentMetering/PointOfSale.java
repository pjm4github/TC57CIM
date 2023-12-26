package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Logical point where transactions take place with operational interaction
 * between cashier and the payment system; in certain cases the point of sale
 * interacts directly with the end customer, in which case the cashier might not
 * be a real person: for example a self-service kiosk or over the internet.
 * @created 25-Dec-2023 8:45:23 PM
 */
public class PointOfSale extends IdentifiedObject {

	/**
	 * Local description for where this point of sale is physically located.
	 */
	public String location;

	public PointOfSale(){

	}
}//end PointOfSale