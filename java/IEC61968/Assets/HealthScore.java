package IEC61968.Assets;


/**
 * Score that is indicative of the health of one or more assets.
 * @author Gowri
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class HealthScore extends AggregateScore {

	/**
	 * Risk score with which this health score is associated.
	 */
	public RiskScore AssetRiskScore;

	public HealthScore(){

	}
}//end HealthScore