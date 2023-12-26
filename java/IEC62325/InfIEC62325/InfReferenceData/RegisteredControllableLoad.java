package IEC62325.InfIEC62325.InfReferenceData;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.CostPerEnergyUnit;

/**
 * Temporary holding for load reduction attributes removed from RegisteredLoad.
 * Use for future use case when developing the RegisteredDistributedResource
 * specialized classes.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class RegisteredControllableLoad {

	/**
	 * Maximum Base Load (MW), per Participating Load Resource
	 */
	public ActivePower maxBaseLoad;
	/**
	 * Maximum Deployment time (seconds)
	 */
	public Float maxDeploymentTime;
	/**
	 * Maximum Number of Daily Load Curtailments
	 */
	public Integer maxLoadRedTimesPerDay;
	/**
	 * maximum load reduction
	 */
	public ActivePower maxLoadReduction;
	/**
	 * Maxiimum Load Reduction Time (min), per Participating Load Resource
	 */
	public Float maxReductionTime;
	/**
	 * Maximum weekly deployments
	 */
	public Integer maxWeeklyDeployment;
	/**
	 * Minimum MW for a load reduction (e.g., MW rating of a discrete pump.
	 * 
	 * This attribute may be used also in the LoadBid class. The reason that the
	 * attribute is also modeled in this class is that it is resource attribute and
	 * needs to be persistently stored.
	 */
	public ActivePower minLoadReduction;
	/**
	 * minimum load reduction cost. Single number for the load
	 */
	public CostPerEnergyUnit minLoadReductionCost;
	/**
	 * Shortest period load reduction shall be maintained before load can be restored
	 * to normal levels.
	 * 
	 * This attribute may be used also in the LoadBid class. The reason that the
	 * attribute is also modeled in this class is that it is resource attribute and
	 * needs to be persistently stored.
	 */
	public Float minLoadReductionInterval;
	/**
	 * Minimum Load Reduction Time (min), per Participating Load Resource
	 */
	public Float minReductionTime;
	/**
	 * Shortest time that load shall be left at normal levels before a new load
	 * reduction.
	 * 
	 * This attribute may be used also in the LoadBid class. The reason that the
	 * attribute is also modeled in this class is that it is resource attribute and
	 * needs to be persistently stored.
	 */
	public Float minTimeBetLoadRed;
	/**
	 * Time period that is required from an order to reduce a load to the time that it
	 * takes to get to the minimum load reduction.
	 * 
	 * This attribute may be used also in the LoadBid class. The reason that the
	 * attribute is also modeled in this class is that it is resource attribute and
	 * needs to be persistently stored.
	 */
	public Float reqNoticeTime;

	public RegisteredControllableLoad(){

	}
}//end RegisteredControllableLoad