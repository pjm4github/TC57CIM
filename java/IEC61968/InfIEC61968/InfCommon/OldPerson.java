package IEC61968.InfIEC61968.InfCommon;

import IEC61968.Common.Status;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Meas.MeasurementValue;
import IEC61968.InfIEC61968.InfWork.LaborItem;
import IEC61968.Common.Person;

/**
 * General purpose information for name and other information to contact people.
 * @created 29-Dec-2023 6:01:52 PM
 */
public class OldPerson extends Person {

	public Status status;
	/**
	 * Utility-specific classification for this person, according to the utility's
	 * corporate standards and practices. Examples include employee, contractor, agent,
	 * not affiliated, etc.
	 * Note that this field is not used to indicate whether this person is a customer
	 * of the utility. Often an employee or contractor is also a customer. Customer
	 * information is gained with relationship to Organisation and CustomerData. In
	 * similar fashion, this field does not indicate the various roles this person may
	 * fill as part of utility operations.
	 */
	public String type;
	public MeasurementValue MeasurementValues;
	public ErpCompetency ErpCompetency;
	public LaborItem LaborItems;
	public ErpPersonnel ErpPersonnel;
	public Skill Skills;
	public PersonOrganisationRole OrganisationRoles;
	public PersonPropertyRole LandPropertyRoles;

	public OldPerson(){

	}
}//end OldPerson