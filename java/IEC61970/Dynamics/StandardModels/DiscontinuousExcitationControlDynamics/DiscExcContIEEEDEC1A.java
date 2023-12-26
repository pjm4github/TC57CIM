package IEC61970.Dynamics.StandardModels.DiscontinuousExcitationControlDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Type DEC1A discontinuous excitation control model
 * that boosts generator excitation to a level higher than that demanded by the
 * voltage regulator and stabilizer immediately following a system fault.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 12.2.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class DiscExcContIEEEDEC1A extends DiscontinuousExcitationControlDynamics {

	/**
	 * Speed change reference (<i>E</i><i><sub>SC</sub></i>).  Typical Value = 0.0015.
	 */
	public PU esc;
	/**
	 * Discontinuous controller gain (<i>K</i><i><sub>AN</sub></i>).  Typical Value =
	 * 400.
	 */
	public PU kan;
	/**
	 * Terminal voltage limiter gain (<i>K</i><i><sub>ETL</sub></i>).  Typical Value =
	 * 47.
	 */
	public PU ketl;
	/**
	 * Discontinuous controller time constant (<i>T</i><i><sub>AN</sub></i>).  Typical
	 * Value = 0.08.
	 */
	public Seconds tan;
	/**
	 * Time constant (<i>T</i><i><sub>D</sub></i>).  Typical Value = 0.03.
	 */
	public Seconds td;
	/**
	 * Time constant (<i>T</i><i><sub>L</sub></i><sub>1</sub>).  Typical Value = 0.025.
	 */
	public Seconds tl1;
	/**
	 * Time constant (<i>T</i><i><sub>L</sub></i><sub>2</sub>).  Typical Value = 1.25.
	 */
	public Seconds tl2;
	/**
	 * DEC washout time constant (<i>T</i><i><sub>W</sub></i><sub>5</sub>).  Typical
	 * Value = 5.
	 */
	public Seconds tw5;
	/**
	 * Regulator voltage reference (<i>V</i><i><sub>AL</sub></i>).  Typical Value = 5.
	 * 5.
	 */
	public PU val;
	/**
	 * Limiter for Van (<i>V</i><i><sub>ANMAX</sub></i>).
	 */
	public PU vanmax;
	/**
	 * Limiter (<i>V</i><i><sub>OMAX</sub></i>).  Typical Value = 0.3.
	 */
	public PU vomax;
	/**
	 * Limiter (<i>V</i><i><sub>OMIN</sub></i>).  Typical Value = 0.1.
	 */
	public PU vomin;
	/**
	 * Limiter (<i>V</i><i><sub>SMAX</sub></i>).  Typical Value = 0.2.
	 */
	public PU vsmax;
	/**
	 * Limiter (<i>V</i><i><sub>SMIN</sub></i>).  Typical Value = -0.066.
	 */
	public PU vsmin;
	/**
	 * Terminal voltage level reference (<i>V</i><i><sub>TC</sub></i>).  Typical Value
	 * = 0.95.
	 */
	public PU vtc;
	/**
	 * Voltage reference (<i>V</i><i><sub>TLMT</sub></i>).  Typical Value = 1.1.
	 */
	public PU vtlmt;
	/**
	 * Voltage limits (<i>V</i><i><sub>TM</sub></i>).  Typical Value = 1.13.
	 */
	public PU vtm;
	/**
	 * Voltage limits (<i>V</i><i><sub>TN</sub></i>).  Typical Value = 1.12.
	 */
	public PU vtn;

	public DiscExcContIEEEDEC1A(){

	}
}//end DiscExcContIEEEDEC1A