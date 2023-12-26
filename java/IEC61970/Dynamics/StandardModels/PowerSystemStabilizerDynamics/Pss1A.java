package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;

/**
 * Single input power system stabilizer. It is a modified version in order to
 * allow representation of various vendors' implementations on PSS type 1A.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class Pss1A extends PowerSystemStabilizerDynamics {

	/**
	 * Notch filter parameter (A1).
	 */
	public PU a1;
	/**
	 * Notch filter parameter (A2). 
	 */
	public PU a2;
	/**
	 * Notch filter parameter (A3). 
	 */
	public PU a3;
	/**
	 * Notch filter parameter (A4). 
	 */
	public PU a4;
	/**
	 * Notch filter parameter (A5). 
	 */
	public PU a5;
	/**
	 * Notch filter parameter (A6). 
	 */
	public PU a6;
	/**
	 * Notch filter parameter (A7). 
	 */
	public PU a7;
	/**
	 * Notch filter parameter (A8). 
	 */
	public PU a8;
	/**
	 * Type of input signal.
	 */
	public InputSignalKind inputSignalType;
	/**
	 * Selector (Kd).
	 * true = e<sup>-sTdelay</sup> used
	 * false = e<sup>-sTdelay</sup> not used.
	 */
	public Boolean kd;
	/**
	 * Stabilizer gain (Ks). 
	 */
	public PU ks;
	/**
	 * Lead/lag time constant (T1). 
	 */
	public Seconds t1;
	/**
	 * Lead/lag time constant (T2). 
	 */
	public Seconds t2;
	/**
	 * Lead/lag time constant (T3). 
	 */
	public Seconds t3;
	/**
	 * Lead/lag time constant (T4). 
	 */
	public Seconds t4;
	/**
	 * Washout time constant (T5). 
	 */
	public Seconds t5;
	/**
	 * Transducer time constant (T6). 
	 */
	public Seconds t6;
	/**
	 * Time constant (Tdelay). 
	 */
	public Seconds tdelay;
	/**
	 * Stabilizer input cutoff threshold (Vcl). 
	 */
	public PU vcl;
	/**
	 * Stabilizer input cutoff threshold (Vcu). 
	 */
	public PU vcu;
	/**
	 * Maximum stabilizer output (Vrmax). 
	 */
	public PU vrmax;
	/**
	 * Minimum stabilizer output (Vrmin). 
	 */
	public PU vrmin;

	public Pss1A(){

	}
}//end Pss1A