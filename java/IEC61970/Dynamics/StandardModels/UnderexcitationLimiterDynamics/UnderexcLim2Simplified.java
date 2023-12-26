package IEC61970.Dynamics.StandardModels.UnderexcitationLimiterDynamics;

import IEC61970.Base.Domain.PU;

/**
 * This model can be derived from UnderexcLimIEEE2.
 * The limit characteristic (look -up table) is a single straight-line, the same
 * as UnderexcLimIEEE2 (see Figure 10.4 (p 32), IEEE 421.5-2005 Section 10.2).
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class UnderexcLim2Simplified extends UnderexcitationLimiterDynamics {

	/**
	 * Gain Under excitation limiter (Kui).  Typical Value = 0.1.
	 */
	public PU kui;
	/**
	 * Segment P initial point (P0).  Typical Value = 0.
	 */
	public PU p0;
	/**
	 * Segment P end point (P1).  Typical Value = 1.
	 */
	public PU p1;
	/**
	 * Segment Q initial point (Q0).  Typical Value = -0.31.
	 */
	public PU q0;
	/**
	 * Segment Q end point (Q1).  Typical Value = -0.1.
	 */
	public PU q1;
	/**
	 * Maximum error signal (V<sub>UImax</sub>).  Typical Value = 1.
	 */
	public PU vuimax;
	/**
	 * Minimum error signal (V<sub>UImin</sub>).  Typical Value = 0.
	 */
	public PU vuimin;

	public UnderexcLim2Simplified(){

	}
}//end UnderexcLim2Simplified