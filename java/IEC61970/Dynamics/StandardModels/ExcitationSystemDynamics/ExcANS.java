package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Italian excitation system. It represents static field voltage or excitation
 * current feedback excitation system.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcANS extends ExcitationSystemDynamics {

	/**
	 * Governor Control Flag (BLINT).
	 * 0 = lead-lag regulator
	 * 1 = proportional integral regulator.
	 * Typical Value = 0.
	 */
	public Integer blint;
	/**
	 * Minimum exciter current (I<sub>FMN</sub>).  Typical Value = -5.2.
	 */
	public PU ifmn;
	/**
	 * Maximum exciter current (I<sub>FMX</sub>).  Typical Value = 6.5.
	 */
	public PU ifmx;
	/**
	 * Exciter gain (K<sub>2</sub>).  Typical Value = 20.
	 */
	public Float k2;
	/**
	 * AVR gain (K<sub>3</sub>).  Typical Value = 1000.
	 */
	public Float k3;
	/**
	 * Ceiling factor (K<sub>CE</sub>).  Typical Value = 1.
	 */
	public Float kce;
	/**
	 * Feedback enabling (K<sub>RVECC</sub>).
	 * 0 = Open loop control
	 * 1 = Closed loop control.
	 * Typical Value = 1.
	 */
	public Integer krvecc;
	/**
	 * Rate feedback signal flag (K<sub>VFIF</sub>).
	 * 0 = output voltage of the exciter
	 * 1 = exciter field current.
	 * Typical Value = 0.
	 */
	public Integer kvfif;
	/**
	 * Time constant (T<sub>1</sub>).  Typical Value = 20.
	 */
	public Seconds t1;
	/**
	 * Time constant (T<sub>2</sub>).  Typical Value = 0.05.
	 */
	public Seconds t2;
	/**
	 * Time constant (T<sub>3</sub>).  Typical Value = 1.6.
	 */
	public Seconds t3;
	/**
	 * Exciter time constant (T<sub>B</sub>).  Typical Value = 0.04.
	 */
	public Seconds tb;
	/**
	 * Minimum AVR output (V<sub>RMN</sub>).  Typical Value = -5.2.
	 */
	public PU vrmn;
	/**
	 * Maximum AVR output (V<sub>RMX</sub>).  Typical Value = 6.5.
	 */
	public PU vrmx;

	public ExcANS(){

	}
}//end ExcANS