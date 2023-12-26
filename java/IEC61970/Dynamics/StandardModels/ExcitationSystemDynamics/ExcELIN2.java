package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Detailed Excitation System Model - ELIN (VATECH).  This model represents an all-
 * static excitation system. A PI voltage controller establishes a desired field
 * current set point for a proportional current controller. The integrator of the
 * PI controller has a follow-up input to match its signal to the present field
 * current.  Power system stabilizer models used in conjunction with this
 * excitation system model: PssELIN2, PssIEEE2B, Pss2B.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcELIN2 extends ExcitationSystemDynamics {

	/**
	 * Gain (Efdbas).  Typical Value = 0.1.
	 */
	public PU efdbas;
	/**
	 * Limiter (Iefmax).  Typical Value = 1.
	 */
	public PU iefmax;
	/**
	 * Minimum open circuit excitation voltage (Iefmax2).  Typical Value = -5.
	 */
	public PU iefmax2;
	/**
	 * Limiter (Iefmin).  Typical Value = 1.
	 */
	public PU iefmin;
	/**
	 * Voltage regulator input gain (K1).  Typical Value = 0.
	 */
	public PU k1;
	/**
	 * Voltage regulator input limit (K1ec).  Typical Value = 2.
	 */
	public PU k1ec;
	/**
	 * Gain (K2).  Typical Value = 5.
	 */
	public PU k2;
	/**
	 * Gain (K3).  Typical Value = 0.1.
	 */
	public PU k3;
	/**
	 * Gain (K4).  Typical Value = 0.
	 */
	public PU k4;
	/**
	 * Voltage controller derivative gain (Kd1).  Typical Value = 34.5.
	 */
	public PU kd1;
	/**
	 * Gain (Ke2).  Typical Value = 0.1.
	 */
	public PU ke2;
	/**
	 * Gain (Ketb).  Typical Value = 0.06.
	 */
	public PU ketb;
	/**
	 * Controller follow up gain (PID1max).  Typical Value = 2.
	 */
	public PU pid1max;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Ve1,
	 * back of commutating reactance (Se[Ve1]).  Typical Value = 0.
	 */
	public PU seve1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Ve2,
	 * back of commutating reactance (Se[Ve2]).  Typical Value = 1.
	 */
	public PU seve2;
	/**
	 * Voltage controller derivative washout time constant (Tb1).  Typical Value = 12.
	 * 45.
	 */
	public Seconds tb1;
	/**
	 * Time constant (Te).  Typical Value = 0.
	 */
	public Seconds te;
	/**
	 * Time Constant (Te2).  Typical Value = 1.
	 */
	public Seconds te2;
	/**
	 * Controller follow up dead band (Ti1).  Typical Value = 0.
	 */
	public PU ti1;
	/**
	 * Time constant (Ti3).  Typical Value = 3.
	 */
	public Seconds ti3;
	/**
	 * Time constant (Ti4).  Typical Value = 0.
	 */
	public Seconds ti4;
	/**
	 * Time constant (Tr4).  Typical Value = 1.
	 */
	public Seconds tr4;
	/**
	 * Limiter (Upmax).  Typical Value = 3.
	 */
	public PU upmax;
	/**
	 * Limiter (Upmin).  Typical Value = 0.
	 */
	public PU upmin;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (Ve1).  Typical Value = 3.
	 */
	public PU ve1;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (Ve2).  Typical Value = 0.
	 */
	public PU ve2;
	/**
	 * Excitation transformer effective reactance (Xp).  Typical Value = 1.
	 */
	public PU xp;

	public ExcELIN2(){

	}
}//end ExcELIN2