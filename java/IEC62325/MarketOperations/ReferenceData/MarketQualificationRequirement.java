package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Certain skills are required and shall be certified in order for a person
 * (typically a member of a crew) to be qualified to work on types of equipment.
 * @created 28-Dec-2023 12:17:20 PM
 */
public class MarketQualificationRequirement extends IdentifiedObject {

	/**
	 * Effective date of the privilege, terminate date of the privilege, or effective
	 * date of the application for the organization
	 */
	public DateTime effectiveDate;
	/**
	 * This is the terminate date of the application for the organization
	 * The specific organization can no longer access the application as of the
	 * terminate date
	 */
	public DateTime expirationDate;
	/**
	 * Qualification identifier.
	 */
	public String qualificationID;
	/**
	 * The status of the privilege. Shows the status of the user's qualification.
	 * The current statuses are: 1=New, 2=Active, 3=Refused, 4=Terminated,
	 * 5=Withdrawn
	 * and it is subject to update.
	 */
	public Integer status;
	/**
	 * This is the name of the status of the qualification and is used to display the
	 * status of the user's or organization's status.
	 */
	public String statusType;

	public MarketQualificationRequirement(){

	}
}//end MarketQualificationRequirement