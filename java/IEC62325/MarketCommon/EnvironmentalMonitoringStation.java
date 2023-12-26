package IEC62325.MarketCommon;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Minutes;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.Common.Location;
import IEC61968.Metering.UsagePoint;

/**
 * An environmental monitoring station, examples of which could be a weather
 * station or a seismic monitoring station.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class EnvironmentalMonitoringStation extends IdentifiedObject {

	/**
	 * Whether this station is currently reporting using daylight saving time.
	 * Intended to aid a utility Weather Service in interpreting information coming
	 * from a station and has no direct relationship to the manner in which time is
	 * expressed in EnvironmentalValueSet.
	 */
	public Boolean dstObserved;
	/**
	 * Indication that station is part of a network of stations used to monitor
	 * weather phenomena covering a large geographical area.
	 */
	public Boolean isNetworked;
	/**
	 * The time offset from UTC (a.k.a. GMT) configured in the station "clock", not
	 * (necessarily) the time zone in which the station is physically located.
	 * This attribute exists to support management of utility monitoring stations and
	 * has no direct relationship to the manner in which time is expressed in
	 * EnvironmentalValueSet.
	 */
	public Minutes timeZoneOffset;
	/**
	 * Location of this monitoring station.
	 */
	public Location Location;
	public UsagePoint UsagePoint;

	public EnvironmentalMonitoringStation(){

	}
}//end EnvironmentalMonitoringStation