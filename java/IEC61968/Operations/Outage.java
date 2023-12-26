package IEC61968.Operations;

import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;
import IEC61968.Common.CrewStatusKind;
import IEC61970.Base.Faults.Fault;
import IEC61968.Metering.UsagePoint;
import IEC61970.Base.Wires.Switch;
import IEC61970.Base.Core.Equipment;
import IEC61968.Common.Document;
import IEC61968.Common.Crew;

/**
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class Outage extends Document {

	public DateTimeInterval actualPeriod;
	public String communityDescriptor;
	public Integer customersRestored;
	public DateTimeInterval estimatedPeriod;
	public Integer metersAffected;
	public Integer originalCustomersServed;
	public Integer originalMetersAffected;
	/**
	 * Defines if the outage has been verified or is only estimated.
	 */
	public OutageStatusKind outageKind;
	public CrewStatusKind statusKind;
	public ServicePointOutageSummary summary;
	public String utilityDisclaimer;
	/**
	 * All faults involved in this outage.
	 */
	public Fault Faults;
	/**
	 * all deenergized useage points associated with the outage. 
	 */
	public UsagePoint DeEnergizedUsagePoint;
	/**
	 * All potentially open switches causing this outage. This realationship is meant
	 * to be used as "indication" for initiation of outage-related business processes,
	 * whereas for actual actions of switches, SwitchAction-Switch relationship should
	 * be used.
	 */
	public Switch OpenedSwitches;
	/**
	 * All equipments associated with this outage.
	 */
	public Equipment Equipments;
	/**
	 * All energized usage points associated with this outage.
	 */
	public UsagePoint EnergizedUsagePoint;
	/**
	 * All switch actions to apply within the scope of this planned outage. Each such
	 * action groups switches to which the action is to apply in order to produce the
	 * desired network state considered as outage.
	 */
	public SwitchAction PlannedSwitchActions;
	public Crew Crew;

	public Outage(){

	}
}//end Outage