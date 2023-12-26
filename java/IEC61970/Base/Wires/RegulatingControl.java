package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.PhaseCode;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * Specifies a set of equipment that works together to control a power system
 * quantity such as voltage or flow.
 * Remote bus voltage control is possible by specifying the controlled terminal
 * located at some place remote from the controlling equipment.
 * In case multiple equipment, possibly of different types, control same terminal
 * there must be only one RegulatingControl at that terminal. The most specific
 * subtype of RegulatingControl shall be used in case such equipment participate
 * in the control, e.g. TapChangerControl for tap changers.
 * For flow control  load sign convention is used, i.e. positive sign means flow
 * out from a TopologicalNode (bus) into the conducting equipment.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class RegulatingControl extends PowerSystemResource {

	/**
	 * The regulation is performed in a discrete mode. This applies to equipment with
	 * discrete controls, e.g. tap changers and shunt compensators.
	 */
	public Boolean discrete;
	/**
	 * The flag tells if regulation is enabled.
	 */
	public Boolean enabled;
	/**
	 * The regulating control mode presently available.  This specification allows for
	 * determining the kind of regulation without need for obtaining the units from a
	 * schedule.
	 */
	public RegulatingControlModeKind mode;
	/**
	 * Phase voltage controlling this regulator, measured at regulator location.
	 */
	public PhaseCode monitoredPhase;
	/**
	 * This is a deadband used with discrete control to avoid excessive update of
	 * controls like tap changers and shunt compensator banks while regulating.
	 * The units of those appropriate for the mode.
	 */
	public Float targetDeadband;
	/**
	 * The target value specified for case input.   This value can be used for the
	 * target value without the use of schedules. The value has the units appropriate
	 * to the mode attribute.
	 */
	public Float targetValue;
	/**
	 * Specify the multiplier for used for the targetValue.
	 */
	public UnitMultiplier targetValueUnitMultiplier;

	public RegulatingControl(){

	}
}//end RegulatingControl