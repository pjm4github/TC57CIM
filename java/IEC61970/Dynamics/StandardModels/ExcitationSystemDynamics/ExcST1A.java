package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Modification of an old IEEE ST1A static excitation system without
 * overexcitation limiter (OEL) and underexcitation limiter (UEL).
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcST1A extends ExcitationSystemDynamics {

	/**
	 * Exciter output current limit reference (Ilr).  Typical Value = 0.
	 */
	public PU ilr;
	/**
	 * Voltage regulator gain (Ka).  Typical Value = 190.
	 */
	public PU ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (Kc). Typical
	 * Value = 0.05.
	 */
	public PU kc;
	/**
	 * Excitation control system stabilizer gains (Kf).  Typical Value = 0.
	 */
	public PU kf;
	/**
	 * Exciter output current limiter gain (Klr).  Typical Value = 0.
	 */
	public PU klr;
	/**
	 * Voltage regulator time constant (Ta).  Typical Value = 0.02.
	 */
	public Seconds ta;
	/**
	 * Voltage regulator time constant (Tb).  Typical Value = 10.
	 */
	public Seconds tb;
	/**
	 * Voltage regulator time constant (Tb<sub>1</sub>).  Typical Value = 0.
	 */
	public Seconds tb1;
	/**
	 * Voltage regulator time constant (Tc).  Typical Value = 1.
	 */
	public Seconds tc;
	/**
	 * Voltage regulator time constant (Tc<sub>1</sub>).  Typical Value = 0.
	 */
	public Seconds tc1;
	/**
	 * Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
	 */
	public Seconds tf;
	/**
	 * Maximum voltage regulator output (Vamax).  Typical Value = 999.
	 */
	public PU vamax;
	/**
	 * Minimum voltage regulator output (Vamin).  Typical Value = -999.
	 */
	public PU vamin;
	/**
	 * Maximum voltage regulator input limit (Vimax).  Typical Value = 999.
	 */
	public PU vimax;
	/**
	 * Minimum voltage regulator input limit (Vimin).  Typical Value = -999.
	 */
	public PU vimin;
	/**
	 * Maximum voltage regulator outputs (Vrmax).  Typical Value = 7.8.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator outputs (Vrmin).  Typical Value = -6.7.
	 */
	public PU vrmin;
	/**
	 * Excitation xfmr effective reactance (Xe).  Typical Value = 0.04.
	 */
	public PU xe;

	public ExcST1A(){

	}
}//end ExcST1A