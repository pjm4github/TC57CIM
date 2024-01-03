package IEC62325.MarketOperations.MarketPlan;

import IEC62325.MarketOperations.MktDomain.ExecutionType;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Boolean;
import IEC62325.MarketOperations.MktDomain.MarketType;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * This class represents an actual instance of a planned market. For example, a
 * Day Ahead market opens with the Bid Submission, ends with the closing of the
 * Bid Submission. The market run represent the whole process. MarketRuns can be
 * defined for markets such as Day Ahead Market, Real Time Market, Hour Ahead
 * Market, Week Ahead Market, etc.
 * @created 28-Dec-2023 8:12:28 PM
 */
public class MarketRun extends IdentifiedObject {

	/**
	 * The execution type; Day Ahead, Intra Day, Real Time Pre-Dispatch, Real Time
	 * Dispatch
	 */
	public ExecutionType executionType;
	/**
	 * Approved time for case. Identifies the time that the dispatcher approved a
	 * specific real time unit dispatch case
	 */
	public DateTime marketApprovalTime;
	/**
	 * Set to true when the plan is approved by authority and becomes the official
	 * plan for the day ahead market. Identifies the approved case for the market for
	 * the specified time interval.
	 */
	public Boolean marketApprovedStatus;
	/**
	 * The end time defined as the end of the market, market end time.
	 */
	public DateTime marketEndTime;
	/**
	 * The start time defined as the beginning of the market, market start time.
	 */
	public DateTime marketStartTime;
	/**
	 * The market type, Day Ahead Market or Real Time Market.
	 */
	public MarketType marketType;
	/**
	 * This is the state of market run activity as reported by market systems to the
	 * market definition services.
	 */
	public String reportedState;
	/**
	 * This is the state controlled by market defintion service.
	 * Possible values could be but not limited by: Open, Close.
	 */
	public String runState;
	public Market Market;

	public MarketRun(){

	}
}//end MarketRun