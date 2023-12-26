package IEC61970.Dynamics.StandardModels.OverexcitationLimiterDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;

/**
 * The over excitation limiter model is intended to represent the significant
 * features of OELs necessary for some large-scale system studies. It is the
 * result of a pragmatic approach to obtain a model that can be widely applied
 * with attainable data from generator owners. An attempt to include all
 * variations in the functionality of OELs and duplicate how they interact with
 * the rest of the excitation systems would likely result in a level of
 * application insufficient for the studies for which they are intended.
 * 
 * Reference: IEEE OEL 421.5-2005 Section 9.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class OverexcLimIEEE extends OverexcitationLimiterDynamics {

	/**
	 * OEL pickup/drop-out hysteresis (HYST).  Typical Value = 0.03.
	 */
	public PU hyst;
	/**
	 * OEL timed field current limit (I<sub>FDLIM</sub>).  Typical Value = 1.05.
	 */
	public PU ifdlim;
	/**
	 * OEL instantaneous field current limit (I<sub>FDMAX</sub>).  Typical Value = 1.5.
	 */
	public PU ifdmax;
	/**
	 * OEL timed field current limiter pickup level (I<sub>TFPU</sub>).  Typical Value
	 * = 1.05.
	 */
	public PU itfpu;
	/**
	 * OEL cooldown gain (K<sub>CD</sub>).  Typical Value = 1.
	 */
	public PU kcd;
	/**
	 * OEL ramped limit rate (K<sub>RAMP</sub>).  Unit = PU/sec.  Typical Value = 10.
	 */
	public Float kramp;

	public OverexcLimIEEE(){

	}
}//end OverexcLimIEEE