package IEC62325.InfIEC62325.InfCongestionRevenueRights;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Meas.Limit;
import IEC62325.MarketOperations.ReferenceData.Flowgate;
import IEC62325.MarketOperations.MarketOpCommon.MktMeasurement;

/**
 * A type of limit that indicates if it is enforced and, through association, the
 * organisation responsible for setting the limit.
 * @created 02-Jan-2024 11:58:01 PM
 */
public class ViolationLimit extends Limit {

	/**
	 * True if limit is enforced. 
	 */
	public Boolean enforced;
	public Flowgate Flowgate;
	public MktMeasurement MktMeasurement;

	public ViolationLimit(){

	}
}//end ViolationLimit