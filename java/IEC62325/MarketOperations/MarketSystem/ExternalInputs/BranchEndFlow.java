package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MarketOpCommon.MktPowerTransformer;

/**
 * Dynamic flows and ratings associated with a branch end.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class BranchEndFlow {

	/**
	 * The Load Dump Rating for the branch
	 */
	public Float loadDumpRating;
	/**
	 * The Long Term Rating for the branch
	 */
	public Float longTermRating;
	/**
	 * The MVAR flow on the branch
	 * Attribute Usage: Reactive power flow at the series device, transformer, phase
	 * shifter, or line end
	 */
	public Float mVARFlow;
	/**
	 * The MW flow on the branch
	 * Attribute Usage: Active power flow at the series device, transformer, phase
	 * shifter, or line end
	 */
	public Float mwFlow;
	/**
	 * The Normal Rating for the branch
	 */
	public Float normalRating;
	/**
	 * The Short Term Rating for the branch
	 */
	public Float shortTermRating;
	public MktACLineSegment MktACLineSegmentEndAFlow;
	public MktACLineSegment MktACLineSegmentEndBFlow;
	public MktSeriesCompensator MktSeriesCompensatorEndBFlow;
	public MktSeriesCompensator MktSeriresCompensatorEndAFlow;
	public MktPowerTransformer MktPowerTransformerEndBFlow;
	public MktPowerTransformer MktPowerTransformerEndAFlow;

	public BranchEndFlow(){

	}
}//end BranchEndFlow