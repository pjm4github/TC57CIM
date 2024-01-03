package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Domain.Float;

/**
 * Model to define a zone within a Metered Sub System.
 * @created 28-Dec-2023 12:17:00 PM
 */
public class MSSZone extends AggregateNode {

	/**
	 * Provides an indication if losses are to be ignored for this metered subsystem
	 * zone.
	 */
	public YesNo ignoreLosses;
	/**
	 * This is the default loss factor for the Metered Sub-System (MSS) zone. The
	 * actual losses are calculated during the RT market.
	 */
	public Float lossFactor;
	/**
	 * Metered Sub-System (MSS) Load Following may select Net vs. Gross settlement.
	 * Net Settlement requires the net Demand settled at the Metered Sub-Sustem (MSS)
	 * Load Aggregation Point (LAP) and Net Supply needs to settle at the equivalent
	 * to the weighted average price of the MSS generation.  Gross load will be
	 * settled at the System LAP and the Gross supply will be settled at the LMP.  MSS
	 * Aggregation that elects gross settlement shall have to identify if its
	 * resources are Load Following or not. 
	 */
	public YesNo rucGrossSettlement;

	public MSSZone(){

	}
}//end MSSZone