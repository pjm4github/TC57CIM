///////////////////////////////////////////////////////////
//  StreetAddress.h
//  Implementation of the Class StreetAddress
//  Created on:      25-Dec-2023 8:45:24 PM
///////////////////////////////////////////////////////////

#if !defined(EA_15920DD7_6A1D_4b44_AEBA_042755DA21CD__INCLUDED_)
#define EA_15920DD7_6A1D_4b44_AEBA_042755DA21CD__INCLUDED_

#include "String.h"
#include "Status.py"
#include "IEC61968\Common\StreetDetail.java"
#include "IEC61968\Common\TownDetail.java"

/**
 * General purpose street and postal address information.
 */
class StreetAddress
{

public:
	StreetAddress();
	/**
	 * Post office box.
	 */
	String poBox;
	/**
	 * Postal code for the address.
	 */
	String postalCode;
	/**
	 * Status of this address.
	 */
	Status status;
	/**
	 * Street detail.
	 */
	StreetDetail streetDetail;
	/**
	 * Town detail.
	 */
	TownDetail townDetail;

};
#endif // !defined(EA_15920DD7_6A1D_4b44_AEBA_042755DA21CD__INCLUDED_)
