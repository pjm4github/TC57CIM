package IEC61968.Customers;

import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.Common.ConfigurationEvent;

/**
 * Category of service provided to the customer.
 * @created 03-Jan-2024 12:17:44 PM
 */
public class ServiceCategory extends IdentifiedObject {

	/**
	 * Kind of service.
	 */
	public ServiceKind kind;
	/**
	 * All pricing structures applicable to this service category.
	 */
	public PricingStructure PricingStructures;
	/**
	 * All configuration events created for this service category.
	 */
	public ConfigurationEvent ConfigurationEvents;

	public ServiceCategory(){

	}
}//end ServiceCategory