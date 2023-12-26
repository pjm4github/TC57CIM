package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Dual input Power System Stabilizer, based on IEEE type 2, with modified output
 * limiter defined by WECC (Western Electricity Coordinating Council, USA).
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PssWECC extends PowerSystemStabilizerDynamics {

	/**
	 * Type of input signal #1.
	 */
	public InputSignalKind inputSignal1Type;
	/**
	 * Type of input signal #2.
	 */
	public InputSignalKind inputSignal2Type;
	/**
	 * Input signal 1 gain  (K<sub>1</sub>). 
	 */
	public PU k1;
	/**
	 * Input signal 2 gain (K<sub>2</sub>). 
	 */
	public PU k2;
	/**
	 * Input signal 1 transducer time constant (T<sub>1</sub>).
	 */
	public Seconds t1;
	/**
	 * Lag time constant (T<sub>10</sub>). 
	 */
	public Seconds t10;
	/**
	 * Input signal 2 transducer time constant (T<sub>2</sub>). 
	 */
	public Seconds t2;
	/**
	 * Stabilizer washout time constant (T<sub>3</sub>). 
	 */
	public Seconds t3;
	/**
	 * Stabilizer washout time lag constant (T<sub>4</sub>) (>0).
	 */
	public Seconds t4;
	/**
	 * Lead time constant (T<sub>5</sub>). 
	 */
	public Seconds t5;
	/**
	 * Lag time constant (T<sub>6</sub>). 
	 */
	public Seconds t6;
	/**
	 * Lead time constant (T<sub>7</sub>). 
	 */
	public Seconds t7;
	/**
	 * Lag time constant (T<sub>8</sub>). 
	 */
	public Seconds t8;
	/**
	 * Lead time constant (T<sub>9</sub>). 
	 */
	public Seconds t9;
	/**
	 * Minimum value for voltage compensator output (V<sub>CL</sub>). 
	 */
	public PU vcl;
	/**
	 * Maximum value for voltage compensator output (V<sub>CU</sub>). 
	 */
	public PU vcu;
	/**
	 * Maximum output signal (Vsmax). 
	 */
	public PU vsmax;
	/**
	 * Minimum output signal (Vsmin). 
	 */
	public PU vsmin;

	public PssWECC(){

	}
}//end PssWECC