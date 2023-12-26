package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type PSS3B power system stabilizer
 * model. The PSS model PSS3B has dual inputs of electrical power and rotor
 * angular frequency deviation. The signals are used to derive an equivalent
 * mechanical power signal.
 * 
 * Reference: IEEE 3B 421.5-2005 Section 8.3.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PssIEEE3B extends PowerSystemStabilizerDynamics {

	/**
	 * Notch filter parameter (A1).  Typical Value = 0.359.
	 */
	public PU a1;
	/**
	 * Notch filter parameter (A2).  Typical Value = 0.586.
	 */
	public PU a2;
	/**
	 * Notch filter parameter (A3).  Typical Value = 0.429.
	 */
	public PU a3;
	/**
	 * Notch filter parameter (A4).  Typical Value = 0.564.
	 */
	public PU a4;
	/**
	 * Notch filter parameter (A5).  Typical Value = 0.001.
	 */
	public PU a5;
	/**
	 * Notch filter parameter (A6).  Typical Value = 0.
	 */
	public PU a6;
	/**
	 * Notch filter parameter (A7).  Typical Value = 0.031.
	 */
	public PU a7;
	/**
	 * Notch filter parameter (A8).  Typical Value = 0.
	 */
	public PU a8;
	/**
	 * Type of input signal #1.  Typical Value = generatorElectricalPower.
	 */
	public InputSignalKind inputSignal1Type;
	/**
	 * Type of input signal #2.  Typical Value = rotorSpeed.
	 */
	public InputSignalKind inputSignal2Type;
	/**
	 * Gain on signal # 1 (Ks1).  Typical Value = -0.602.
	 */
	public PU ks1;
	/**
	 * Gain on signal # 2 (Ks2).  Typical Value = 30.12.
	 */
	public PU ks2;
	/**
	 * Transducer time constant (T1).  Typical Value = 0.012.
	 */
	public Seconds t1;
	/**
	 * Transducer time constant (T2).  Typical Value = 0.012.
	 */
	public Seconds t2;
	/**
	 * Washout time constant (Tw1).  Typical Value = 0.3.
	 */
	public Seconds tw1;
	/**
	 * Washout time constant (Tw2).  Typical Value = 0.3.
	 */
	public Seconds tw2;
	/**
	 * Washout time constant (Tw3).  Typical Value = 0.6.
	 */
	public Seconds tw3;
	/**
	 * Stabilizer output max limit (Vstmax).  Typical Value = 0.1.
	 */
	public PU vstmax;
	/**
	 * Stabilizer output min limit (Vstmin).  Typical Value = -0.1.
	 */
	public PU vstmin;

	public PssIEEE3B(){

	}
}//end PssIEEE3B