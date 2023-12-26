package IEC61970.Dynamics.StandardModels.UnderexcitationLimiterDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * <font color="#0f0f0f">Westinghouse minimum excitation limiter.</font>
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class UnderexcLimX2 extends UnderexcitationLimiterDynamics {

	/**
	 * Differential gain (Kf2).
	 */
	public PU kf2;
	/**
	 * Minimum excitation limit gain (Km).
	 */
	public PU km;
	/**
	 * Minimum excitation limit value (MELMAX).
	 */
	public PU melmax;
	/**
	 * Excitation center setting (Qo).
	 */
	public PU qo;
	/**
	 * Excitation radius (R).
	 */
	public PU r;
	/**
	 * Differential time constant (Tf2) (>0).
	 */
	public Seconds tf2;
	/**
	 * Minimum excitation limit time constant (Tm).
	 */
	public Seconds tm;

	public UnderexcLimX2(){

	}
}//end UnderexcLimX2