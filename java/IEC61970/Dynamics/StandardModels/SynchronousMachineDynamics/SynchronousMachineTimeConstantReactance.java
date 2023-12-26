package IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PU;

/**
 * Synchronous machine detailed modelling types are defined by the combination of
 * the attributes SynchronousMachineTimeConstantReactance.modelType and
 * SynchronousMachineTimeConstantReactance.rotorType.
 * <b>
 * </b><b>Parameter notes:</b>
 * <ol>
 * 	<li>The "p" in the time-related attribute names is a substitution for a
 * "prime" in the usual parameter notation, e.g. tpdo refers to <b>T'do</b>.</li>
 * </ol>
 * <b>
 * </b>The parameters used for models expressed in time constant reactance form
 * include:
 * <ul>
 * 	<li>RotatingMachine.ratedS (MVAbase)</li>
 * 	<li>RotatingMachineDynamics.damping (D)</li>
 * 	<li>RotatingMachineDynamics.inertia (H)</li>
 * 	<li>RotatingMachineDynamics.saturationFactor (S1)</li>
 * 	<li>RotatingMachineDynamics.saturationFactor120 (S12)</li>
 * 	<li>RotatingMachineDynamics.statorLeakageReactance (Xl)</li>
 * 	<li>RotatingMachineDynamics.statorResistance (Rs)</li>
 * 	<li>SynchronousMachineTimeConstantReactance.ks (Ks)</li>
 * 	<li>SynchronousMachineDetailed.saturationFactorQAxis (S1q)</li>
 * 	<li>SynchronousMachineDetailed.saturationFactor120QAxis (S12q)</li>
 * 	<li>SynchronousMachineDetailed.efdBaseRatio</li>
 * 	<li>SynchronousMachineDetailed.ifdBaseType</li>
 * 	<li>SynchronousMachineDetailed.ifdBaseValue, if present</li>
 * 	<li>.xDirectSync (Xd)</li>
 * 	<li>.xDirectTrans (X'd)</li>
 * 	<li>.xDirectSubtrans (X''d)</li>
 * 	<li>.xQuadSync (Xq)</li>
 * 	<li>.xQuadTrans (X'q)</li>
 * 	<li>.xQuadSubtrans (X''q)</li>
 * 	<li>.tpdo (T'do)</li>
 * 	<li>.tppdo (T''do)</li>
 * 	<li>.tpqo (T'qo)</li>
 * 	<li>.tppqo (T''qo)</li>
 * 	<li>.tc.</li>
 * </ul>
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class SynchronousMachineTimeConstantReactance extends SynchronousMachineDetailed {

	/**
	 * Saturation loading correction factor (Ks) (>= 0).  Used only by Type J model.
	 * Typical Value = 0.
	 */
	public Float ks;
	/**
	 * Type of synchronous machine model used in Dynamic simulation applications.
	 */
	public SynchronousMachineModelKind modelType;
	/**
	 * Type of rotor on physical machine.
	 */
	public RotorKind rotorType;
	/**
	 * Damping time constant for "Canay" reactance.  Typical Value = 0.
	 */
	public Seconds tc;
	/**
	 * Direct-axis transient rotor time constant (T'do) (> T''do).  Typical Value = 5.
	 */
	public Seconds tpdo;
	/**
	 * Direct-axis subtransient rotor time constant (T''do) (> 0).  Typical Value = 0.
	 * 03.
	 */
	public Seconds tppdo;
	/**
	 * Quadrature-axis subtransient rotor time constant (T''qo) (> 0). Typical Value =
	 * 0.03.
	 */
	public Seconds tppqo;
	/**
	 * Quadrature-axis transient rotor time constant (T'qo) (> T''qo). Typical Value =
	 * 0.5.
	 */
	public Seconds tpqo;
	/**
	 * Direct-axis subtransient reactance (unsaturated) (X''d) (> Xl).  Typical Value
	 * = 0.2.
	 */
	public PU xDirectSubtrans;
	/**
	 * Direct-axis synchronous reactance (Xd) (>= X'd).
	 * The quotient of a sustained value of that AC component of armature voltage that
	 * is produced by the total direct-axis flux due to direct-axis armature current
	 * and the value of the AC component of this current, the machine running at rated
	 * speed. Typical Value = 1.8.
	 */
	public PU xDirectSync;
	/**
	 * Direct-axis transient reactance (unsaturated) (X'd) (> =X''d).  Typical Value =
	 * 0.5.
	 */
	public PU xDirectTrans;
	/**
	 * Quadrature-axis subtransient reactance (X''q) (> Xl).  Typical Value = 0.2.
	 */
	public PU xQuadSubtrans;
	/**
	 * Quadrature-axis synchronous reactance (Xq) (> =X'q).
	 * The ratio of the component of reactive armature voltage, due to the quadrature-
	 * axis component of armature current, to this component of current, under steady
	 * state conditions and at rated frequency.  Typical Value = 1.6.
	 */
	public PU xQuadSync;
	/**
	 * Quadrature-axis transient reactance (X'q) (> =X''q).  Typical Value = 0.3.
	 */
	public PU xQuadTrans;

	public SynchronousMachineTimeConstantReactance(){

	}
}//end SynchronousMachineTimeConstantReactance