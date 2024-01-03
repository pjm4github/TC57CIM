package IEC62325.InfIEC62325.InfEnergyScheduling;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.BasicIntervalSchedule;
import IEC62325.MarketOperations.ReferenceData.SubControlArea;
import IEC62325.MarketOperations.MarketOpCommon.MktMeasurement;

/**
 * A continuously variable component of a control area's MW net interchange
 * schedule. Dynamic schedules are sent and received by control areas.
 * @created 03-Jan-2024 1:49:41 PM
 */
public class DynamicSchedule extends BasicIntervalSchedule {

	/**
	 * Dynamic schedule sign reversal required (true/false)
	 */
	public Boolean dynSchedSignRev;
	/**
	 * The "active" or "inactive" status of the dynamic schedule
	 */
	public String dynSchedStatus;
	/**
	 * A control area can send dynamic schedules to other control areas
	 */
	public SubControlArea Send_SubControlArea;
	/**
	 * A control area can receive dynamic schedules from other control areas
	 */
	public SubControlArea Receive_SubControlArea;
	public MktMeasurement MktMeasurement;

	public DynamicSchedule(){

	}
}//end DynamicSchedule