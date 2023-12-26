package IEC61970.Dynamics.StandardModels;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PU;

/**
 * Abstract parent class for all synchronous and asynchronous machine standard
 * models.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class RotatingMachineDynamics extends DynamicsFunctionBlock {

	/**
	 * Damping torque coefficient (D).  A proportionality constant that, when
	 * multiplied by the angular velocity of the rotor poles with respect to the
	 * magnetic field (frequency), results in the damping torque.  This value is often
	 * zero when the sources of damping torques (generator damper windings, load
	 * damping effects, etc.) are modelled in detail.  Typical Value = 0.
	 */
	public Float damping;
	/**
	 * Inertia constant of generator or motor and mechanical load (H) (>0).  This is
	 * the specification for the stored energy in the rotating mass when operating at
	 * rated speed.  For a generator, this includes the generator plus all other
	 * elements (turbine, exciter) on the same shaft and has units of MW*sec.  For a
	 * motor, it includes the motor plus its mechanical load. Conventional units are
	 * per unit on the generator MVA base, usually expressed as MW*second/MVA or just
	 * second.   This value is used in the accelerating power reference frame for
	 * operator training simulator solutions.  Typical Value = 3.
	 */
	public Seconds inertia;
	/**
	 * Saturation factor at rated terminal voltage (S1) (> or =0).  Not used by
	 * simplified model.  Defined by defined by S(E1) in the
	 * SynchronousMachineSaturationParameters diagram.  Typical Value = 0.02.
	 */
	public Float saturationFactor;
	/**
	 * Saturation factor at 120% of rated terminal voltage (S12) (> or =S1). Not used
	 * by the simplified model, defined by S(E2) in the
	 * SynchronousMachineSaturationParameters diagram.  Typical Value = 0.12.
	 */
	public Float saturationFactor120;
	/**
	 * Stator leakage reactance (Xl) (> or =0). Typical Value = 0.15.
	 */
	public PU statorLeakageReactance;
	/**
	 * Stator (armature) resistance (Rs) (> or =0). Typical Value = 0.005.
	 */
	public PU statorResistance;

	public RotatingMachineDynamics(){

	}
}//end RotatingMachineDynamics