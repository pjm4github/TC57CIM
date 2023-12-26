package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified IEEE Type ST1 Excitation System with semi-continuous and acting
 * terminal voltage limiter.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcOEX3T extends ExcitationSystemDynamics {

	/**
	 * Saturation parameter (E<sub>1</sub>).
	 */
	public PU e1;
	/**
	 * Saturation parameter (E<sub>2</sub>).
	 */
	public PU e2;
	/**
	 * Gain (K<sub>A</sub>).
	 */
	public PU ka;
	/**
	 * Gain (K<sub>C</sub>).
	 */
	public PU kc;
	/**
	 * Gain (K<sub>D</sub>).
	 */
	public PU kd;
	/**
	 * Gain (K<sub>E</sub>).
	 */
	public PU ke;
	/**
	 * Gain (K<sub>F</sub>).
	 */
	public PU kf;
	/**
	 * Saturation parameter (S<sub>E</sub>(E<sub>1</sub>)).
	 */
	public PU see1;
	/**
	 * Saturation parameter (S<sub>E</sub>(E<sub>2</sub>)).
	 */
	public PU see2;
	/**
	 * Time constant (T<sub>1</sub>).
	 */
	public Seconds t1;
	/**
	 * Time constant (T<sub>2</sub>).
	 */
	public Seconds t2;
	/**
	 * Time constant (T<sub>3</sub>).
	 */
	public Seconds t3;
	/**
	 * Time constant (T<sub>4</sub>).
	 */
	public Seconds t4;
	/**
	 * Time constant (T<sub>5</sub>).
	 */
	public Seconds t5;
	/**
	 * Time constant (T<sub>6</sub>).
	 */
	public Seconds t6;
	/**
	 * Time constant (T<sub>E</sub>).
	 */
	public Seconds te;
	/**
	 * Time constant (T<sub>F</sub>).
	 */
	public Seconds tf;
	/**
	 * Limiter (V<sub>RMAX</sub>).
	 */
	public PU vrmax;
	/**
	 * Limiter (V<sub>RMIN</sub>). 
	 */
	public PU vrmin;

	public ExcOEX3T(){

	}
}//end ExcOEX3T