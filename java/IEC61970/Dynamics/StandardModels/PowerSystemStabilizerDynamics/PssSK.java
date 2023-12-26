package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * PSS Slovakian type - three inputs.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PssSK extends PowerSystemStabilizerDynamics {

	/**
	 * Gain P (K1).  Typical Value = -0.3.
	 */
	public PU k1;
	/**
	 * Gain fe (K2).  Typical Value = -0.15.
	 */
	public PU k2;
	/**
	 * Gain If (K3).  Typical Value = 10.
	 */
	public PU k3;
	/**
	 * Denominator time constant (T1).  Typical Value = 0.3.
	 */
	public Seconds t1;
	/**
	 * Filter time constant (T2).  Typical Value = 0.35.
	 */
	public Seconds t2;
	/**
	 * Denominator time constant (T3).  Typical Value = 0.22.
	 */
	public Seconds t3;
	/**
	 * Filter time constant (T4).  Typical Value = 0.02.
	 */
	public Seconds t4;
	/**
	 * Denominator time constant (T5).  Typical Value = 0.02.
	 */
	public Seconds t5;
	/**
	 * Filter time constant (T6).  Typical Value = 0.02.
	 */
	public Seconds t6;
	/**
	 * Stabilizer output max limit (Vsmax).  Typical Value = 0.4.
	 */
	public PU vsmax;
	/**
	 * Stabilizer output min limit (Vsmin).  Typical Value = -0.4.
	 */
	public PU vsmin;

	public PssSK(){

	}
}//end PssSK