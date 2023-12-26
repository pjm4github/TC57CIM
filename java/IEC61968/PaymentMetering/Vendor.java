package IEC61968.PaymentMetering;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * The entity that owns the point of sale and contracts with the cashier to
 * receipt payments and vend tokens using the payment system. The vendor has a
 * private contract with and is managed by the merchant which is a type of
 * organisation. The vendor is accountable to the merchant for revenue collected,
 * and the merchant is in turn accountable to the supplier.
 * @created 25-Dec-2023 8:45:25 PM
 */
public class Vendor extends IdentifiedObject {

	/**
	 * All vendor shifts opened and owned by this vendor.
	 */
	public VendorShift VendorShifts;

	public Vendor(){

	}
}//end Vendor