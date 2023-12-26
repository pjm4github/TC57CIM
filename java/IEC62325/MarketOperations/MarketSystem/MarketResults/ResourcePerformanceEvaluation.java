package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Represents an the performance evaluation of a resource deployment. Every
 * resource deployment may have many performance evaluations, using different
 * evaluation metrics or algorithms, or produced by different evaluation
 * authorities.
 * @author mwald
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class ResourcePerformanceEvaluation extends IdentifiedObject {

	public DateTime effectiveEndTime;
	public DateTime effectiveStartTime;
	/**
	 * Description of the performance evaluation, e.g. the rating classification used
	 * (any is allowed), why the evaluation was performed, anything that describes the
	 * demand response performance evaluation.
	 */
	public String evaluationDescription;
	/**
	 * The value of the performance. as a String, any rating scheme is supported (e.g.
	 * "1","2","3" or "low", "medium", "high"). The rating scheme is described in the
	 * performanceValueDescription attribute.
	 */
	public String evaluationValue;
	public ResourcePerformanceTimeSeriesFactor ResourcePerformanceTimeSeriesFactors;

	public ResourcePerformanceEvaluation(){

	}
}//end ResourcePerformanceEvaluation