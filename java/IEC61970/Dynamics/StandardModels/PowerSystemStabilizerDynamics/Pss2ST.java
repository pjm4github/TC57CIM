package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * PTI Microprocessor-Based Stabilizer type 1.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class Pss2ST extends PowerSystemStabilizerDynamics {

	/**
	 * Type of input signal #1.  Typical Value = rotorAngularFrequencyDeviation.
	 */
	public InputSignalKind inputSignal1Type;
	/**
	 * Type of input signal #2.  Typical Value = generatorElectricalPower.
	 */
	public InputSignalKind inputSignal2Type;
	/**
	 * Gain (K1). 
	 */
	public PU k1;
	/**
	 * Gain (K2). 
	 */
	public PU k2;
	/**
	 * Limiter (Lsmax). 
	 */
	public PU lsmax;
	/**
	 * Limiter (Lsmin). 
	 */
	public PU lsmin;
	/**
	 * Time constant (T1). 
	 */
	public Seconds t1;
	/**
	 * Time constant (T10). 
	 */
	public Seconds t10;
	/**
	 * Time constant (T2).
	 */
	public Seconds t2;
	/**
	 * Time constant (T3). 
	 */
	public Seconds t3;
	/**
	 * Time constant (T4).
	 */
	public Seconds t4;
	/**
	 * Time constant (T5). 
	 */
	public Seconds t5;
	/**
	 * Time constant (T6). 
	 */
	public Seconds t6;
	/**
	 * Time constant (T7). 
	 */
	public Seconds t7;
	/**
	 * Time constant (T8). 
	 */
	public Seconds t8;
	/**
	 * Time constant (T9). 
	 */
	public Seconds t9;
	/**
	 * Cutoff limiter (Vcl). 
	 */
	public PU vcl;
	/**
	 * Cutoff limiter (Vcu). 
	 */
	public PU vcu;

	public Pss2ST(){

	}
}//end Pss2ST