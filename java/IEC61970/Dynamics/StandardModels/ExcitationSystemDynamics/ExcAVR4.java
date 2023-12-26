package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PU;

/**
 * Italian excitation system. It represents static exciter and electric voltage
 * regulator.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcAVR4 extends ExcitationSystemDynamics {

	/**
	 * AVR output voltage dependency selector (Imul).
	 * true = selector is connected
	 * false = selector is not connected.
	 * Typical Value = true.
	 */
	public Boolean imul;
	/**
	 * AVR gain (K<sub>A</sub>).  Typical Value = 300.
	 */
	public Float ka;
	/**
	 * Exciter gain (K<sub>E</sub>).  Typical Value = 1.
	 */
	public Float ke;
	/**
	 * Exciter internal reactance (K<sub>IF</sub>).  Typical Value = 0.
	 */
	public Float kif;
	/**
	 * AVR time constant (T<sub>1</sub>).  Typical Value = 4.8.
	 */
	public Seconds t1;
	/**
	 * Exciter current feedback time constant (T<sub>1IF</sub>).  Typical Value = 60.
	 */
	public Seconds t1if;
	/**
	 * AVR time constant (T<sub>2</sub>).  Typical Value = 1.5.
	 */
	public Seconds t2;
	/**
	 * AVR time constant (T<sub>3</sub>).  Typical Value = 0.
	 */
	public Seconds t3;
	/**
	 * AVR time constant (T<sub>4</sub>).  Typical Value = 0.
	 */
	public Seconds t4;
	/**
	 * Exciter current feedback time constant (T<sub>IF</sub>).  Typical Value = 0.
	 */
	public Seconds tif;
	/**
	 * Minimum exciter output (V<sub>FMN</sub>).  Typical Value = 0.
	 */
	public PU vfmn;
	/**
	 * Maximum exciter output (V<sub>FMX</sub>).  Typical Value = 5.
	 */
	public PU vfmx;
	/**
	 * Minimum AVR output (V<sub>RMN</sub>).  Typical Value = 0.
	 */
	public PU vrmn;
	/**
	 * Maximum AVR output (V<sub>RMX</sub>).  Typical Value = 5.
	 */
	public PU vrmx;

	public ExcAVR4(){

	}
}//end ExcAVR4