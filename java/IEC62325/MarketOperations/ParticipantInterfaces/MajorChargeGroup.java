package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.MarketSystem.MarketResults.Settlement;

/**
 * A Major Charge Group is the same as Invoice Type which provides the highest
 * level of grouping for charge types configuration. Examples: Market, FERC, RMR.
 * @created 28-Dec-2023 5:22:22 PM
 */
public class MajorChargeGroup extends IdentifiedObject {

	public DateTime effectiveDate;
	public String frequencyType;
	public String invoiceType;
	public String requireAutorun;
	/**
	 * Revision number for the major charge group
	 */
	public String revisionNumber;
	public String runType;
	public String runVersion;
	public DateTime terminationDate;
	/**
	 * A MajorChargeGroup can have 0-n ChargeType. A ChargeType can associate to 0-n
	 * MajorChargeGroup.
	 */
	public ChargeType ChargeType;
	public MarketScheduledEvent MktScheduledEvent;
	public Settlement Settlement;

	public MajorChargeGroup(){

	}
}//end MajorChargeGroup