package IEC61970.Dynamics.StandardModels.VoltageAdjusterDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PU;

/**
 * The class represents IEEE Voltage Adjuster which is used to represent the
 * voltage adjuster in either a power factor or var control system.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 11.1.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class VAdjIEEE extends VoltageAdjusterDynamics {

	/**
	 * Rate at which output of adjuster changes (<i>ADJ_SLEW</i>).  Unit = sec./PU.
	 * Typical Value = 300.
	 */
	public Float adjslew;
	/**
	 * Time that adjuster pulses are off (<i>T</i><i><sub>AOFF</sub></i>).  Typical
	 * Value = 0.5.
	 */
	public Seconds taoff;
	/**
	 * Time that adjuster pulses are on (<i>T</i><i><sub>AON</sub></i>).  Typical
	 * Value = 0.1.
	 */
	public Seconds taon;
	/**
	 * Set high to provide a continuous raise or lower
	 * (<i>V</i><i><sub>ADJF</sub></i>).
	 */
	public Float vadjf;
	/**
	 * Maximum output of the adjuster (<i>V</i><i><sub>ADJMAX</sub></i>).  Typical
	 * Value = 1.1.
	 */
	public PU vadjmax;
	/**
	 * Minimum output of the adjuster (<i>V</i><i><sub>ADJMIN</sub></i>).  Typical
	 * Value = 0.9.
	 */
	public PU vadjmin;

	public VAdjIEEE(){

	}
}//end VAdjIEEE