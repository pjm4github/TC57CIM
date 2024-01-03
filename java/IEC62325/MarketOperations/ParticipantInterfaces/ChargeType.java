package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61968.Common.Document;
import IEC62325.MarketOperations.MarketOpCommon.MktUserAttribute;

/**
 * Charge Type is the basic level configuration for settlement to process specific
 * charges for invoicing purpose. Examples such as: Day Ahead Spinning Reserve
 * Default Invoice Interest Charge, etc.
 * @created 28-Dec-2023 5:20:37 PM
 */
public class ChargeType extends Document {

	public String chargeOrder;
	public String chargeVersion;
	public DateTime effectiveDate;
	public String factor;
	public String frequencyType;
	public DateTime terminationDate;
	public String totalInterval;
	/**
	 * A ChargeGroup can have 0-n ChargeType. A ChargeType can associate to 0-n
	 * ChargeGroup.
	 */
	public ChargeGroup ChargeGroup;
	/**
	 * A ChargeType can have 0-n ChargeComponent and a ChargeComponent can associate
	 * to 0-n ChargeType
	 */
	public ChargeComponent ChargeComponents;
	public MktUserAttribute MktUserAttribute;

	public ChargeType(){

	}
}//end ChargeType