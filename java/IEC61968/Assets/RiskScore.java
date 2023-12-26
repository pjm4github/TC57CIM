package IEC61968.Assets;


/**
 * Score that is indicative of the risk associated with one or more assets.
 * @author Gowri
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class RiskScore extends AggregateScore {

	/**
	 * The risk kind, such as CustomerRisk, FinancialRisk, SafetyRisk, etc.
	 */
	public RiskScoreKind kind;

	public RiskScore(){

	}
}//end RiskScore