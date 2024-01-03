package IEC61968.Customers;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61968.InfIEC61968.InfCustomers.StandardIndustryCode;
import IEC61968.PaymentMetering.AuxiliaryAgreement;
import IEC61968.Metering.UsagePoint;
import IEC61968.Common.Agreement;

/**
 * Agreement between the customer and the service supplier to pay for service at a
 * specific service location. It records certain billing information about the
 * type of service provided at the service location and is used during charge
 * creation to determine the type of service.
 * @created 03-Jan-2024 12:17:07 PM
 */
public class CustomerAgreement extends Agreement {

	/**
	 * If true, the customer is a pre-pay customer for the specified service.
	 */
	public Boolean isPrePay;
	/**
	 * Load management code.
	 */
	public String loadMgmt;
	/**
	 * Final date and time the service will be billed to the previous customer.
	 */
	public DateTime shutOffDateTime;
	/**
	 * All service locations regulated by this customer agreement.
	 */
	public ServiceLocation ServiceLocations;
	public StandardIndustryCode StandardIndustryCode;
	/**
	 * All (non-service related) auxiliary agreements that refer to this customer
	 * agreement.
	 */
	public AuxiliaryAgreement AuxiliaryAgreements;
	/**
	 * All pricing structures applicable to this customer agreement.
	 */
	public PricingStructure PricingStructures;
	/**
	 * All service delivery points regulated by this customer agreement.
	 */
	public UsagePoint UsagePoints;
	/**
	 * Service category for this agreement.
	 */
	public ServiceCategory ServiceCategory;

	public CustomerAgreement(){

	}
}//end CustomerAgreement