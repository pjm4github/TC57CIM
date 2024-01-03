package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Core.Curve;

/**
 * Startup time curve as a function of down time, where time is specified in
 * minutes.  Relationship between unit startup time (Y1-axis) vs. unit elapsed
 * down time (X-axis).
 * @created 28-Dec-2023 5:23:41 PM
 */
public class StartUpTimeCurve extends Curve {

	public GeneratingBid GeneratingBid;

	public StartUpTimeCurve(){

	}
}//end StartUpTimeCurve