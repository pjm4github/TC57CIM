///////////////////////////////////////////////////////////
//  ServiceCategory.h
//  Implementation of the Class ServiceCategory
//  Created on:      25-Dec-2023 8:45:24 PM
///////////////////////////////////////////////////////////

#if !defined(EA_46DD2695_85C3_4e99_AF30_FCE77788D825__INCLUDED_)
#define EA_46DD2695_85C3_4e99_AF30_FCE77788D825__INCLUDED_

#include "IEC61968\Customers\ServiceKind.java"
#include "IdentifiedObject.py"
#include "PricingStructure.h"
#include "ConfigurationEvent.py"

/**
 * Category of service provided to the customer.
 */
class ServiceCategory : public IdentifiedObject
{

public:
	ServiceCategory();
	/**
	 * Kind of service.
	 */
	ServiceKind kind;
	/**
	 * All pricing structures applicable to this service category.
	 */
	PricingStructure *PricingStructures;
	/**
	 * All configuration events created for this service category.
	 */
	ConfigurationEvent *ConfigurationEvents;

};
#endif // !defined(EA_46DD2695_85C3_4e99_AF30_FCE77788D825__INCLUDED_)
