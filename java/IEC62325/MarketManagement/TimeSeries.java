package IEC62325.MarketManagement;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketCommon.EnvironmentalMonitoringStation;
import IEC62325.MarketCommon.MarketParticipant;

/**
 * A set of regular time-ordered measurements or values of quantitative nature of
 * an individual or collective phenomenon taken at successive, in most cases
 * equidistant, periods / points of time.
 * @created 03-Jan-2024 2:00:10 PM
 */
public class TimeSeries extends IdentifiedObject {

	/**
	 * The identification of the nature of the time series.
	 */
	public String businessType;
	/**
	 * An indicator stating that the TimeSeries, identified by the mRID, is cancelled
	 * as well as all the values sent in a previous version of the TimeSeries in a
	 * previous document.
	 */
	public String cancelledTS;
	/**
	 * The coded representation of the type of curve being described.
	 */
	public String curveType;
	/**
	 * Identification of the object that is the common denominator used to aggregate a
	 * time series.
	 */
	public String objectAggregation;
	/**
	 * The type of the product such as Power, energy, reactive power, transport
	 * capacity that is the subject of the time series.
	 */
	public String product;
	/**
	 * Version of the time series.
	 */
	public String version;
	public Reason Reason;
	public MarketEvaluationPoint MarketEvaluationPoint;
	public MarketDocument MarketDocument;
	public Period Period;
	public FlowDirection FlowDirection;
	public Domain Domain;
	public DateAndOrTime DateAndOrTime;
	public EnvironmentalMonitoringStation EnvironmentalMonitoringStation;
	public MarketParticipant MarketParticipant;

	public TimeSeries(){

	}
}//end TimeSeries