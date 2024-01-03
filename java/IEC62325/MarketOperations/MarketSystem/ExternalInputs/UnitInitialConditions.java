package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.RealEnergy;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.ReferenceData.RegisteredGenerator;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Resource status at the end of a given clearing period.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class UnitInitialConditions extends IdentifiedObject {

	/**
	 * Cumulative energy production over trading period.
	 */
	public RealEnergy cumEnergy;
	/**
	 * Cumulative number of status changes of the resource.
	 */
	public Integer cumStatusChanges;
	/**
	 * Number of start ups in the Operating Day until the end of previous hour.
	 */
	public Integer numberOfStartups;
	/**
	 * 'true' if the GeneratingUnit is currently On-Line
	 */
	public Boolean onlineStatus;
	/**
	 * Resource MW output at the end of previous clearing period.
	 */
	public ActivePower resourceMW;
	/**
	 * Resource status at the end of previous clearing period:
	 * 0 - off-line
	 * 1 - on-line production
	 * 2 - in shutdown process
	 * 3 - in startup process
	 */
	public Integer resourceStatus;
	/**
	 * Time and date for resourceStatus
	 */
	public DateTime statusDate;
	/**
	 * Time in market trading intervals the resource is in the state as of the end of
	 * the previous clearing period.
	 */
	public Float timeInStatus;
	/**
	 * Time interval
	 */
	public DateTime timeInterval;
	public RegisteredGenerator GeneratingUnit;

	public UnitInitialConditions(){

	}
}//end UnitInitialConditions