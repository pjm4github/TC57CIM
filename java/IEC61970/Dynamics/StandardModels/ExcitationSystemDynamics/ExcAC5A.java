package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified IEEE AC5A alternator-supplied rectifier excitation system with
 * different minimum controller output.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcAC5A extends ExcitationSystemDynamics {

	/**
	 * Coefficient to allow different usage of the model (a).  Typical Value = 1.
	 */
	public Float a;
	/**
	 * Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value =
	 * 5.6.
	 */
	public PU efd1;
	/**
	 * Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value =
	 * 4.2.
	 */
	public PU efd2;
	/**
	 * Voltage regulator gain (Ka).  Typical Value = 400.
	 */
	public PU ka;
	/**
	 * Exciter constant related to self-excited field (Ke).  Typical Value = 1.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gains (Kf).  Typical Value = 0.03.
	 */
	public PU kf;
	/**
	 * Coefficient to allow different usage of the model-speed coefficient (Ks).
	 * Typical Value = 0.
	 */
	public PU ks;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Efd1
	 * (S<sub>E</sub>[Efd1]).  Typical Value = 0.86.
	 */
	public Float seefd1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Efd2
	 * (S<sub>E</sub>[Efd2]).  Typical Value = 0.5.
	 */
	public Float seefd2;
	/**
	 * Voltage regulator time constant (Ta).  Typical Value = 0.02.
	 */
	public Seconds ta;
	/**
	 * Voltage regulator time constant (Tb).  Typical Value = 0.
	 */
	public Seconds tb;
	/**
	 * Voltage regulator time constant (Tc).  Typical Value = 0.
	 */
	public Seconds tc;
	/**
	 * Exciter time constant, integration rate associated with exciter control (Te).
	 * Typical Value = 0.8.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (Tf1).  Typical Value  = 1.
	 */
	public Seconds tf1;
	/**
	 * Excitation control system stabilizer time constant (Tf2).  Typical Value = 0.8.
	 */
	public Seconds tf2;
	/**
	 * Excitation control system stabilizer time constant (Tf3).  Typical Value = 0.
	 */
	public Seconds tf3;
	/**
	 * Maximum voltage regulator output (Vrmax).  Typical Value = 7.3.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (Vrmin).  Typical Value =-7.3.
	 */
	public PU vrmin;

	public ExcAC5A(){

	}
}//end ExcAC5A