package IEC61968.InfIEC61968.InfCustomers;

import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.String;
import IEC61968.Common.Document;

/**
 * A service guarantee, often imposed by a regulator, defines conditions that, if
 * not satisfied, will result in the utility making a monetary payment to the
 * customer. Note that guarantee's identifier is in the 'name' attribute and the
 * status of the guarantee is in the 'Status.status' attribute.
 * Example service requirements include:
 * 1) If power is not restored within 24 hours, customers can claim $50 for
 * residential customers or $100 for commercial and industrial customers. In
 * addition for each extra period of 12 hours the customer's supply has not been
 * activated, the customer can claim $25.
 * 2) If a customer has a question about their electricity bill, the utility will
 * investigate and respond to the inquiry within 15 working days. If utility fails
 * to meet its guarantee, utility will automatically pay the customer $50.
 * @created 29-Dec-2023 9:25:49 PM
 */
public class ServiceGuarantee extends Document {

	/**
	 * Period in which this service guantee applies.
	 */
	public DateTimeInterval applicationPeriod;
	/**
	 * True if utility must autmatically pay the specified amount whenever the
	 * condition is not satisified, otherwise customer must make a claim to receive
	 * payment.
	 */
	public Boolean automaticPay;
	/**
	 * Amount to be paid by the service provider to the customer for each violation of
	 * the 'serviceRequirement'.
	 */
	public Money payAmount;
	/**
	 * Explanation of the requirement and conditions for satisfying it.
	 */
	public String serviceRequirement;

	public ServiceGuarantee(){

	}
}//end ServiceGuarantee