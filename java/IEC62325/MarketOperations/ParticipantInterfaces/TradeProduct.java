package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.MktDomain.TradeType;

/**
 * <b>TradeType</b>                                        <b>TradeProduct</b>
 * IST  (InterSC Trade)                          PHY (Physical Energy Trade)
 * IST                                                  APN (Energy Trades at
 * Aggregated Pricing Nodes)
 * IST                                                  CPT (Converted Physical
 * Energy Trade)
 * AST (Ancilliary Services Trade)             RUT (Regulation Up Trade)
 * AST                                                 RDT (Regulation Down
 * Trade)
 * AST                                                 SRT (Spinning Reserve
 * Trade)
 * AST                                                 NRT (Non-Spinning Reserve
 * Trade)
 * UCT (Unit Commitment Trade)            null
 * @created 28-Dec-2023 5:24:10 PM
 */
public class TradeProduct {

	/**
	 * PHY (Physical Energy Trade);
	 * APN (Energy Trades at Aggregated Pricing Nodes);
	 * CPT (Converted Physical Energy Trade);
	 * RUT (Regulation Up Trade);
	 * RDT (Regulation Down Trade);
	 * SRT (Spinning Reserve Trade);
	 * NRT (Non-Spinning Reserve Trade)
	 */
	public String tradeProductType;
	/**
	 * IST  - InterSC Trade;
	 * AST - Ancilliary Services Trade;
	 * UCT - Unit Commitment Trade
	 */
	public TradeType tradeType;
	public Trade Trade;

	public TradeProduct(){

	}
}//end TradeProduct