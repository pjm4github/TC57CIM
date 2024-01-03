package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Core.Curve;
import IEC62325.MarketOperations.ReferenceData.RegisteredGenerator;

/**
 * Startup costs and time as a function of down time.  Relationship between unit
 * startup cost (Y1-axis) vs. unit elapsed down time (X-axis).
 * @created 28-Dec-2023 5:23:32 PM
 */
public class StartUpCostCurve extends Curve {

	public RegisteredGenerator RegisteredGenerators;
	public GeneratingBid GeneratingBid;

	public StartUpCostCurve(){

	}
}//end StartUpCostCurve