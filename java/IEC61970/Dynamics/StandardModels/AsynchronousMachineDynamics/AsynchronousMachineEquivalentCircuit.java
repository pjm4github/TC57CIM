package IEC61970.Dynamics.StandardModels.AsynchronousMachineDynamics;

import IEC61970.Base.Domain.PU;

/**
 * The electrical equations of all variations of the asynchronous model are based
 * on the AsynchronousEquivalentCircuit diagram for the direct and quadrature axes,
 * with two equivalent rotor windings in each axis.
 * 
 * <b>Equations for conversion between Equivalent Circuit and Time Constant
 * Reactance forms:</b>
 * <b>Xs</b> = <b>Xm</b> + <b>Xl</b>
 * <b>X'</b> = <b>Xl</b> + <b>Xm</b> * <b>Xlr1</b> / (<b>Xm</b> + <b>Xlr1</b>)
 * <b>X''</b> = <b>Xl</b> + <b>Xm</b> * <b>Xlr1</b>* <b>Xlr2</b> / (<b>Xm</b> *
 * <b>Xlr1</b> + <b>Xm</b> * <b>Xlr2</b> + <b>Xlr1</b> * <b>Xlr2</b>)
 * <b>T'o</b> = (<b>Xm</b> + <b>Xlr1</b>) / (<b>omega</b><b><sub>0</sub></b> *
 * <b>Rr1</b>)
 * <b>T''o</b> = (<b>Xm</b> * <b>Xlr1</b> + <b>Xm</b> * <b>Xlr2</b> + <b>Xlr1</b>
 * * <b>Xlr2</b>) / (<b>omega</b><b><sub>0</sub></b> * <b>Rr2</b> * (<b>Xm </b>+
 * <b>Xlr1</b>)
 * <b>
 * </b>Same equations using CIM attributes from
 * AsynchronousMachineTimeConstantReactance class on left of = sign and
 * AsynchronousMachineEquivalentCircuit class on right (except as noted):
 * xs = xm + RotatingMachineDynamics.statorLeakageReactance
 * xp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1 / (xm + xlr1)
 * xpp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1* xlr2 / (xm *
 * xlr1 + xm * xlr2 + xlr1 * xlr2)
 * tpo = (xm + xlr1) / (2*pi*nominal frequency * rr1)
 * tppo = (xm * xlr1 + xm * xlr2 + xlr1 * xlr2) / (2*pi*nominal frequency * rr2 *
 * (xm + xlr1).
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class AsynchronousMachineEquivalentCircuit extends AsynchronousMachineDynamics {

	/**
	 * Damper 1 winding resistance.
	 */
	public PU rr1;
	/**
	 * Damper 2 winding resistance.
	 */
	public PU rr2;
	/**
	 * Damper 1 winding leakage reactance.
	 */
	public PU xlr1;
	/**
	 * Damper 2 winding leakage reactance.
	 */
	public PU xlr2;
	/**
	 * Magnetizing reactance.
	 */
	public PU xm;

	public AsynchronousMachineEquivalentCircuit(){

	}
}//end AsynchronousMachineEquivalentCircuit