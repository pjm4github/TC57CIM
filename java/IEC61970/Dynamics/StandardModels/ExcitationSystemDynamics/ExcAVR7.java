package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * IVO excitation system.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcAVR7 extends ExcitationSystemDynamics {

	/**
	 * Lead coefficient (A1).  Typical Value = 0.5.
	 */
	public PU a1;
	/**
	 * Lag coefficient (A2).  Typical Value = 0.5.
	 */
	public PU a2;
	/**
	 * Lead coefficient (A3).  Typical Value = 0.5.
	 */
	public PU a3;
	/**
	 * Lag coefficient (A4).  Typical Value = 0.5.
	 */
	public PU a4;
	/**
	 * Lead coefficient (A5).  Typical Value = 0.5.
	 */
	public PU a5;
	/**
	 * Lag coefficient (A6).  Typical Value = 0.5.
	 */
	public PU a6;
	/**
	 * Gain (K1).  Typical Value = 1.
	 */
	public PU k1;
	/**
	 * Gain (K3).  Typical Value = 3.
	 */
	public PU k3;
	/**
	 * Gain (K5).  Typical Value = 1.
	 */
	public PU k5;
	/**
	 * Lead time constant (T1).  Typical Value = 0.05.
	 */
	public Seconds t1;
	/**
	 * Lag time constant (T2).  Typical Value = 0.1.
	 */
	public Seconds t2;
	/**
	 * Lead time constant (T3).  Typical Value = 0.1.
	 */
	public Seconds t3;
	/**
	 * Lag time constant (T4).  Typical Value = 0.1.
	 */
	public Seconds t4;
	/**
	 * Lead time constant (T5).  Typical Value = 0.1.
	 */
	public Seconds t5;
	/**
	 * Lag time constant (T6).  Typical Value = 0.1.
	 */
	public Seconds t6;
	/**
	 * Lead-lag max. limit (Vmax1).  Typical Value = 5.
	 */
	public PU vmax1;
	/**
	 * Lead-lag max. limit (Vmax3).  Typical Value = 5.
	 */
	public PU vmax3;
	/**
	 * Lead-lag max. limit (Vmax5).  Typical Value = 5.
	 */
	public PU vmax5;
	/**
	 * Lead-lag min. limit (Vmin1).  Typical Value = -5.
	 */
	public PU vmin1;
	/**
	 * Lead-lag min. limit (Vmin3).  Typical Value = -5.
	 */
	public PU vmin3;
	/**
	 * Lead-lag min. limit (Vmin5).  Typical Value = -2.
	 */
	public PU vmin5;

	public ExcAVR7(){

	}
}//end ExcAVR7