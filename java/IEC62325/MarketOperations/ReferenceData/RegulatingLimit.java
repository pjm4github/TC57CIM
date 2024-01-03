package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * This class represents the physical characteristic of a generator regarding the
 * regulating limit.
 * @created 03-Jan-2024 2:15:34 PM
 */
public class RegulatingLimit extends IdentifiedObject {

	public ActivePower highLimit;
	public ActivePower lowLimit;

	public RegulatingLimit(){

	}
}//end RegulatingLimit