package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type ST1A model. This model represents
 * systems in which excitation power is supplied through a transformer from the
 * generator terminals (or the unit's auxiliary bus) and is regulated by a
 * controlled rectifier.  The maximum exciter voltage available from such systems
 * is directly related to the generator terminal voltage.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 7.1.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEST1A extends ExcitationSystemDynamics {

	/**
	 * Exciter output current limit reference (I<sub>LR</sub>).  Typical Value = 0.
	 */
	public PU ilr;
	/**
	 * Voltage regulator gain (K<sub>A</sub>).  Typical Value = 190.
	 */
	public PU ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
	 * Typical Value = 0.08.
	 */
	public PU kc;
	/**
	 * Excitation control system stabilizer gains (K<sub>F</sub>).  Typical Value = 0.
	 */
	public PU kf;
	/**
	 * Exciter output current limiter gain (K<sub>LR</sub>).  Typical Value = 0.
	 */
	public PU klr;
	/**
	 * Selector of the Power System Stabilizer (PSS) input (PSSin).
	 * true = PSS input (Vs) added to error signal
	 * false = PSS input (Vs) added to voltage regulator output.
	 * Typical Value = true.
	 */
	public Boolean pssin;
	/**
	 * Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.
	 */
	public Seconds ta;
	/**
	 * Voltage regulator time constant (T<sub>B</sub>).  Typical Value = 10.
	 */
	public Seconds tb;
	/**
	 * Voltage regulator time constant (T<sub>B1</sub>).  Typical Value = 0.
	 */
	public Seconds tb1;
	/**
	 * Voltage regulator time constant (T<sub>C</sub>).  Typical Value = 1.
	 */
	public Seconds tc;
	/**
	 * Voltage regulator time constant (T<sub>C1</sub>).  Typical Value = 0.
	 */
	public Seconds tc1;
	/**
	 * Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
	 * Value = 1.
	 */
	public Seconds tf;
	/**
	 * Selector of the connection of the UEL input (UELin). Typical Value =
	 * ignoreUELsignal.
	 */
	public ExcIEEEST1AUELselectorKind uelin;
	/**
	 * Maximum voltage regulator output (V<sub>AMAX</sub>).  Typical Value = 14.5.
	 */
	public PU vamax;
	/**
	 * Minimum voltage regulator output (V<sub>AMIN</sub>).  Typical Value = -14.5.
	 */
	public PU vamin;
	/**
	 * Maximum voltage regulator input limit (V<sub>IMAX</sub>).  Typical Value = 999.
	 */
	public PU vimax;
	/**
	 * Minimum voltage regulator input limit (V<sub>IMIN</sub>).  Typical Value = -999.
	 */
	public PU vimin;
	/**
	 * Maximum voltage regulator outputs (V<sub>RMAX</sub>).  Typical Value = 7.8.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator outputs (V<sub>RMIN</sub>).  Typical Value = -6.7.
	 */
	public PU vrmin;

	public ExcIEEEST1A(){

	}
}//end ExcIEEEST1A