package IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics;

import IEC61970.Base.Domain.PU;

/**
 * The electrical equations for all variations of the synchronous models are based
 * on the SynchronousEquivalentCircuit diagram for the direct and quadrature axes.
 * 
 * 
 * <b>Equations for conversion between Equivalent Circuit and Time Constant
 * Reactance forms:</b>
 * <b>Xd</b> = <b>Xad</b> + <b>Xl</b>
 * <b>X'd</b> = <b>Xl</b> + <b>Xad</b> * <b>Xfd</b> / (<b>Xad</b> + <b>Xfd</b>)
 * <b>X"d</b> = <b>Xl</b> + <b>Xad</b> * <b>Xfd </b>* <b>X1d</b> / (<b>Xad</b> *
 * <b>Xfd</b> + <b>Xad</b> * <b>X1d</b> + <b>Xfd</b> * <b>X1d</b>)
 * <b>Xq</b> = <b>Xaq</b> + <b>Xl</b>
 * <b>X'q</b> = <b>Xl</b> + <b>Xaq</b> * <b>X1q</b> / (<b>Xaq</b>+ <b>X1q</b>)
 * <b>X"q</b> = <b>Xl</b> + <b>Xaq</b> *<b> X1q</b>* <b>X2q</b> / (<b>Xaq</b> *
 * <b>X1q</b> + <b>Xaq</b> * <b>X2q</b> + <b>X1q</b> * <b>X2q</b>)
 * <b>T'do</b> = (<b>Xad</b> + <b>Xfd</b>) / (<b>omega</b><b><sub>0</sub></b> *
 * <b>Rfd</b>)
 * <b>T"do</b> = (<b>Xad</b> * <b>Xfd</b> + <b>Xad</b> * <b>X1d</b> + <b>Xfd</b> *
 * <b>X1d</b>) / (<b>omega</b><b><sub>0</sub></b> * <b>R1d</b> * (<b>Xad</b> +
 * <b>Xfd</b>)
 * <b>T'qo</b> = (<b>Xaq</b> + <b>X1q</b>) / (<b>omega</b><b><sub>0</sub></b> *
 * <b>R1q</b>)
 * <b>T"qo</b> = (<b>Xaq</b> * <b>X1q</b> + <b>Xaq</b> * <b>X2q</b> + <b>X1q</b> *
 * <b>X2q</b>)/ (<b>omega</b><b><sub>0</sub></b> * <b>R2q</b> * (<b>Xaq</b> +
 * <b>X1q</b>)
 * <b>
 * </b>Same equations using CIM attributes from
 * SynchronousMachineTimeConstantReactance class on left of = sign and
 * SynchronousMachineEquivalentCircuit class on right (except as noted):
 * xDirectSync = xad + RotatingMachineDynamics.statorLeakageReactance
 * xDirectTrans = RotatingMachineDynamics.statorLeakageReactance + xad * xfd /
 * (xad + xfd)
 * xDirectSubtrans = RotatingMachineDynamics.statorLeakageReactance + xad * xfd *
 * x1d / (xad * xfd + xad * x1d + xfd * x1d)
 * xQuadSync = xaq + RotatingMachineDynamics.statorLeakageReactance
 * xQuadTrans = RotatingMachineDynamics.statorLeakageReactance + xaq * x1q / (xaq+
 * x1q)
 * xQuadSubtrans = RotatingMachineDynamics.statorLeakageReactance + xaq * x1q* x2q
 * / (xaq * x1q + xaq * x2q + x1q * x2q)
 * tpdo = (xad + xfd) / (2*pi*nominal frequency * rfd)
 * tppdo = (xad * xfd + xad * x1d + xfd * x1d) / (2*pi*nominal frequency * r1d *
 * (xad + xfd)
 * tpqo = (xaq + x1q) / (2*pi*nominal frequency * r1q)
 * tppqo = (xaq * x1q + xaq * x2q + x1q * x2q)/ (2*pi*nominal frequency * r2q *
 * (xaq + x1q).
 * 
 * Are only valid for a simplified model where "Canay" reactance is zero.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class SynchronousMachineEquivalentCircuit extends SynchronousMachineDetailed {

	/**
	 * D-axis damper 1 winding resistance.
	 */
	public PU r1d;
	/**
	 * Q-axis damper 1 winding resistance.
	 */
	public PU r1q;
	/**
	 * Q-axis damper 2 winding resistance.
	 */
	public PU r2q;
	/**
	 * Field winding resistance.
	 */
	public PU rfd;
	/**
	 * D-axis damper 1 winding leakage reactance.
	 */
	public PU x1d;
	/**
	 * Q-axis damper 1 winding leakage reactance.
	 */
	public PU x1q;
	/**
	 * Q-axis damper 2 winding leakage reactance.
	 */
	public PU x2q;
	/**
	 * D-axis mutual reactance.
	 */
	public PU xad;
	/**
	 * Q-axis mutual reactance.
	 */
	public PU xaq;
	/**
	 * Differential mutual ("Canay") reactance.
	 */
	public PU xf1d;
	/**
	 * Field winding leakage reactance.
	 */
	public PU xfd;

	public SynchronousMachineEquivalentCircuit(){

	}
}//end SynchronousMachineEquivalentCircuit