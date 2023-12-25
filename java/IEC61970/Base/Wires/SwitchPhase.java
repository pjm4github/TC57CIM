package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.Boolean;
import TC57CIM.IEC61970.Base.Core.PowerSystemResource;

/**
 * Single phase of a multi-phase switch when its attributes might be different per
 * phase.
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:29 PM
 */
public class SwitchPhase extends PowerSystemResource {

	/**
	 * The attribute tells if the switch is considered closed when used as input to
	 * topology processing.
	 */
	public Boolean closed;
	/**
	 * Used in cases when no Measurement for the status value is present. If the
	 * SwitchPhase has a status measurement the Discrete.normalValue is expected to
	 * match with this value.
	 */
	public Boolean normalOpen;
	/**
	 * Phase of this SwitchPhase on the side with terminal sequence number equal 1.
	 * Should be a phase contained in that terminal&rsquo;s phases attribute.
	 */
	public SinglePhaseKind phaseSide1;
	/**
	 * Phase of this SwitchPhase on the side with terminal sequence number equal 2.
	 * Should be a phase contained in that terminal&rsquo;s Terminal.phases attribute.
	 */
	public SinglePhaseKind phaseSide2;

	public SwitchPhase(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}