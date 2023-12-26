package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Static PI transformer fed excitation system: ELIN (VATECH) - simplified model.
 * This model represents an all-static excitation system. A PI voltage controller
 * establishes a desired field current set point for a proportional current
 * controller. The integrator of the PI controller has a follow-up input to match
 * its signal to the present field current.  A power system stabilizer with power
 * input is included in the model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcELIN1 extends ExcitationSystemDynamics {

	/**
	 * Controller follow up dead band (Dpnf).  Typical Value = 0.
	 */
	public PU dpnf;
	/**
	 * Maximum open circuit excitation voltage (Efmax).  Typical Value = 5.
	 */
	public PU efmax;
	/**
	 * Minimum open circuit excitation voltage (Efmin).  Typical Value = -5.
	 */
	public PU efmin;
	/**
	 * Stabilizer Gain 1 (Ks1).  Typical Value = 0.
	 */
	public PU ks1;
	/**
	 * Stabilizer Gain 2 (Ks2).  Typical Value = 0.
	 */
	public PU ks2;
	/**
	 * Stabilizer Limit Output (smax).  Typical Value = 0.1.
	 */
	public PU smax;
	/**
	 * Current transducer time constant (Tfi).  Typical Value = 0.
	 */
	public Seconds tfi;
	/**
	 * Controller reset time constant (Tnu).  Typical Value = 2.
	 */
	public Seconds tnu;
	/**
	 * Stabilizer Phase Lag Time Constant (Ts1).  Typical Value = 1.
	 */
	public Seconds ts1;
	/**
	 * Stabilizer Filter Time Constant (Ts2).  Typical Value = 1.
	 */
	public Seconds ts2;
	/**
	 * Stabilizer parameters (Tsw).  Typical Value = 3.
	 */
	public Seconds tsw;
	/**
	 * Current controller gain (Vpi).  Typical Value = 12.45.
	 */
	public PU vpi;
	/**
	 * Controller follow up gain (Vpnf).  Typical Value = 2.
	 */
	public PU vpnf;
	/**
	 * Voltage controller proportional gain (Vpu).  Typical Value = 34.5.
	 */
	public PU vpu;
	/**
	 * Excitation transformer effective reactance (Xe) (>=0).  Xe represents the
	 * regulation of the transformer/rectifier unit.  Typical Value = 0.06.
	 */
	public PU xe;

	public ExcELIN1(){

	}
}//end ExcELIN1