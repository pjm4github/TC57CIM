package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.MarketOpCommon.MktUserAttribute;

/**
 * Charge Group is the grouping of Charge Types for settlement invoicing purpose.
 * Examples such as Ancillary Services, Interests, etc.
 * @created 28-Dec-2023 5:20:24 PM
 */
public class ChargeGroup extends IdentifiedObject {

	public DateTime effectiveDate;
	public String marketCode;
	public DateTime terminationDate;
	/**
	 * A ChargeGroup instance can have relationships with other ChargeGroup instances.
	 */
	public ChargeGroup ChargeGroupParent;
	public MktUserAttribute MktUserAttribute;

	public ChargeGroup(){

	}
}//end ChargeGroup