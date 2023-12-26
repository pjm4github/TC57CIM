package IEC62325.Environmental;

import IEC61970.Base.Meas.Analog;
import IEC62325.MarketCommon.EnvironmentalMonitoringStation;

/**
 * Analog (float) measurement of relevance in the environmental domain.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class EnvironmentalAnalog extends Analog {

	/**
	 * Classification condition which this analog helps define.
	 */
	public ClassificationCondition ClassificationCondition;
	/**
	 * Observation or forecast with which this environmental analog measurement is
	 * associated.
	 */
	public EnvironmentalInformation EnvironmentalInformation;
	/**
	 * The reporting capability this environmental value set helps define.
	 */
	public ReportingCapability ReportingCapability;
	/**
	 * Monitoring station which provides this environmental analog measurement.
	 */
	public EnvironmentalMonitoringStation EnvironmentalMonitoringStation;

	public EnvironmentalAnalog(){

	}
}//end EnvironmentalAnalog