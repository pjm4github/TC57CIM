# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106


from IEC62325.MarketOperations.MarketSystem.MarketResults.InstructionClearing import InstructionClearing
from IEC62325.MarketOperations.MarketSystem.MarketResults.InstructionClearingDOT import InstructionClearingDOT


from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC62325.MarketOperations.MarketSystem.MarketResults.ResourcePerformanceEvaluation import \
    ResourcePerformanceEvaluation


class MarketActualEvent:
    pass


class DistributedResourceActualEvent(MarketActualEvent):
    """
    A demand response event is created when there is a need to call upon resources
    to respond to demand adjustment requests. These events are created by ISO/RTO
    system operations and managed  by a demand response management system (DRMS).
    These events may or may not be coordinated with the Market Events and a defined
    Energy Market. The event will call for the deployment of a number of registered
    resources, or for deployment of resources within a zone (an organizational area
    within the power system that contains a number of resources).
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        super().__init__()
        # 	 * Total active power adjustment (e.g. load reduction) requested for this demand
        # 	 * response event.
        self.total_power_adjustment = ActivePower()
        # 	 * ActualDemandResponseEvents may exist that are not part of a coordinated
        # 	 * MarketActualEvent associated to a Market. These ActualDemandResponseEvents can
        # 	 * have many InstructionClearing Instructions for specified RegisteredResources or
        # 	 * DemandResponse AggregateNodes.
        self.instruction_clearing = InstructionClearing()
        self.resource_performance_evaluations = ResourcePerformanceEvaluation()
        self.instruction_clearing_dot = InstructionClearingDOT()
