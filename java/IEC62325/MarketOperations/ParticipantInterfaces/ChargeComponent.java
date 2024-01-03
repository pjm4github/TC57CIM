package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.MarketSystem.MarketResults.BillDeterminant;

/**
 * A Charge Component is a list of configurable charge quality items to feed into
 * settlement calculation and/or bill determinants.
 * @created 28-Dec-2023 5:20:12 PM
 */
public class ChargeComponent extends IdentifiedObject {

	public String deleteStatus;
	public DateTime effectiveDate;
	public String equation;
	public String message;
	public String roundOff;
	public String sum;
	public DateTime terminationDate;
	public String type;
	/**
	 * A BillDeterminant can have 0-n ChargeComponent and a ChargeComponent can
	 * associate to 0-n BillDeterminant.
	 */
	public BillDeterminant BillDeterminants;

	public ChargeComponent(){

	}
}//end ChargeComponent