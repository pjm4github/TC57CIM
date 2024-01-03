package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.PurposeFlagType;
import IEC62325.MarketOperations.MktDomain.MPMTestIdentifierType;
import IEC62325.MarketOperations.MktDomain.MPMTestMethodType;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.MarketSystem.MarketResults.MPMTestResults;
import IEC62325.MarketOperations.MarketSystem.MarketResults.MPMResourceStatus;

/**
 * Provides a reference to the Market Power Mitigation test identifiers and
 * methods for the results of the DA or RT markets. Specific data is the test
 * identifier (Price, Conduct, or Impact) and the test method (System MPM, Local
 * MPM, Alternate System MPM, or Alternate Local MPM).
 * @created 28-Dec-2023 12:16:10 PM
 */
public class MPMTestCategory extends IdentifiedObject {

	/**
	 * Nature of threshold data:
	 * 'M' - Mitigation threshold
	 * 'R' - Reporting threshold
	 */
	public PurposeFlagType purposeFlag;
	/**
	 * 1 - Global Price Test
	 * 2 - Global Conduct Test
	 * 3 - Global Impact Test
	 * 4 - Local Price Test
	 * 5 - Local Conduct Test
	 * 6 - Local Impact Test
	 */
	public MPMTestIdentifierType testIdentifier;
	/**
	 * The method of performing the market power monitoring. Examples are Normal
	 * (default) thresholds or Alternate thresholds.
	 */
	public MPMTestMethodType testMethod;
	public MPMTestThreshold MPMTestThreshold;
	public MPMTestResults MPMTestResults;
	public MPMResourceStatus MPMResourceStatus;

	public MPMTestCategory(){

	}
}//end MPMTestCategory