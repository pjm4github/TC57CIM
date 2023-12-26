package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.ReferenceData.RegisteredDistributedResource;

/**
 * Rating of a resource for its demand response performance. e.g. given a set on
 * monthly resource demand response performance evaluations, the resource may be
 * rated with excellent, average, or poor performance for the sample set.
 * @author mwald
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class ResourcePerformanceRating extends IdentifiedObject {

	/**
	 * starting date time that the rating is valid for
	 */
	public DateTime effectiveEndTime;
	/**
	 * ending date time that the rating is valid for
	 */
	public DateTime effectiveStartTime;
	/**
	 * the resource's demand response rating description
	 */
	public String ratingDescription;
	/**
	 * the type of performance rating, e.g. which market or product the rating is for
	 */
	public String ratingType;
	/**
	 * the resource's demand response rating
	 */
	public String ratingValue;
	public RegisteredDistributedResource RegisteredResource;

	public ResourcePerformanceRating(){

	}
}//end ResourcePerformanceRating