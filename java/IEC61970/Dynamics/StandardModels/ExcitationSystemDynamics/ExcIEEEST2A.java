package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Boolean;

/**
 * The class represents IEEE Std 421.5-2005 type ST2A model. Some static systems
 * utilize both current and voltage sources (generator terminal quantities) to
 * comprise the power source.  The regulator controls the exciter output through
 * controlled saturation of the power transformer components.  These compound-
 * source rectifier excitation systems are designated Type ST2A and are
 * represented by ExcIEEEST2A.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 7.2.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEST2A extends ExcitationSystemDynamics {

	/**
	 * Maximum field voltage (E<sub>FDMax</sub>).  Typical Value = 99.
	 */
	public PU efdmax;
	/**
	 * Voltage regulator gain (K<sub>A</sub>).  Typical Value = 120.
	 */
	public PU ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
	 * Typical Value = 1.82.
	 */
	public PU kc;
	/**
	 * Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
	 * = 1.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gains (K<sub>F</sub>).  Typical Value = 0.
	 * 05.
	 */
	public PU kf;
	/**
	 * Potential circuit gain coefficient (K<sub>I</sub>).  Typical Value = 8.
	 */
	public PU ki;
	/**
	 * Potential circuit gain coefficient (K<sub>P</sub>).  Typical Value = 4.88.
	 */
	public PU kp;
	/**
	 * Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.15.
	 */
	public Seconds ta;
	/**
	 * Exciter time constant, integration rate associated with exciter control
	 * (T<sub>E</sub>).  Typical Value = 0.5.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
	 * Value = 1.
	 */
	public Seconds tf;
	/**
	 * UEL input (UELin).
	 * true = HV gate
	 * false = add to error signal.
	 * Typical Value = true.
	 */
	public Boolean uelin;
	/**
	 * Maximum voltage regulator outputs (V<sub>RMAX</sub>).  Typical Value = 1.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator outputs (V<sub>RMIN</sub>).  Typical Value = 0.
	 */
	public PU vrmin;

	public ExcIEEEST2A(){

	}
}//end ExcIEEEST2A