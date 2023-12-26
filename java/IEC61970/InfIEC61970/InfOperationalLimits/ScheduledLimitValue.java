package IEC61970.InfIEC61970.InfOperationalLimits;

import IEC61970.Base.LoadModel.Season;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A limit that is applicable during a scheduled time period.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class ScheduledLimitValue extends IdentifiedObject {

	/**
	 * The season for which the scheduled limits applies.    If not specified, then
	 * applicable ot any season.
	 */
	public Season Season;

	public ScheduledLimitValue(){

	}
}//end ScheduledLimitValue