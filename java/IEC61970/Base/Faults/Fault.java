package IEC61970.Base.Faults;

import IEC61970.Base.Core.PhaseCode;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61970.Base.Core.Equipment;
import IEC61968.Common.Location;

/**
 * Abnormal condition causing current flow through conducting equipment, such as
 * caused by equipment failure or short circuits from objects not typically
 * modeled (for example, a tree falling on a line).
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class Fault extends IdentifiedObject {

	/**
	 * Fault impedance. Its usage is described by 'kind'.
	 */
	public FaultImpedance impedance;
	/**
	 * The kind of phase fault.
	 */
	public PhaseConnectedFaultKind kind;
	/**
	 * The date and time at which the fault occurred.
	 */
	public DateTime occurredDateTime;
	/**
	 * The phases participating in the fault. The fault connections into these phases
	 * are further specified by the type of fault.
	 */
	public PhaseCode phases;
	/**
	 * Equipment carrying this fault.
	 */
	public Equipment FaultyEquipment;
	/**
	 * All types of fault cause.
	 */
	public FaultCauseType FaultCauseTypes;
	public Location Location;

	public Fault(){

	}
}//end Fault