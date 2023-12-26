package IEC61970.Dynamics.StandardModels.LoadDynamics;


/**
 * Type of static load model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public enum StaticLoadModelKind {
	/**
	 * Exponential P and Q equations are used and the following attributes are
	 * required:
	 * kp1, kp2, kp3, kpf, ep1, ep2, ep3
	 * kq1, kq2, kq3, kqf, eq1, eq2, eq3.
	 */
	exponential,
	/**
	 * ZIP1 P and Q equations are used and the following attributes are required:
	 * kp1, kp2, kp3, kpf
	 * kq1, kq2, kq3, kqf.
	 */
	zIP1,
	/**
	 * This model separates the frequency-dependent load (primarily motors) from other
	 * load.  ZIP2 P and Q equations are used and the following attributes are
	 * required:
	 * kp1, kp2, kp3, kq4, kpf
	 * kq1, kq2, kq3, kq4, kqf.
	 */
	zIP2,
	/**
	 * The load is represented as a constant impedance.  ConstantZ P and Q equations
	 * are used and no attributes are required.
	 */
	constantZ
}