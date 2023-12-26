package IEC62325.Environmental;

import IEC61970.Base.Domain.DateTimeInterval;

/**
 * The actual or forecast characteristics of an environmental phenomenon at a
 * specific point in time (or during a specific time interval) that may have both
 * a center and area/line location.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class EnvironmentalPhenomenon {

	/**
	 * The timestamp of the phenomenon as a single point or time interval.
	 */
	public DateTimeInterval timeInterval;
	/**
	 * The forecast or observation of which this phenomenon description is a part.
	 */
	public EnvironmentalInformation EnvironmentalInformation;
	/**
	 * Location of relevance to this environmental phenomenon.
	 */
	public EnvironmentalLocationType EnvironmentalLocationKind;
	/**
	 * The classification of this phenomenon.
	 */
	public PhenomenonClassification PhenomenonClassification;

	public EnvironmentalPhenomenon(){

	}
}//end EnvironmentalPhenomenon