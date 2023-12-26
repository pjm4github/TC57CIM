package IEC62325.Environmental;

import IEC61970.Base.Domain.Integer;
import IEC61968.AssetMeas.CalculationIntervalUnitKind;
import IEC62325.Environmental.EnvDomain.ReportingMethodKind;
import IEC62325.MarketCommon.EnvironmentalMonitoringStation;

/**
 * <font color="#0f0f0f">Definition of one set of reporting capabilities for this
 * monitoring station. The associated EnvironmentalValueSets describe the maximum
 * range of possible environmental values the station is capable of returning.
 * This attribute is intended primarily to assist a utility in managing its
 * stations. </font>
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class ReportingCapability {

	/**
	 * Number of units of time making up reporting period.
	 */
	public Integer reportingIntervalPeriod;
	/**
	 * Unit of time in which reporting period is expressed. 
	 */
	public CalculationIntervalUnitKind reportingIntervalType;
	/**
	 * Indicates how the weather station reports observations.
	 */
	public ReportingMethodKind reportingMethod;
	/**
	 * The environmental monitoring station to which this set of reporting
	 * capabilities belong.
	 */
	public EnvironmentalMonitoringStation EnvironmentalMonitoringStation;

	public ReportingCapability(){

	}
}//end ReportingCapability