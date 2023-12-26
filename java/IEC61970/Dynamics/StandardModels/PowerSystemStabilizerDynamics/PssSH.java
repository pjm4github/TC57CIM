package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Model for Siemens "H infinity" power system stabilizer with generator
 * electrical power input.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PssSH extends PowerSystemStabilizerDynamics {

	/**
	 * Main gain (K).  Typical Value = 1.
	 */
	public PU k;
	/**
	 * Gain 0 (K0).  Typical Value = 0.012.
	 */
	public PU k0;
	/**
	 * Gain 1 (K1).  Typical Value = 0.488.
	 */
	public PU k1;
	/**
	 * Gain 2 (K2).  Typical Value = 0.064.
	 */
	public PU k2;
	/**
	 * Gain 3 (K3).  Typical Value = 0.224.
	 */
	public PU k3;
	/**
	 * Gain 4 (K4).  Typical Value = 0.1.
	 */
	public PU k4;
	/**
	 * Time constant 1 (T1).  Typical Value = 0.076.
	 */
	public Seconds t1;
	/**
	 * Time constant 2 (T2).  Typical Value = 0.086.
	 */
	public Seconds t2;
	/**
	 * Time constant 3 (T3).   Typical Value = 1.068.
	 */
	public Seconds t3;
	/**
	 * Time constant 4 (T4).  Typical Value = 1.913.
	 */
	public Seconds t4;
	/**
	 * Input time constant (Td).  Typical Value = 10.
	 */
	public Seconds td;
	/**
	 * Output maximum limit (Vsmax).  Typical Value = 0.1.
	 */
	public PU vsmax;
	/**
	 * Output minimum limit (Vsmin).  Typical Value = -0.1.
	 */
	public PU vsmin;

	public PssSH(){

	}
}//end PssSH