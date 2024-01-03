package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.ApnodeType;
import IEC62325.MarketOperations.MktDomain.ParticipationCategoryMPM;
import IEC62325.MarketOperations.MarketSystem.MarketResults.MPMTestResults;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.GenDistributionFactor;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.LoadDistributionFactor;

/**
 * An aggregated pricing node is a specialized type of pricing node used to model
 * items such as System Zone, Default Price Zone, Custom Price Zone, Control Area,
 * Aggregated Generation, Aggregated Particpating Load, Aggregated Non-
 * Participating Load, Trading Hub, Designated Control Area(DCA) Zone.
 * @created 03-Jan-2024 2:15:33 PM
 */
public class AggregatedPnode extends Pnode {

	/**
	 * Aggregate Price Node Types
	 */
	public ApnodeType apnodeType;
	/**
	 * Designated Control Area participation in LMP price measurement
	 * 
	 * 'Y' - Participates in both Local Market Power Mitigation (LMPM) and System
	 * Market Power Mitigation (SMPM)
	 * 'N' - Not included in LMP price measures
	 * 'S' - Participatesin SMPM price measures
	 * 'L' - Participatesin LMPM price measures
	 */
	public ParticipationCategoryMPM participationCategory;
	public TACArea TACArea;
	public PnodeDistributionFactor PnodeDistributionFactor;
	public MPMTestResults MPMTestResults;
	public GenDistributionFactor GenDistributionFactor;
	public LoadDistributionFactor LoadDistributionFactor;

	public AggregatedPnode(){

	}
}//end AggregatedPnode