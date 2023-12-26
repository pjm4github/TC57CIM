package IEC61970.Dynamics.StandardModels.OverexcitationLimiterDynamics;

import IEC61970.Base.Domain.PU;

/**
 * Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the
 * excitation set-point by mean of non-windup integral regulator.
 * Irated is the rated machine excitation current (calculated from nameplate
 * conditions: V<sub>nom</sub>, P<sub>nom</sub>, CosPhi<sub>nom</sub>).
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class OverexcLim2 extends OverexcitationLimiterDynamics {

	/**
	 * Limit value of rated field current (I<sub>FDLIM</sub>).  Typical Value = 1.05.
	 */
	public PU ifdlim;
	/**
	 * Gain Over excitation limiter (K<sub>OI</sub>).  Typical Value = 0.1.
	 */
	public PU koi;
	/**
	 * Maximum error signal (V<sub>OIMAX</sub>).  Typical Value = 0.
	 */
	public PU voimax;
	/**
	 * Minimum error signal (V<sub>OIMIN</sub>).  Typical Value = -9999.
	 */
	public PU voimin;

	public OverexcLim2(){

	}
}//end OverexcLim2