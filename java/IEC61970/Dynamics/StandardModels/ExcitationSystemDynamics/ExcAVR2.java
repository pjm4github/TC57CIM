package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Italian excitation system corresponding to IEEE (1968) Type 2 Model. It
 * represents alternator and rotating diodes and electromechanic voltage
 * regulators.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcAVR2 extends ExcitationSystemDynamics {

	/**
	 * Field voltage value 1 (E1).  Typical Value = 4.18.
	 */
	public PU e1;
	/**
	 * Field voltage value 2 (E2).  Typical Value = 3.14.
	 */
	public PU e2;
	/**
	 * AVR gain (K<sub>A</sub>).  Typical Value = 500.
	 */
	public Float ka;
	/**
	 * Rate feedback gain (K<sub>F</sub>).  Typical Value = 0.12.
	 */
	public Float kf;
	/**
	 * Saturation factor at E1 (S(E1)).  Typical Value = 0.1.
	 */
	public Float se1;
	/**
	 * Saturation factor at E2 (S(E2)).  Typical Value = 0.03.
	 */
	public Float se2;
	/**
	 * AVR time constant (T<sub>A</sub>).  Typical Value = 0.02.
	 */
	public Seconds ta;
	/**
	 * AVR time constant (T<sub>B</sub>).  Typical Value = 0.
	 */
	public Seconds tb;
	/**
	 * Exciter time constant (T<sub>E</sub>).  Typical Value = 1.
	 */
	public Seconds te;
	/**
	 * Rate feedback time constant (T<sub>F1</sub>).  Typical Value = 1.
	 */
	public Seconds tf1;
	/**
	 * Rate feedback time constant (T<sub>F2</sub>).  Typical Value = 1.
	 */
	public Seconds tf2;
	/**
	 * Minimum AVR output (V<sub>RMN</sub>).  Typical Value = -6.
	 */
	public PU vrmn;
	/**
	 * Maximum AVR output (V<sub>RMX</sub>).  Typical Value = 7.
	 */
	public PU vrmx;

	public ExcAVR2(){

	}
}//end ExcAVR2