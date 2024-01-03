package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC62325.MarketOperations.MktDomain.BidTypeRMR;
import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.SelfSchedReferenceType;
import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.MktDomain.MarketProductSelfSchedType;
import IEC62325.MarketOperations.MktDomain.MQSCHGType;
import IEC61970.Base.Core.RegularIntervalSchedule;

/**
 * Defines self schedule values to be used for specified time intervals.
 * @created 28-Dec-2023 5:19:48 PM
 */
public class BidSelfSched extends RegularIntervalSchedule {

	/**
	 * This is a Y/N flag for a self-schedule of a resource per market per date and
	 * hour, using a specific TR ID. It indicates whether a self-schedule using a TR
	 * is balanced with another self-schedule using the same TR ID.
	 */
	public YesNo balancingFlag;
	/**
	 * bidType has two types as the required output of requirements and qualified pre-
	 * dispatch.
	 */
	public BidTypeRMR bidType;
	/**
	 * This is a Y/N flag for a self-schedule of a resource per market per date and
	 * hour, using a specific TR ID. It indicates whether a self-schedule using a TR
	 * has scheduling priority in DAM/RTM.
	 */
	public YesNo priorityFlag;
	/**
	 * Contains the PriceTaker, ExistingTransmissionContract,
	 * TransmissionOwnershipRights pumping self schedule quantity. If this value is
	 * not null, then the unit is in pumping mode.
	 */
	public Float pumpSelfSchedMw;
	/**
	 * Indication of which type of self schedule is being referenced.
	 */
	public SelfSchedReferenceType referenceType;
	/**
	 * Self scheduled value
	 */
	public Float selfSchedMw;
	/**
	 * Price Taker Export Self Sched Support Resource
	 */
	public String selfSchedSptResource;
	/**
	 * This attribute is used to specify if a bid includes a self sched bid. If so
	 * what self sched type is it. The possible values are shown as follow but not
	 * limited to:
	 * 
	 * 'ETC' - Existing transmission contract
	 * 'TOR' - Transmission ownership right
	 * 'RMR' - Reliability must run
	 * 'RGMR' - Regulatory must run
	 * "RMT" - Relaiability must take
	 * "PT" - Price taker
	 * "LPT" - Low price taker
	 * "SP" - Self provision
	 * "RA" - Resource adequacy
	 * 
	 * This attribute is originally defined in the BidSelfSched class
	 */
	public MarketProductSelfSchedType selfSchedType;
	public MQSCHGType updateType;
	/**
	 * A unique identifier of a wheeling transaction. A wheeling transaction is a
	 * balanced Energy exchange among Supply and Demand Resources.
	 */
	public String wheelingTransactionReference;

	public BidSelfSched(){

	}
}//end BidSelfSched