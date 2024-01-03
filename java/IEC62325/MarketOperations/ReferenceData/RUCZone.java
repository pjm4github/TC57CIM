package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MarketSystem.MarketResults.LossClearingResults;

/**
 * A specialized class of type AggregatedNode type. Defines RUC Zones. A forecast
 * region represents a collection of Nodes for which the Market operator has
 * developed sufficient historical demand and relevant weather data to perform a
 * demand forecast for such area. The Market Operator may further adjust this
 * forecast to ensure that the Reliability Unit Commitment produces adequate local
 * capacity procurement.
 * @created 03-Jan-2024 2:15:34 PM
 */
public class RUCZone extends AggregateNode {

	public LossClearingResults LossClearingResults;

	public RUCZone(){

	}
}//end RUCZone