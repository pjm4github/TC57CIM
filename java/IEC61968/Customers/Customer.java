package IEC61968.Customers;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Priority;
import IEC61968.Common.Status;
import IEC61970.Base.Domain.Boolean;
import IEC61968.Metering.EndDevice;
import IEC61968.InfIEC61968.InfCommon.OldPerson;
import IEC61968.Work.Work;
import IEC61968.Operations.OutagePlan;
import IEC61968.Common.OrganisationRole;

/**
 * Organisation receiving services from service supplier.
 * @updated 03-Jan-2024 12:16:45 PM
 */
public class Customer extends OrganisationRole {

	/**
	 * Kind of customer.
	 */
	public CustomerKind kind;
	/**
	 * Locale designating language to use in communications with this customer.
	 */
	public String locale;
	/**
	 * Priority of the customer.
	 */
	public Priority priority;
	/**
	 * (if applicable) Public utilities commission (PUC) identification number.
	 */
	public String pucNumber;
	/**
	 * True if customer organisation has special service needs such as life support,
	 * hospitals, etc.
	 */
	public String specialNeed;
	/**
	 * Status of this customer.
	 */
	public Status status;
	/**
	 * (use 'priority' instead) True if this is an important customer. Importance is
	 * for matters different than those in 'specialNeed' attribute.
	 */
	public Boolean vip;
	/**
	 * All end devices of this customer.
	 */
	public EndDevice EndDevices;
	public Customer Customer;
	/**
	 * All accounts of this customer.
	 */
	public CustomerAccount CustomerAccounts;
	public OldPerson ErpPersons;
	/**
	 * All agreements of this customer.
	 */
	public CustomerAgreement CustomerAgreements;
	/**
	 * All the works performed for this customer.
	 */
	public Work Works;
	/**
	 * The outage plan that identifies the customers that are affected.
	 */
	public OutagePlan OutagePlan;

	public Customer(){

	}
}//end Customer