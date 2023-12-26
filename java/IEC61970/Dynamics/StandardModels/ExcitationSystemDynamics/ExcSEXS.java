package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Simplified Excitation System Model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcSEXS extends ExcitationSystemDynamics {

	/**
	 * Field voltage clipping maximum limit (Efdmax).  Typical Value = 5.
	 */
	public PU efdmax;
	/**
	 * Field voltage clipping minimum limit (Efdmin).  Typical Value = -5.
	 */
	public PU efdmin;
	/**
	 * Maximum field voltage output (Emax).  Typical Value = 5.
	 */
	public PU emax;
	/**
	 * Minimum field voltage output (Emin).  Typical Value = -5.
	 */
	public PU emin;
	/**
	 * Gain (K) (>0).  Typical Value = 100.
	 */
	public PU k;
	/**
	 * PI controller gain (Kc).  Typical Value = 0.08.
	 */
	public PU kc;
	/**
	 * Ta/Tb - gain reduction ratio of lag-lead element (TaTb).  Typical Value = 0.1.
	 */
	public Float tatb;
	/**
	 * Denominator time constant of lag-lead block (Tb).  Typical Value = 10.
	 */
	public Seconds tb;
	/**
	 * PI controller phase lead time constant (Tc).  Typical Value = 0.
	 */
	public Seconds tc;
	/**
	 * Time constant of gain block (Te).  Typical Value = 0.05.
	 */
	public Seconds te;

	public ExcSEXS(){

	}
}//end ExcSEXS