package IEC61968.PaymentMetering;

import IEC61968.Common.Agreement;

/**
 * A formal controlling contractual agreement between supplier and merchant, in
 * terms of which the merchant is authorised to vend tokens and receipt payments
 * on behalf of the supplier. The merchant is accountable to the supplier for
 * revenue collected at point of sale.
 * @created 25-Dec-2023 8:45:22 PM
 */
public class MerchantAgreement extends Agreement {

	/**
	 * All merchant accounts instantiated as a result of this merchant agreement.
	 */
	public MerchantAccount MerchantAccounts;

	public MerchantAgreement(){

	}
}//end MerchantAgreement