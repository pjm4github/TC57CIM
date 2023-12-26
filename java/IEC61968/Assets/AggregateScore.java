package IEC61968.Assets;


/**
 * An aggregated indicative scoring by an analytic, which is based on other
 * analytic scores, that can be used to characterize the health of or the risk
 * associated with one or more assets.
 * @author Gowri
 * @version 1.0
 * @created 25-Dec-2023 8:45:18 PM
 */
public class AggregateScore extends AnalyticScore {

	public AnalyticScore AnalyticScore;

	public AggregateScore(){

	}
}//end AggregateScore