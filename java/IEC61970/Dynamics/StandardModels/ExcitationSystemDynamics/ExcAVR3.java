package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Italian excitation system. It represents exciter dynamo and electric regulator.
 * 
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcAVR3 extends ExcitationSystemDynamics {

	/**
	 * Field voltage value 1 (E1).  Typical Value = 4.18.
	 */
	public PU e1;
	/**
	 * Field voltage value 2 (E2).  Typical Value = 3.14.
	 */
	public PU e2;
	/**
	 * AVR gain (K<sub>A</sub>).  Typical Value = 100.
	 */
	public Float ka;
	/**
	 * Saturation factor at E1 (S(E1)).  Typical Value = 0.1.
	 */
	public Float se1;
	/**
	 * Saturation factor at E2 (S(E2)).  Typical Value = 0.03.
	 */
	public Float se2;
	/**
	 * AVR time constant (T<sub>1</sub>).  Typical Value = 20.
	 */
	public Seconds t1;
	/**
	 * AVR time constant (T<sub>2</sub>).  Typical Value = 1.6.
	 */
	public Seconds t2;
	/**
	 * AVR time constant (T<sub>3</sub>).  Typical Value = 0.66.
	 */
	public Seconds t3;
	/**
	 * AVR time constant (T<sub>4</sub>).  Typical Value = 0.07.
	 */
	public Seconds t4;
	/**
	 * Exciter time constant (T<sub>E</sub>).  Typical Value = 1.
	 */
	public Seconds te;
	/**
	 * Minimum AVR output (V<sub>RMN</sub>).  Typical Value = -7.5.
	 */
	public PU vrmn;
	/**
	 * Maximum AVR output (V<sub>RMX</sub>).  Typical Value = 7.5.
	 */
	public PU vrmx;

	public ExcAVR3(){

	}
}//end ExcAVR3