package IEC61968.Common;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * General purpose information for name and other information to contact people.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class Person extends IdentifiedObject {

	/**
	 * Electronic address.
	 */
	public ElectronicAddress electronicAddress;
	/**
	 * Person's first name.
	 */
	public String firstName;
	/**
	 * Landline phone number.
	 */
	public TelephoneNumber landlinePhone;
	/**
	 * Person's last (family, sir) name.
	 */
	public String lastName;
	/**
	 * Middle name(s) or initial(s).
	 */
	public String mName;
	/**
	 * Mobile phone number.
	 */
	public TelephoneNumber mobilePhone;
	/**
	 * A prefix or title for the person's name, such as Miss, Mister, Doctor, etc.
	 */
	public String prefix;
	/**
	 * Special service needs for the person (contact) are described; examples include
	 * life support, etc.
	 */
	public String specialNeed;
	/**
	 * A suffix for the person's name, such as II, III, etc.
	 */
	public String suffix;
	/**
	 * All roles of this person.
	 */
	public PersonRole Roles;

	public Person(){

	}
}//end Person