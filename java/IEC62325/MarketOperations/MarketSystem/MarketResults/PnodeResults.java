package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.MQSCHGType;
import IEC61970.Base.Domain.String;

/**
 * Provides the total price, the cost component, the loss component, and the
 * congestion component for Pnodes for the forward and real time markets. There
 * are several prices produced based on the run type (MPM, RUC, Pricing, or
 * Scheduling/Dispatch).
 * @created 28-Dec-2023 8:24:38 PM
 */
public class PnodeResults {

	/**
	 * Congestion component of Location Marginal Price (LMP) in monetary units per MW.
	 */
	public Float congestLMP;
	/**
	 * Cost component of Locational Marginal Pricing (LMP) in monetary units per MW.
	 */
	public Float costLMP;
	/**
	 * Loss component of Location Marginal Price (LMP) in monetary units per MW.
	 */
	public Float lossLMP;
	/**
	 * Locational Marginal Price (LMP) ($/MWh)
	 */
	public Float marginalClearingPrice;
	/**
	 * total MW schedule at the pnode
	 */
	public Float scheduledMW;
	public DateTime updateTimeStamp;
	public MQSCHGType updateType;
	public String updateUser;

	public PnodeResults(){

	}
}//end PnodeResults