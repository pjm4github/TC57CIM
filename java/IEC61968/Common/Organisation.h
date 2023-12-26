///////////////////////////////////////////////////////////
//  Organisation.h
//  Implementation of the Class Organisation
//  Created on:      25-Dec-2023 8:45:23 PM
///////////////////////////////////////////////////////////

#if !defined(EA_D4B1CE7A_C375_4d51_864B_40842B134D7D__INCLUDED_)
#define EA_D4B1CE7A_C375_4d51_864B_40842B134D7D__INCLUDED_

#include "ElectronicAddress.h"
#include "IEC61968\Common\TelephoneNumber.java"
#include "StreetAddress.h"
#include "IdentifiedObject.py"
#include "IEC61968\Common\ParentOrganization.java"

/**
 * Organisation that might have roles as utility, contractor, supplier,
 * manufacturer, customer, etc.
 */
class Organisation : public IdentifiedObject
{

public:
	Organisation();
	/**
	 * Electronic address.
	 */
	ElectronicAddress electronicAddress;
	/**
	 * Phone number.
	 */
	TelephoneNumber phone1;
	/**
	 * Additional phone number.
	 */
	TelephoneNumber phone2;
	/**
	 * Postal address, potentially different than 'streetAddress' (e.g., another city).
	 */
	StreetAddress postalAddress;
	/**
	 * Street address.
	 */
	StreetAddress streetAddress;
	/**
	 * Parent organisation of this organisation.
	 */
	ParentOrganization *ParentOrganisation;

};
#endif // !defined(EA_D4B1CE7A_C375_4d51_864B_40842B134D7D__INCLUDED_)
