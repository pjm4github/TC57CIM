package IEC62325.MarketOperations.MarketPlan;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Market (e.g. Day Ahead Market, Real Time Market) with a description of the
 * Market operation control parameters.
 * @created 28-Dec-2023 8:11:35 PM
 */
public class Market extends IdentifiedObject {

	/**
	 * Market ending time - actual market end
	 */
	public DateTime actualEnd;
	/**
	 * Market starting time - actual market start
	 */
	public DateTime actualStart;
	/**
	 * True if daylight savings time (DST) is in effect.
	 */
	public Boolean dst;
	/**
	 * Market end time.
	 */
	public DateTime end;
	/**
	 * Local time zone.
	 */
	public String localTimeZone;
	/**
	 * Market start time.
	 */
	public DateTime start;
	/**
	 * Market Status
	 * 'OPEN', 'CLOSED', 'CLEARED', 'BLOCKED'
	 */
	public String status;
	/**
	 * Trading time interval length.
	 */
	public Float timeIntervalLength;
	/**
	 * Market trading date
	 */
	public DateTime tradingDay;
	/**
	 * Trading period that describes the market, possibilities could be for an Energy
	 * Market:
	 * Day
	 * Hour
	 * 
	 * For a CRR Market:
	 * Year
	 * Month
	 * Season
	 */
	public String tradingPeriod;

	public Market(){

	}
}//end Market