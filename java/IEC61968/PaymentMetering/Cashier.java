package IEC61968.PaymentMetering;

import IEC61968.Common.ElectronicAddress;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * The operator of the point of sale for the duration of CashierShift. Cashier is
 * under the exclusive management control of Vendor.
 * @created 25-Dec-2023 8:45:19 PM
 */
public class Cashier extends IdentifiedObject {

	/**
	 * Electronic address.
	 */
	public ElectronicAddress electronicAddress;
	/**
	 * All shifts operated by this cashier.
	 */
	public CashierShift CashierShifts;

	public Cashier(){

	}
}//end Cashier