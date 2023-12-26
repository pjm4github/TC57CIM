package IEC62325.InfIEC62325.InfMarketOpCommon;


/**
 * Kind of market role an organisation can have. This list is not exhausted, as
 * other roles may exist.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public enum MarketRoleKind {
	/**
	 * Energy service consumer.
	 */
	energyServiceConsumer,
	/**
	 * Generator merchant owner.
	 */
	generatorOwner,
	/**
	 * Generator merchant operator.
	 */
	generatorOperator,
	/**
	 * Transmission service provider.
	 */
	transmissionServiceProvider,
	/**
	 * Transmission owner.
	 */
	transmissionOwner,
	/**
	 * Transmission operator.
	 */
	transmissionOperator,
	/**
	 * Distribution provider.
	 */
	distributionProvider,
	/**
	 * Load serving entity.
	 */
	loadServingEntity,
	/**
	 * Purchasing selling entity.
	 */
	purchasingSellingEntity,
	/**
	 * Competitive retailer.
	 */
	competitiveRetailer,
	/**
	 * Reliability authority.
	 */
	reliabilityAuthority,
	/**
	 * Planning authority.
	 */
	planningAuthority,
	/**
	 * Balancing authority.
	 */
	balancingAuthority,
	/**
	 * Interchange authority.
	 */
	interchangeAuthority,
	/**
	 * Transmission planner.
	 */
	transmissionPlanner,
	/**
	 * Resource planner.
	 */
	resourcePlanner,
	/**
	 * Standards developer.
	 */
	standardsDeveloper,
	/**
	 * Compliance monitor.
	 */
	complianceMonitor,
	/**
	 * A party that has a contract proving financial security and identifying balance
	 * responsibility with the Imbalance Settlement Responsible of the Market Balance
	 * Area entitling the party to operate in the market. This is the only role
	 * allowing a party to nominate energy on a wholesale level.
	 * <b><i>Additional information:</i></b>
	 * The meaning of the word "balance" in this context signifies that the quantity
	 * contracted to provide or to consume shall be equal to the quantity really
	 * provided or consumed. Equivalent to "Program responsible party" in the
	 * Netherlands. Equivalent to "Balance group manager" in Germany. Equivalent to
	 * "market agent" in Spain.
	 */
	BalanceResponsibleParty,
	/**
	 * A party that markets the difference between actual metered energy consumption
	 * and the energy bought with firm energy contracts by the Party Connected to the
	 * Grid. In addition the Balance Supplier markets any difference with the firm
	 * energy contract (of the Party Connected to the Grid) and the metered production.
	 * 
	 * <b><i>Additional information:</i></b>
	 * There is only one Balance Supplier for each Accounting Point.
	 */
	BalanceSupplier,
	/**
	 * The party responsible for invoicing a concerned party.
	 */
	BillingAgent,
	/**
	 * A party that is selling or buying energy on a firm basis (a fixed volume per
	 * market time period).
	 */
	BlockEnergyTrader,
	/**
	 * A party, acting on behalf of the System Operators involved, responsible for
	 * establishing a coordinated Offered Capacity and/or Net Transfer Capacity (NTC)
	 * and/or Available Transfer Capacity (ATC) between several Market Balance Areas.
	 */
	CapacityCoordinator,
	/**
	 * A party that has a contract to participate in the Capacity Market to acquire
	 * capacity through a Transmission Capacity Allocator.
	 * 
	 * The capacity may be acquired on behalf of an Interconnection Trade Responsible
	 * or for sale on secondary capacity markets.
	 */
	CapacityTrader,
	/**
	 * A party that consumes electricity.
	 * <b><i>Additional information:</i></b>
	 * This is a Type of Party Connected to the Grid.
	 */
	Consumer,
	/**
	 * A party who can be brought to rights, legally and financially, for any
	 * imbalance between enegry nominated and consumed for all associated Accounting
	 * Points.
	 * <b><i>Additional information:</i></b>
	 * This is a type of Balance Responsible Party.
	 */
	ConsumptionResponsibleParty,
	/**
	 * Responsible for :
	 * 1. The coordination of exchange programs between its related Market Balance
	 * Areas and for the exchanges between its associated Control Areas.
	 * 2. The load frequency control for its own area.
	 * 3. The coordination of the correction of time deviations.
	 */
	ControlAreaOperator,
	/**
	 * Responsible for :
	 * 1. The coordination of exchanges between its associated Control Blocks and the
	 * organisation of the coordination of exchange programs between its related
	 * Control Areas.
	 * 2. The load frequency control within its own block and ensuring that its
	 * Control Areas respect their obligations in respect to load frequency control
	 * and time deviation.
	 * 3. The organisation of the settlement and/or compensation between its Control
	 * Areas.
	 */
	ControlBlockOperator,
	/**
	 * Responsible for :
	 * 1. The coordination of exchange programs between its related Control Blocks and
	 * for the exchanges between its associated Coordination Center Zones.
	 * 2. Ensuring that its Control Blocks respect their obligations in respect to
	 * load frequency control.
	 * 3. Calculating the time deviation in cooperation with the associated
	 * coordination centers.
	 * 4. Carrying out the settlement and/or compensation between its Control Blocks
	 * and against the other Coordination Center Zones.
	 */
	CoordinationCenterOperator,
	/**
	 * A party responsible for providing access to the grid through an Accounting
	 * Point and its use for energy consumption or production to the Party Connected
	 * to the Grid.
	 */
	GridAccessProvider,
	/**
	 * A party that operates one or more grids.
	 */
	GridOperator,
	/**
	 * A party that is responsible for settlement of the difference between the
	 * contracted quantities and the realised quantities of energy products for the
	 * Balance Responsible Parties in a Market Balance Area.
	 * Note:
	 * The Imbalance Settlement Responsible has not the responsibility to invoice. The
	 * Imbalance Settlement Responsible may delegate the invoicing responsibility to a
	 * more generic role such as a Billing Agent.
	 */
	ImbalanceSettlementResponsible,
	/**
	 * Is a Balance Responsible Party or depends on one. They are recognized by the
	 * Nomination Validator for the nomination of already allocated capacity.
	 * <b><i>Additional information:</i></b>
	 * This is a type of Balance Responsible Party.
	 */
	InterconnectionTradeResponsible,
	/**
	 * Market Information Aggregator, A party that provides market related information
	 * that has been compiled from the figures supplied by different actors in the
	 * market. This information may also be published or distributed for general use.
	 * <b><i>Note:</i></b>
	 * The Market Information Aggregator may receive information from any market
	 * participant that is relevant for publication or distribution.
	 */
	MarketInformationAggregator,
	/**
	 * The unique power exchange of trades for the actual delivery of energy that
	 * receives the bids from the Balance Responsible Parties that have a contract to
	 * bid. The Market Operator determines the market energy price for the Market
	 * Balance Area after applying technical constraints from the System Operator. It
	 * may also establish the price for the reconciliation within a Metering Grid Area.
	 */
	MarketOperator,
	/**
	 * A party responsible for keeping a database of meters.
	 */
	MeterAdministrator,
	/**
	 * A party responsible for installing, maintaining, testing, certifying and
	 * decommissioning physical meters.
	 */
	MeterOperator,
	/**
	 * A party responsible for meter reading and quality control of the reading.
	 */
	MeteredDataCollector,
	/**
	 * A party responsible for the establishment and validation of metered data based
	 * on the collected data received from the Metered Data Collector. The party is
	 * responsible for the history of metered data for a Metering Point.
	 */
	MeteredDataResponsible,
	/**
	 * A party responsible for the establishment and qualification of metered data
	 * from the Metered Data Responsible. This data is aggregated according to a
	 * defined set of market rules.
	 */
	MeteredDataAggregator,
	/**
	 * A party responsible for registering the parties linked to the metering points
	 * in a Metering Grid Area. They are also responsible for maintaining the Metering
	 * Point technical specifications. They are responsible for creating and
	 * terminating metering points.
	 */
	MeteringPointAdministrator,
	/**
	 * Responsible for the management of the available tenders for all Acquiring
	 * System Operators to establish the order of the reserve capacity that can be
	 * activated.
	 */
	MOLResponsible,
	/**
	 * Has the responsibility of ensuring that all capacity nominated is within the
	 * allowed limits and confirming all valid nominations to all involved parties.
	 * They inform the Interconnection Trade Responsible of the maximum nominated
	 * capacity allowed. Depending on market rules for a given interconnection the
	 * corresponding System Operators may appoint one Nomination Validator.
	 */
	NominationValidator,
	/**
	 * A party that contracts for the right to consume or produce electricity at an
	 * Accounting Point.
	 */
	PartyConnectedToTheGrid,
	/**
	 * A party that produces electricity.
	 * <b><i>Additional information:</i></b>
	 * This is a type of Party Connected to the Grid.
	 */
	Producer,
	/**
	 * A party who can be brought to rights, legally and financially, for any
	 * imbalance between energy nominated and produced for all associated Accounting
	 * Points.
	 * <b><i>Additional information:</i></b>
	 * This is a type of Balance Responsible Party.
	 */
	ProductionResponsibleParty,
	/**
	 * A party that is financially accountable for the reconciled volume of energy
	 * products for a profiled Accounting Point.
	 */
	ReconciliationAccountable,
	/**
	 * A party that is responsible for reconciling, within a Metering Grid Area, the
	 * volumes used in the imbalance settlement process for profiled Accounting Points
	 * and the actual metered quantities.
	 * Note:
	 * The Reconciliation Responsible may delegate the invoicing responsibility to a
	 * more generic role such as a Billing Agent.
	 */
	ReconciliationResponsible,
	/**
	 * Informs the market of reserve requirements, receives tenders against the
	 * requirements and in compliance with the prequalification criteria, determines
	 * what tenders meet requirements and assigns tenders.
	 */
	ReserveAllocator,
	/**
	 * A role that manages a resource object and provides the schedules for it
	 */
	ResourceProvider,
	/**
	 * A party that is responsible for the schedule information and its exchange on
	 * behalf of a Balance Responsible Party. For example in the Polish market a
	 * Scheduling Coordinator is responsible for information interchange for
	 * scheduling and settlement.
	 */
	SchedulingCoordinator,
	/**
	 * A party that is responsible for a stable power system operation
	 * (including the organisation of physical balance) through a transmission grid in
	 * a geographical area. The System Operator will also determine and be responsible
	 * for cross border capacity and exchanges. If necessary they may reduce allocated
	 * capacity to ensure operational stability. Transmission as mentioned above means
	 * "the transport of electricity on the extra high or high voltage network with a
	 * view to its delivery to final customers or to distributors. Operation of
	 * transmission includes as well the tasks of system operation concerning its
	 * management of energy flows, reliability of the system and availability of all
	 * necessary system services." (definition taken from the ENTSO-E RGCE Operation
	 * handbook Glossary).
	 * <b><i>Note: </i></b>additional obligations may be imposed through local market
	 * rules.
	 */
	SystemOperator,
	/**
	 * A party who can be brought to rights, legally and financially, for any
	 * imbalance between energy nominated and consumed for all associated Accounting
	 * Points.
	 * <b><i>Note:</i></b>
	 * A power exchange without any privileged responsibilities acts as a Trade
	 * Responsible Party.
	 * <b><i>Additional information:</i></b>
	 * This is a type of Balance Responsible Party.
	 */
	TradeResponsibleParty,
	/**
	 * Manages the allocation of transmission capacity for an Allocated Capacity Area.
	 * 
	 * <b><i>For explicit auctions:</i></b>
	 * The Transmission Capacity Allocator manages, on behalf of the System Operators,
	 * the allocation of available transmission capacity for an Allocated capacity
	 * Area. They offer the available transmission capacity to the market, allocates
	 * the available transmission capacity to individual Capacity Traders and
	 * calculates the billing amount of already allocated capacities to the Capacity
	 * Traders.
	 */
	TransmissionCapacityAllocator
}