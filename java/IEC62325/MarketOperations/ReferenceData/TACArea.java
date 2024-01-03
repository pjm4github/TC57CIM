package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.AreaLoadCurve;

/**
 * Transmission Access Charge Area. Charges assessed, on behalf of the
 * Participating Transmission Owner, to parties who require access to the
 * controlled grid.
 * @created 03-Jan-2024 2:15:34 PM
 */
public class TACArea extends IdentifiedObject {

	public AreaLoadCurve AreaLoadCurve;

	public TACArea(){

	}
}//end TACArea