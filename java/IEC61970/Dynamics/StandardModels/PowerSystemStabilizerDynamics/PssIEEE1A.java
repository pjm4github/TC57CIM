package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type PSS1A power system stabilizer
 * model. PSS1A is the generalized form of a PSS with a single input. Some common
 * stabilizer input signals are speed, frequency, and power.
 * 
 * Reference: IEEE 1A 421.5-2005 Section 8.1.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PssIEEE1A extends PowerSystemStabilizerDynamics {

	/**
	 * PSS signal conditioning frequency filter constant (A1).  Typical Value = 0.061.
	 */
	public PU a1;
	/**
	 * PSS signal conditioning frequency filter constant (A2).  Typical Value = 0.0017.
	 */
	public PU a2;
	/**
	 * Type of input signal.  Typical Value = rotorAngularFrequencyDeviation.
	 */
	public InputSignalKind inputSignalType;
	/**
	 * Stabilizer gain (Ks).  Typical Value = 5.
	 */
	public PU ks;
	/**
	 * Lead/lag time constant (T1).  Typical Value = 0.3.
	 */
	public Seconds t1;
	/**
	 * Lead/lag time constant (T2).  Typical Value = 0.03.
	 */
	public Seconds t2;
	/**
	 * Lead/lag time constant (T3).  Typical Value = 0.3.
	 */
	public Seconds t3;
	/**
	 * Lead/lag time constant (T4).  Typical Value = 0.03.
	 */
	public Seconds t4;
	/**
	 * Washout time constant (T5).  Typical Value = 10.
	 */
	public Seconds t5;
	/**
	 * Transducer time constant (T6).  Typical Value = 0.01.
	 */
	public Seconds t6;
	/**
	 * Maximum stabilizer output (Vrmax).  Typical Value = 0.05.
	 */
	public PU vrmax;
	/**
	 * Minimum stabilizer output (Vrmin).  Typical Value = -0.05.
	 */
	public PU vrmin;

	public PssIEEE1A(){

	}
}//end PssIEEE1A