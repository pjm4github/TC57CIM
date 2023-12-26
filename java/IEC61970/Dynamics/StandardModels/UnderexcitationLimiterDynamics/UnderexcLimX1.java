package IEC61970.Dynamics.StandardModels.UnderexcitationLimiterDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * <font color="#0f0f0f">Allis-Chalmers minimum excitation limiter.</font>
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class UnderexcLimX1 extends UnderexcitationLimiterDynamics {

	/**
	 * Minimum excitation limit slope (K) (>0).
	 */
	public PU k;
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
	 * Differential time constant (Tf2) (>0).
	 */
	public Seconds tf2;
	/**
	 * Minimum excitation limit time constant (Tm).
	 */
	public Seconds tm;

	public UnderexcLimX1(){

	}
}//end UnderexcLimX1