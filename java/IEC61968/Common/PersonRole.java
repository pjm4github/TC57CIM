package IEC61968.Common;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class PersonRole extends IdentifiedObject {

	/**
	 * All appointments for this person.
	 */
	public Appointment Appointments;
	/**
	 * All configuration events created for this person role.
	 */
	public ConfigurationEvent ConfigurationEvents;

	public PersonRole(){

	}
}//end PersonRole