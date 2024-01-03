///////////////////////////////////////////////////////////
//  MarketPerson.h
//  Implementation of the Class MarketPerson
//  Created on:      03-Jan-2024 2:15:34 PM
///////////////////////////////////////////////////////////

#if !defined(EA_6136B286_E139_4e0f_935C_81759CEB0A8B__INCLUDED_)
#define EA_6136B286_E139_4e0f_935C_81759CEB0A8B__INCLUDED_

#include "java\IEC61970\Base\Domain\IEC61970\Base\Domain\String.java"
#include "java\IEC61968\Common\ElectronicAddress.java"
#include "IEC61968\Common\TelephoneNumber.java"
#include "java\IEC61968\Common\Status.java"
#include "java\IEC61970\Base\Core\IdentifiedObject.java"
#include "MarketSkill.h"

/**
 * General purpose information for name and other information to contact people.
 */
class MarketPerson : public IdentifiedObject
{

public:
	MarketPerson();
	/**
	 * Category of this person relative to utility operations, classified according to
	 * the utility's corporate standards and practices. Examples include employee,
	 * contractor, agent, not affiliated, etc.
	 * This field is not used to indicate whether this person is a customer of the
	 * utility. Often an employee or contractor is also a customer. Customer
	 * information is gained with relationship to Organisation and CustomerData. In
	 * similar fashion, this field does not indicate the various roles this person may
	 * fill as part of utility operations.
	 */
	String category;
	/**
	 * Alternate Electronic address.
	 */
	ElectronicAddress electronicAddressAlternate;
	/**
	 * Primary Electronic address.
	 */
	ElectronicAddress electronicAddressPrimary;
	/**
	 * Person's first name.
	 */
	String firstName;
	/**
	 * Unique identifier for person relative to its governing authority, for example a
	 * federal tax identifier (such as a Social Security number in the United States).
	 */
	String governmentID;
	/**
	 * Landline phone number.
	 */
	TelephoneNumber landlinePhone;
	/**
	 * Person's last (family, sir) name.
	 */
	String lastName;
	/**
	 * Middle name(s) or initial(s).
	 */
	String mName;
	/**
	 * Mobile phone number.
	 */
	TelephoneNumber mobilePhone;
	/**
	 * A prefix or title for the person's name, such as Miss, Mister, Doctor, etc.
	 */
	String prefix;
	/**
	 * Special service needs for the person (contact) are described; examples include
	 * life support, etc.
	 */
	String specialNeed;
	Status status;
	/**
	 * A suffix for the person's name, such as II, III, etc.
	 */
	String suffix;
	/**
	 * The user name for the person; required to log in.
	 */
	String userID;
	MarketSkill *MarketSkills;

};
#endif // !defined(EA_6136B286_E139_4e0f_935C_81759CEB0A8B__INCLUDED_)
