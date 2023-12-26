///////////////////////////////////////////////////////////
//  CustomerAgreement.h
//  Implementation of the Class CustomerAgreement
//  Created on:      25-Dec-2023 8:45:20 PM
///////////////////////////////////////////////////////////

#if !defined(EA_0C51235D_4E76_456a_AA58_B23D4C981080__INCLUDED_)
#define EA_0C51235D_4E76_456a_AA58_B23D4C981080__INCLUDED_

#include "Boolean.h"
#include "String.h"
#include "DateTime.py"
#include "ServiceLocation.h"
#include "StandardIndustryCode.h"
#include "IEC61968\PaymentMetering\AuxiliaryAgreement.java"
#include "PricingStructure.h"
#include "UsagePoint.h"
#include "ServiceCategory.h"
#include "IEC61968\Common\Agreement.java"

/**
 * Agreement between the customer and the service supplier to pay for service at a
 * specific service location. It records certain billing information about the
 * type of service provided at the service location and is used during charge
 * creation to determine the type of service.
 */
class CustomerAgreement : public Agreement
{

public:
	CustomerAgreement();
	/**
	 * If true, the customer is a pre-pay customer for the specified service.
	 */
	Boolean isPrePay;
	/**
	 * Load management code.
	 */
	String loadMgmt;
	/**
	 * Final date and time the service will be billed to the previous customer.
	 */
	DateTime shutOffDateTime;
	/**
	 * All service locations regulated by this customer agreement.
	 */
	ServiceLocation *ServiceLocations;
	StandardIndustryCode *StandardIndustryCode;
	/**
	 * All (non-service related) auxiliary agreements that refer to this customer
	 * agreement.
	 */
	AuxiliaryAgreement *AuxiliaryAgreements;
	/**
	 * All pricing structures applicable to this customer agreement.
	 */
	PricingStructure *PricingStructures;
	/**
	 * All service delivery points regulated by this customer agreement.
	 */
	UsagePoint *UsagePoints;
	/**
	 * Service category for this agreement.
	 */
	ServiceCategory *ServiceCategory;

};
#endif // !defined(EA_0C51235D_4E76_456a_AA58_B23D4C981080__INCLUDED_)
