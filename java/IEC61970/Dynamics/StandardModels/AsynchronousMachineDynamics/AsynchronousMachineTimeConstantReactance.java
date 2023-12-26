package IEC61970.Dynamics.StandardModels.AsynchronousMachineDynamics;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PU;

/**
 * <b>Parameter Notes:</b>
 * <ol>
 * 	<li>If <b>X''</b> = <b>X'</b>, a single cage (one equivalent rotor winding per
 * axis) is modelled.</li>
 * 	<li>The "p" in the attribute names is a substitution for a "prime" in the
 * usual parameter notation, e.g. tpo refers to T'o.</li>
 * </ol>
 * 
 * The parameters used for models expressed in time constant reactance form
 * include:
 * <ul>
 * 	<li>RotatingMachine.ratedS (MVAbase)</li>
 * 	<li>RotatingMachineDynamics.damping (D)</li>
 * 	<li>RotatingMachineDynamics.inertia (H)</li>
 * 	<li>RotatingMachineDynamics.saturationFactor (S1)</li>
 * 	<li>RotatingMachineDynamics.saturationFactor120 (S12)</li>
 * 	<li>RotatingMachineDynamics.statorLeakageReactance (Xl)</li>
 * 	<li>RotatingMachineDynamics.statorResistance (Rs)</li>
 * 	<li>.xs (Xs)</li>
 * 	<li>.xp (X')</li>
 * 	<li>.xpp (X'')</li>
 * 	<li>.tpo (T'o)</li>
 * 	<li>.tppo (T''o).</li>
 * </ul>
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class AsynchronousMachineTimeConstantReactance extends AsynchronousMachineDynamics {

	/**
	 * Transient rotor time constant (T'o) (> T''o).  Typical Value = 5.
	 */
	public Seconds tpo;
	/**
	 * Subtransient rotor time constant (T''o) (> 0).  Typical Value = 0.03.
	 */
	public Seconds tppo;
	/**
	 * Transient reactance (unsaturated) (X') (>=X'').  Typical Value = 0.5.
	 */
	public PU xp;
	/**
	 * Subtransient reactance (unsaturated) (X'') (> Xl).  Typical Value = 0.2.
	 */
	public PU xpp;
	/**
	 * Synchronous reactance (Xs) (>= X').  Typical Value = 1.8.
	 */
	public PU xs;

	public AsynchronousMachineTimeConstantReactance(){

	}
}//end AsynchronousMachineTimeConstantReactance