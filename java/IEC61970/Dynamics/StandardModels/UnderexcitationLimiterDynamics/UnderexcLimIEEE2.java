package IEC61970.Dynamics.StandardModels.UnderexcitationLimiterDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents the Type UEL2 which has either a straight-line or multi-
 * segment characteristic when plotted in terms of machine reactive power output
 * vs. real power output.
 * 
 * Reference: IEEE UEL2 421.5-2005 Section 10.2.  (Limit characteristic lookup
 * table shown in Figure 10.4 (p 32) of the standard).
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class UnderexcLimIEEE2 extends UnderexcitationLimiterDynamics {

	/**
	 * UEL terminal voltage exponent applied to real power input to UEL limit look-up
	 * table (k1).  Typical Value = 2.
	 */
	public Float k1;
	/**
	 * UEL terminal voltage exponent applied to reactive power output from UEL limit
	 * look-up table (k2).  Typical Value = 2.
	 */
	public Float k2;
	/**
	 * Gain associated with optional integrator feedback input signal to UEL
	 * (K<sub>FB</sub>).  Typical Value = 0.
	 */
	public PU kfb;
	/**
	 * UEL excitation system stabilizer gain (K<sub>UF</sub>).  Typical Value = 0.
	 */
	public PU kuf;
	/**
	 * UEL integral gain (K<sub>UI</sub>).  Typical Value = 0.5.
	 */
	public PU kui;
	/**
	 * UEL proportional gain (K<sub>UL</sub>).  Typical Value = 0.8.
	 */
	public PU kul;
	/**
	 * Real power values for endpoints (P<sub>0</sub>).  Typical Value = 0.
	 */
	public PU p0;
	/**
	 * Real power values for endpoints (P<sub>1</sub>).  Typical Value = 0.3.
	 */
	public PU p1;
	/**
	 * Real power values for endpoints (P<sub>10</sub>). 
	 */
	public PU p10;
	/**
	 * Real power values for endpoints (P<sub>2</sub>).  Typical Value = 0.6.
	 */
	public PU p2;
	/**
	 * Real power values for endpoints (P<sub>3</sub>).  Typical Value = 0.9.
	 */
	public PU p3;
	/**
	 * Real power values for endpoints (P<sub>4</sub>).  Typical Value = 1.02.
	 */
	public PU p4;
	/**
	 * Real power values for endpoints (P<sub>5</sub>). 
	 */
	public PU p5;
	/**
	 * Real power values for endpoints (P<sub>6</sub>).
	 */
	public PU p6;
	/**
	 * Real power values for endpoints (P<sub>7</sub>). 
	 */
	public PU p7;
	/**
	 * Real power values for endpoints (P<sub>8</sub>). 
	 */
	public PU p8;
	/**
	 * Real power values for endpoints (P<sub>9</sub>). 
	 */
	public PU p9;
	/**
	 * Reactive power values for endpoints (Q<sub>0</sub>).  Typical Value = -0.31.
	 */
	public PU q0;
	/**
	 * Reactive power values for endpoints (Q<sub>1</sub>).  Typical Value = -0.31.
	 */
	public PU q1;
	/**
	 * Reactive power values for endpoints (Q<sub>10</sub>). 
	 */
	public PU q10;
	/**
	 * Reactive power values for endpoints (Q<sub>2</sub>).  Typical Value = -0.28.
	 */
	public PU q2;
	/**
	 * Reactive power values for endpoints (Q<sub>3</sub>).  Typical Value = -0.21.
	 */
	public PU q3;
	/**
	 * Reactive power values for endpoints (Q<sub>4</sub>).  Typical Value = 0.
	 */
	public PU q4;
	/**
	 * Reactive power values for endpoints (Q<sub>5</sub>). 
	 */
	public PU q5;
	/**
	 * Reactive power values for endpoints (Q<sub>6</sub>). 
	 */
	public PU q6;
	/**
	 * Reactive power values for endpoints (Q<sub>7</sub>). 
	 */
	public PU q7;
	/**
	 * Reactive power values for endpoints (Q<sub>8</sub>). 
	 */
	public PU q8;
	/**
	 * Reactive power values for endpoints (Q<sub>9</sub>). 
	 */
	public PU q9;
	/**
	 * UEL lead time constant (T<sub>U1</sub>).  Typical Value = 0.
	 */
	public Seconds tu1;
	/**
	 * UEL lag time constant (T<sub>U2</sub>).  Typical Value = 0.
	 */
	public Seconds tu2;
	/**
	 * UEL lead time constant (T<sub>U3</sub>).  Typical Value = 0.
	 */
	public Seconds tu3;
	/**
	 * UEL lag time constant (T<sub>U4</sub>).  Typical Value = 0.
	 */
	public Seconds tu4;
	/**
	 * Time constant associated with optional integrator feedback input signal to UEL
	 * (T<sub>UL</sub>).  Typical Value = 0.
	 */
	public Seconds tul;
	/**
	 * Real power filter time constant (T<sub>UP</sub>).  Typical Value = 5.
	 */
	public Seconds tup;
	/**
	 * Reactive power filter time constant (T<sub>UQ</sub>).  Typical Value = 0.
	 */
	public Seconds tuq;
	/**
	 * Voltage filter time constant (T<sub>UV</sub>).  Typical Value = 5.
	 */
	public Seconds tuv;
	/**
	 * UEL integrator output maximum limit (V<sub>UIMAX</sub>).  Typical Value = 0.25.
	 */
	public PU vuimax;
	/**
	 * UEL integrator output minimum limit (V<sub>UIMIN</sub>).  Typical Value = 0.
	 */
	public PU vuimin;
	/**
	 * UEL output maximum limit (V<sub>ULMAX</sub>).  Typical Value = 0.25.
	 */
	public PU vulmax;
	/**
	 * UEL output minimum limit (V<sub>ULMIN</sub>).  Typical Value = 0.
	 */
	public PU vulmin;

	public UnderexcLimIEEE2(){

	}
}//end UnderexcLimIEEE2