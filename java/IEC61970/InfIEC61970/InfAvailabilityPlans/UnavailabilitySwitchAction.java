package IEC61970.InfIEC61970.InfAvailabilityPlans;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Wires.Switch;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Relevant switching action for supporting the availability (or unavailability)
 * plans.  This could open or close a switch that is not directly connected to the
 * unavailable equipment .
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class UnavailabilitySwitchAction extends IdentifiedObject {

	/**
	 * The switch is to be open during the scheduled period. 
	 */
	public Boolean open;
	public EquipmentUnavailabilitySchedule m_EquipmentUnavailabilitySchedule;
	public Switch m_Switch;

	public UnavailabilitySwitchAction(){

	}
}//end UnavailabilitySwitchAction