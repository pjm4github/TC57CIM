///////////////////////////////////////////////////////////
//  ElectronicAddress.h
//  Implementation of the Class ElectronicAddress
//  Created on:      25-Dec-2023 8:45:21 PM
///////////////////////////////////////////////////////////

#if !defined(EA_16E04AA3_C9C6_4272_9BB7_37C1D25DFCEA__INCLUDED_)
#define EA_16E04AA3_C9C6_4272_9BB7_37C1D25DFCEA__INCLUDED_

#include "String.h"

/**
 * Electronic address information.
 */
class ElectronicAddress
{

public:
	ElectronicAddress();
	/**
	 * Primary email address.
	 */
	String email1;
	/**
	 * Alternate email address.
	 */
	String email2;
	/**
	 * Address on local area network.
	 */
	String lan;
	/**
	 * MAC (Media Access Control) address.
	 */
	String mac;
	/**
	 * Password needed to log in.
	 */
	String password;
	/**
	 * Radio address.
	 */
	String radio;
	/**
	 * User ID needed to log in, which can be for an individual person, an
	 * organisation, a location, etc.
	 */
	String userID;
	/**
	 * World wide web address.
	 */
	String web;

};
#endif // !defined(EA_16E04AA3_C9C6_4272_9BB7_37C1D25DFCEA__INCLUDED_)
