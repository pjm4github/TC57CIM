package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified IEEE AC4A alternator-supplied rectifier excitation system with
 * different minimum controller output.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcAC4A extends ExcitationSystemDynamics {

	/**
	 * Voltage regulator gain (Ka).  Typical Value = 200.
	 */
	public PU ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (Kc).  Typical
	 * Value = 0.
	 */
	public PU kc;
	/**
	 * Voltage regulator time constant (Ta).  Typical Value = 0.015.
	 */
	public Seconds ta;
	/**
	 * Voltage regulator time constant (Tb).  Typical Value = 10.
	 */
	public Seconds tb;
	/**
	 * Voltage regulator time constant (Tc).  Typical Value = 1.
	 */
	public Seconds tc;
	/**
	 * Maximum voltage regulator input limit (Vimax).  Typical Value = 10.
	 */
	public PU vimax;
	/**
	 * Minimum voltage regulator input limit (Vimin).  Typical Value = -10.
	 */
	public PU vimin;
	/**
	 * Maximum voltage regulator output (Vrmax).  Typical Value = 5.64.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (Vrmin).  Typical Value = -4.53.
	 */
	public PU vrmin;

	public ExcAC4A(){

	}
}//end ExcAC4A