package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.String;
import IEC61968.InfIEC61968.InfCommon.BankAccount;
import IEC61968.Metering.UsagePoint;
import IEC61968.Customers.CustomerAgreement;
import IEC61968.Common.OrganisationRole;

/**
 * Organisation that provides services to customers.
 * @created 25-Dec-2023 8:45:24 PM
 */
public class ServiceSupplier extends OrganisationRole {

	/**
	 * Unique transaction reference prefix number issued to an entity by the
	 * International Organization for Standardization for the purpose of tagging onto
	 * electronic financial transactions, as defined in ISO/IEC 7812-1 and ISO/IEC
	 * 7812-2.
	 */
	public String issuerIdentificationNumber;
	/**
	 * Kind of supplier.
	 */
	public SupplierKind kind;
	/**
	 * All BackAccounts this ServiceSupplier owns.
	 */
	public BankAccount BankAccounts;
	/**
	 * All usage points this service supplier utilises to deliver a service.
	 */
	public UsagePoint UsagePoints;
	/**
	 * All customer agreements of this service supplier.
	 */
	public CustomerAgreement CustomerAgreements;

	public ServiceSupplier(){

	}
}//end ServiceSupplier