package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC62325.MarketOperations.MktDomain.BidMitigationType;
import IEC62325.MarketOperations.MktDomain.BidMitigationStatus;
import IEC61970.Base.Core.RegularIntervalSchedule;

/**
 * Defines bid schedules to allow a product bid to use specified bid price curves
 * for different time intervals.
 * @created 28-Dec-2023 5:19:35 PM
 */
public class BidPriceSchedule extends RegularIntervalSchedule {

	/**
	 * BID Type:
	 * 
	 * I - Initial Bid;
	 * F - Final Bid
	 */
	public BidMitigationType bidType;
	/**
	 * Mitigation Status:
	 * 
	 * 'S' - Mitigated by SMPM because of "misconduct"
	 * 'L; - Mitigated by LMPM because of "misconduct"
	 * 'R' - Modified by LMPM because of RMR rules
	 * 'M' - Mitigated because of "misconduct" both by SMPM and LMPM
	 * 'B' - Mitigated because of "misconduct" both by SMPM and modified by LMLM
	 * because of RMR rules
	 * 'O' - original
	 */
	public BidMitigationStatus mitigationStatus;

	public BidPriceSchedule(){

	}
}//end BidPriceSchedule