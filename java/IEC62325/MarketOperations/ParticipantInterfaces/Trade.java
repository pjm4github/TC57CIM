package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.MarketType;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Inter Scheduling Coordinator Trades to model financial trades which may impact
 * settlement.
 * @created 28-Dec-2023 5:23:51 PM
 */
public class Trade extends IdentifiedObject {

	/**
	 * The validated and current market accepted trade amount of a physical energy
	 * trade.
	 */
	public Float adjustedTradeQuantity;
	/**
	 * MW quantity submitted by counter SC for the same trade
	 */
	public Float counterTradeQuantity;
	/**
	 * The Depend On IST Name points to the unique IST Name in the chain of physical
	 * energy trades.
	 */
	public String dependOnTradeName;
	/**
	 * Time and date the trade was last modified. 
	 */
	public DateTime lastModified;
	public MarketType marketType;
	/**
	 * Start time and date for which trade applies.
	 */
	public DateTime startTime;
	/**
	 * Stop time and date for which trade is applicable.
	 */
	public DateTime stopTime;
	/**
	 * Timestamp of submittal of submit From Scheduling Coordinator Trade to Market
	 * Participant Bid Submittal
	 */
	public DateTime submitFromTimeStamp;
	/**
	 * Userid of the submit From Scheduling Coordinator trade 
	 */
	public String submitFromUser;
	/**
	 * Timestamp of submittal of submit To Scheduling Coordinator Trade to Market
	 * Participant Bid Submittal
	 */
	public DateTime submitToTimeStamp;
	/**
	 * Userid of the submit To Scheduling Coordinator trade 
	 */
	public String submitToUser ;
	/**
	 * tradeQuantity:
	 * If tradeType = IST, The amount of an Energy Trade.
	 * If tradeType = AST, The amount of an Ancillary Service Obligation Trade.
	 * If tradeType = UCT, The amount of a Unit Commitment Obligation Trade.
	 */
	public Float tradeQuantity;
	/**
	 * Resulting status of the trade following the rule engine processing.
	 */
	public String tradeStatus;
	public DateTime updateTimeStamp;
	public String updateUser;
	public TradeError TradeError;

	public Trade(){

	}
}//end Trade