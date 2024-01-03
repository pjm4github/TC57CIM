package IEC61968.InfIEC61968.InfCommon;

import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Domain.DateTime;
import IEC61968.InfIEC61968.InfWork.QualificationRequirement;
import IEC61968.Common.Document;

/**
 * Proficiency level of a craft, which is required to operate or maintain a
 * particular type of asset and/or perform certain types of work.
 * @created 29-Dec-2023 6:03:20 PM
 */
public class Skill extends Document {

	/**
	 * Interval between the certification and its expiry.
	 */
	public DateTimeInterval certificationPeriod;
	/**
	 * Date and time the skill became effective.
	 */
	public DateTime effectiveDateTime;
	/**
	 * Level of skill for a Craft.
	 */
	public SkillLevelKind level;
	public Craft Crafts;
	public QualificationRequirement QualificationRequirements;

	public Skill(){

	}
}//end Skill