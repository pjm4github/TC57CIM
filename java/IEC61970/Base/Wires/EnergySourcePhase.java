package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Core.PowerSystemResource;

/**
 * Represents the single phase information of an unbalanced energy source.
 * @author 222206
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
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

	public void finalize() throws Throwable {
		super.finalize();
	}

}