package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.ParticipantInterfaces.Trade;
import IEC62325.MarketCommon.MarketParticipant;

/**
 * Market participants could be represented by Scheduling Coordinators (SCs) that
 * are registered with the RTO/ISO. One participant could register multiple SCs
 * with the RTO/ISO. Many market participants can do business with the RTO/ISO
 * using a single SC. One SC could schedule multiple generators. A load scheduling
 * point could be used by multiple SCs. Each SC could schedule load at multiple
 * scheduling points. An inter-tie scheduling point can be used by multiple SCs.
 * Each SC can schedule interchange at multiple inter-tie scheduling points.
 * @created 03-Jan-2024 2:15:34 PM
 */
public class SchedulingCoordinator extends MarketParticipant {

	/**
	 * Flag to indicate creditworthiness (Y, N)
	 */
	public YesNo creditFlag;
	/**
	 * Date that the scheduling coordinator becomes creditworthy.
	 */
	public DateTime creditStartEffectiveDate;
	/**
	 * Indication of the last time this scheduling coordinator information was
	 * modified.
	 */
	public DateTime lastModified;
	/**
	 * Scheduling coordinator qualification status, Qualified, Not Qualified, or
	 * Disqualified.
	 */
	public String qualificationStatus;
	/**
	 * This is the short name or Scheduling Coordinator ID field.
	 */
	public String scid;
	public ContractRight TransmissionContractRight;
	public Trade SubmitToSCTrade;
	public Trade ToSCTrade;
	public Trade FromSCTrade;
	public Trade SubmitFromSCTrade;
	public MarketParticipant MarketParticipant;
	public SchedulingCoordinatorUser m_SchedulingCoordinatorUser;

	public SchedulingCoordinator(){

	}
}//end SchedulingCoordinator