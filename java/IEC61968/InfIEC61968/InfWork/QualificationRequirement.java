package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61968.InfIEC61968.InfAssets.Specification;

/**
 * Certain skills are required and must be certified in order for a person
 * (typically a member of a crew) to be qualified to work on types of equipment.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class QualificationRequirement extends WorkIdentifiedObject {

	/**
	 * Qualification identifier.
	 */
	public String qualificationID;
	public Specification Specifications;

	public QualificationRequirement(){

	}
}//end QualificationRequirement