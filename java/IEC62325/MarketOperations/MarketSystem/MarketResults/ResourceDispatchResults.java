package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.MQSCHGType;

/**
 * The ResourceDispatchResults class provides market results that can be provided
 * to a SC. The specific data provided consists of several indicators such as
 * contingency flags, blocked start up, and RMR dispatch. It also provides the
 * projected overall and the regulating status of the resource.
 * @created 28-Dec-2023 8:25:53 PM
 */
public class ResourceDispatchResults {

	/**
	 * Blocked Dispatch Indicator (Yes/No)
	 */
	public String blockedDispatch;
	/**
	 * Block sending DOP to ADS (Y/N)
	 */
	public String blockedPublishDOP;
	/**
	 * Contingent Operating Reserve Indicator (Yes/No).  Resource participating with
	 * AS capacity in contingency dispatch.
	 */
	public YesNo contingencyFlag;
	/**
	 * indicate which limit is the constraints
	 */
	public String limitIndicator;
	/**
	 * resource energy ramping lower limit
	 */
	public Float lowerLimit;
	/**
	 * maximum ramp rate
	 */
	public Float maxRampRate;
	/**
	 * The upper operating limit incorporating any derate used by the RTD for the
	 * Binding Interval. 
	 */
	public Float operatingLimitHigh;
	/**
	 * The lower operating limit incorporating any derate used by the RTD for the
	 * Binding Interval. 
	 */
	public Float operatingLimitLow;
	/**
	 * Penalty Dispatch Indicator (Yes / No) indicating an un-economic adjustment.
	 */
	public YesNo penaltyDispatchIndicator;
	/**
	 * The upper regulating limit incorporating any derate used by the RTD for the
	 * Binding Interval. 
	 */
	public Float regulatingLimitHigh;
	/**
	 * The lower regulating limit incorporating any derate used by the RTD for the
	 * Binding Interval. 
	 */
	public Float regulatingLimitLow;
	/**
	 * Unit Commitment Status (On/Off/Starting)
	 */
	public String resourceStatus;
	/**
	 * Resource total upward schedule.  total schedule = En + all AS per resource per
	 * interval
	 */
	public Float totalSchedule;
	public DateTime updateTimeStamp;
	public MQSCHGType updateType;
	public String updateUser;
	/**
	 * resource energy ramping upper limit
	 */
	public Float upperLimit;

	public ResourceDispatchResults(){

	}
}//end ResourceDispatchResults