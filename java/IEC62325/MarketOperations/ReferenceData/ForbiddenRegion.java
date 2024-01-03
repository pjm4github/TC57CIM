package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Forbbiden region is operating ranges where the units are unable to maintain
 * steady operation without causing equipment damage.  The four attributes that
 * define a forbidden region are the low MW, the High MW, the crossing time, and
 * the crossing cost.
 * @created 28-Dec-2023 12:13:58 PM
 */
public class ForbiddenRegion extends IdentifiedObject {

	/**
	 * Cost associated with crossing the forbidden region
	 */
	public Float crossingCost;
	/**
	 * Time to cross the forbidden region in minutes.
	 */
	public Integer crossTime;
	/**
	 * High end of the region definition
	 */
	public Float highMW;
	/**
	 * Low end of the region definition.
	 */
	public Float lowMW;

	public ForbiddenRegion(){

	}
}//end ForbiddenRegion