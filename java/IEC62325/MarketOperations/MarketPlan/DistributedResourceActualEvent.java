package IEC62325.MarketOperations.MarketPlan;

import IEC61970.Base.Domain.ActivePower;
import IEC62325.MarketOperations.MarketSystem.MarketResults.InstructionClearing;
import IEC62325.MarketOperations.MarketSystem.MarketResults.ResourcePerformanceEvaluation;
import IEC62325.MarketOperations.MarketSystem.MarketResults.InstructionClearingDOT;

/**
 * A demand response event is created when there is a need to call upon resources
 * to respond to demand adjustment requests. These events are created by ISO/RTO
 * system operations and managed  by a demand response management system (DRMS).
 * These events may or may not be coordinated with the Market Events and a defined
 * Energy Market. The event will call for the deployment of a number of registered
 * resources, or for deployment of resources within a zone (an organizational area
 * within the power system that contains a number of resources).
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class DistributedResourceActualEvent extends MarketActualEvent {

	/**
	 * Total active power adjustment (e.g. load reduction) requested for this demand
	 * response event.
	 */
	public ActivePower totalPowerAdjustment;
	/**
	 * ActualDemandResponseEvents may exist that are not part of a coordinated
	 * MarketActualEvent associated to a Market. These ActualDemandResponseEvents can
	 * have many InstructionClearing Instructions for specified RegisteredResources or
	 * DemandResponse AggregateNodes.
	 */
	public InstructionClearing InstructionClearing;
	public ResourcePerformanceEvaluation ResourcePerformanceEvaluations;
	public InstructionClearingDOT InstructionClearingDOT;

	public DistributedResourceActualEvent(){

	}
}//end DistributedResourceActualEvent