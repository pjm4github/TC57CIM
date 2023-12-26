package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type AC5A model. The model represents
 * a simplified model for brushless excitation systems. The regulator is supplied
 * from a source, such as a permanent magnet generator, which is not affected by
 * system disturbances.  Unlike other ac models, this model uses loaded rather
 * than open circuit exciter saturation data in the same way as it is used for the
 * dc models.  Because the model has been widely implemented by the industry, it
 * is sometimes used to represent other types of systems when either detailed data
 * for them are not available or simplified models are required.
 * 
 * 
 * Reference: IEEE Standard 421.5-2005 Section 6.5.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEAC5A extends ExcitationSystemDynamics {

	/**
	 * Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>).
	 * Typical Value = 5.6.
	 */
	public PU efd1;
	/**
	 * Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>).
	 * Typical Value = 4.2.
	 */
	public PU efd2;
	/**
	 * Voltage regulator gain (K<sub>A</sub>).  Typical Value = 400.
	 */
	public PU ka;
	/**
	 * Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
	 * = 1.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gains (K<sub>F</sub>).  Typical Value = 0.
	 * 03.
	 */
	public PU kf;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]).  Typical Value = 0.86.
	 */
	public Float seefd1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]).  Typical Value = 0.5.
	 */
	public Float seefd2;
	/**
	 * Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.02.
	 */
	public Seconds ta;
	/**
	 * Exciter time constant, integration rate associated with exciter control
	 * (T<sub>E</sub>).  Typical Value = 0.8.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (T<sub>F1</sub>).  Typical
	 * Value = 1.
	 */
	public Seconds tf1;
	/**
	 * Excitation control system stabilizer time constant (T<sub>F2</sub>).  Typical
	 * Value = 1.
	 */
	public Seconds tf2;
	/**
	 * Excitation control system stabilizer time constant (T<sub>F3</sub>).  Typical
	 * Value = 1.
	 */
	public Seconds tf3;
	/**
	 * Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 7.3.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -7.3.
	 */
	public PU vrmin;

	public ExcIEEEAC5A(){

	}
}//end ExcIEEEAC5A