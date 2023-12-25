package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.Integer;
import TC57CIM.IEC61970.Base.Core.PowerSystemResource;

/**
 * Single phase of a multi-phase shunt compensator when its attributes might be
 * different per phase.
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:29 PM
 */
public class ShuntCompensatorPhase extends PowerSystemResource {

	/**
	 * The maximum number of sections that may be switched in for this phase. 
	 */
	public Integer maximumSections;
	/**
	 * For the capacitor phase, the normal number of sections switched in.
	 */
	public Integer normalSections;
	/**
	 * Phase of this shunt compensator component.   If the shunt compensator is wye
	 * connected, the connection is from the indicated phase to the central ground or
	 * neutral point.  If the shunt compensator is delta connected, the phase
	 * indicates a shunt compensator connected from the indicated phase to the next
	 * logical non-neutral phase.
	 */
	public SinglePhaseKind phase;

	public ShuntCompensatorPhase(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}