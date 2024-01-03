package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.PerCent;
import IEC62325.MarketOperations.MktDomain.MPMTestOutcome;

/**
 * Provides the outcome and margin percent (as appropriate) result data for the
 * MPM tests.  There are relationships to Zone for Designated Congestion Area
 * Tests, CurveSchedData for bid segment tests, to the SubControlArea for the
 * system wide level tests, and Pnodes for the LMPM impact tests.
 * @created 28-Dec-2023 8:22:54 PM
 */
public class MPMTestResults {

	/**
	 * Used to show the Margin % result of the Impact test
	 */
	public PerCent marginPercent;
	/**
	 * The results of the test. For the Price, Impact, and Conduct tests, typical
	 * values are NA, Pass, Fail, Disable, or Skip. 
	 */
	public MPMTestOutcome outcome;

	public MPMTestResults(){

	}
}//end MPMTestResults