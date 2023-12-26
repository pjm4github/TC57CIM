package IEC61970.Base.Wires;

import IEC61970.Base.Core.PowerSystemResource;

/**
 * Represents the single phase information of an unbalanced energy source.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class EnergySourcePhase extends PowerSystemResource {

	/**
	 * Phase of this energy source component.   If the energy source wye connected,
	 * the connection is from the indicated phase to the central ground or neutral
	 * point.  If the energy source is delta connected, the phase indicates an energy
	 * source connected from the indicated phase to the next logical non-neutral phase.
	 */
	public SinglePhaseKind phase;
	/**
	 * The energy sourceto which the phase belongs.
	 */
	public EnergySource EnergySource;

	public EnergySourcePhase(){

	}
}//end EnergySourcePhase