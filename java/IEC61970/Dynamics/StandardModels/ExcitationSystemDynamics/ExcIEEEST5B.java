package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type ST5B model. The Type ST5B
 * excitation system is a variation of the Type ST1A model, with alternative
 * overexcitation and underexcitation inputs and additional limits.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 7.5.
 * 
 * Note: the block diagram in the IEEE 421.5 standard has input signal Vc and does
 * not indicate the summation point with Vref. The implementation of the
 * ExcIEEEST5B shall consider summation point with Vref.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEST5B extends ExcitationSystemDynamics {

	/**
	 * Rectifier regulation factor (K<sub>C</sub>).  Typical Value = 0.004.
	 */
	public PU kc;
	/**
	 * Regulator gain (K<sub>R</sub>).  Typical Value = 200.
	 */
	public PU kr;
	/**
	 * Firing circuit time constant (T1).  Typical Value = 0.004.
	 */
	public Seconds t1;
	/**
	 * Regulator lag time constant (T<sub>B1</sub>).  Typical Value = 6.
	 */
	public Seconds tb1;
	/**
	 * Regulator lag time constant (T<sub>B2</sub>).  Typical Value = 0.01.
	 */
	public Seconds tb2;
	/**
	 * Regulator lead time constant (T<sub>C1</sub>).  Typical Value = 0.8.
	 */
	public Seconds tc1;
	/**
	 * Regulator lead time constant (T<sub>C2</sub>).  Typical Value = 0.08.
	 */
	public Seconds tc2;
	/**
	 * OEL lag time constant (T<sub>OB1</sub>).  Typical Value = 2.
	 */
	public Seconds tob1;
	/**
	 * OEL lag time constant (T<sub>OB2</sub>).  Typical Value = 0.08.
	 */
	public Seconds tob2;
	/**
	 * OEL lead time constant (T<sub>OC1</sub>).  Typical Value = 0.1.
	 */
	public Seconds toc1;
	/**
	 * OEL lead time constant (T<sub>OC2</sub>).  Typical Value = 0.08.
	 */
	public Seconds toc2;
	/**
	 * UEL lag time constant (T<sub>UB1</sub>).  Typical Value = 10.
	 */
	public Seconds tub1;
	/**
	 * UEL lag time constant (T<sub>UB2</sub>).  Typical Value = 0.05.
	 */
	public Seconds tub2;
	/**
	 * UEL lead time constant (T<sub>UC1</sub>).  Typical Value = 2.
	 */
	public Seconds tuc1;
	/**
	 * UEL lead time constant (T<sub>UC2</sub>).  Typical Value = 0.1.
	 */
	public Seconds tuc2;
	/**
	 * Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 5.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -4.
	 */
	public PU vrmin;

	public ExcIEEEST5B(){

	}
}//end ExcIEEEST5B