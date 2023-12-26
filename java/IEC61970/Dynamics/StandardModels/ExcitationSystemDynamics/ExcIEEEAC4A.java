package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type AC4A model. The model represents
 * type AC4A alternator-supplied controlled-rectifier excitation system which is
 * quite different from the other type ac systems. This high initial response
 * excitation system utilizes a full thyristor bridge in the exciter output
 * circuit.  The voltage regulator controls the firing of the thyristor bridges.
 * The exciter alternator uses an independent voltage regulator to control its
 * output voltage to a constant value. These effects are not modeled; however,
 * transient loading effects on the exciter alternator are included.
 * 
 * 
 * Reference: IEEE Standard 421.5-2005 Section 6.4.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEAC4A extends ExcitationSystemDynamics {

	/**
	 * Voltage regulator gain (K<sub>A</sub>).  Typical Value = 200.
	 */
	public PU ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
	 * Typical Value = 0.
	 */
	public PU kc;
	/**
	 * Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.015.
	 */
	public Seconds ta;
	/**
	 * Voltage regulator time constant (T<sub>B</sub>).  Typical Value = 10.
	 */
	public Seconds tb;
	/**
	 * Voltage regulator time constant (T<sub>C</sub>).  Typical Value = 1.
	 */
	public Seconds tc;
	/**
	 * Maximum voltage regulator input limit (V<sub>IMAX</sub>).  Typical Value = 10.
	 */
	public PU vimax;
	/**
	 * Minimum voltage regulator input limit (V<sub>IMIN</sub>).  Typical Value = -10.
	 */
	public PU vimin;
	/**
	 * Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 5.64.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -4.53.
	 */
	public PU vrmin;

	public ExcIEEEAC4A(){

	}
}//end ExcIEEEAC4A