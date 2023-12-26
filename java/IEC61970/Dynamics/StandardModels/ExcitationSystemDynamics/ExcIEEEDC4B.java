package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type DC4B model. These excitation
 * systems utilize a field-controlled dc commutator exciter with a continuously
 * acting voltage regulator having supplies obtained from the generator or
 * auxiliary bus.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 5.4.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEDC4B extends ExcitationSystemDynamics {

	/**
	 * Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>).
	 * Typical Value = 1.75.
	 */
	public PU efd1;
	/**
	 * Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>).
	 * Typical Value = 2.33.
	 */
	public PU efd2;
	/**
	 * Voltage regulator gain (K<sub>A</sub>).  Typical Value = 1.
	 */
	public PU ka;
	/**
	 * Regulator derivative gain (K<sub>D</sub>).  Typical Value = 20.
	 */
	public PU kd;
	/**
	 * Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
	 * = 1.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gain (K<sub>F</sub>).  Typical Value = 0.
	 */
	public PU kf;
	/**
	 * Regulator integral gain (K<sub>I</sub>).  Typical Value = 20.
	 */
	public PU ki;
	/**
	 * Regulator proportional gain (K<sub>P</sub>).  Typical Value = 20.
	 */
	public PU kp;
	/**
	 * OEL input (OELin).
	 * true = LV gate
	 * false = subtract from error signal.
	 * Typical Value = true.
	 */
	public Boolean oelin;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]).  Typical Value = 0.08.
	 */
	public Float seefd1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]).  Typical Value = 0.27.
	 */
	public Float seefd2;
	/**
	 * Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.2.
	 */
	public Seconds ta;
	/**
	 * Regulator derivative filter time constant(T<sub>D</sub>).  Typical Value = 0.01.
	 */
	public Seconds td;
	/**
	 * Exciter time constant, integration rate associated with exciter control
	 * (T<sub>E</sub>).  Typical Value = 0.8.
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
	 * Minimum exciter voltage output(V<sub>EMIN</sub>).  Typical Value = 0.
	 */
	public PU vemin;
	/**
	 * Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 2.7.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -0.9.
	 */
	public PU vrmin;

	public ExcIEEEDC4B(){

	}
}//end ExcIEEEDC4B