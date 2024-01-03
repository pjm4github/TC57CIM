package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC62325.MarketOperations.MktDomain.CheckOutType;
import IEC62325.MarketOperations.MktDomain.InterTieDirection;
import IEC62325.MarketOperations.MktDomain.MarketProductType;
import IEC61970.Base.Domain.Integer;
import IEC62325.MarketOperations.MktDomain.MarketType;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Boolean;
import IEC62325.MarketOperations.MktDomain.EnergyProductType;
import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.ReferenceData.SchedulingPoint;
import IEC62325.MarketOperations.ReferenceData.RegisteredInterTie;
import IEC61970.Base.Core.Curve;

/**
 * Interchange schedule class to hold information for interchange schedules such
 * as import export type, energy type, and etc.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class InterchangeSchedule extends Curve {

	/**
	 * To indicate a check out type such as adjusted capacity or dispatch capacity.
	 */
	public CheckOutType checkOutType;
	/**
	 * Import or export.
	 */
	public InterTieDirection directionType;
	/**
	 * Energy product type.
	 */
	public MarketProductType energyType;
	/**
	 * Interval length.
	 */
	public Integer intervalLength;
	/**
	 * Market type.
	 */
	public MarketType marketType;
	/**
	 * Operating date, hour.
	 */
	public DateTime operatingDate;
	/**
	 * To indicate an out-of-market (OOM) schedule.
	 */
	public Boolean outOfMarketType;
	/**
	 * Schedule type.
	 */
	public EnergyProductType scheduleType;
	/**
	 * Wheeling Counter-Resource ID (required when Schedule Type=Wheel).
	 */
	public String wcrID;
	public SchedulingPoint InterTie;
	public RegisteredInterTie RegisteredInterTie;
	public InterchangeETCData InterchangeETCData;

	public InterchangeSchedule(){

	}
}//end InterchangeSchedule