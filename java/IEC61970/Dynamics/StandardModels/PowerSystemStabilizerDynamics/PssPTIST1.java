package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PU;

/**
 * PTI Microprocessor-Based Stabilizer type 1.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PssPTIST1 extends PowerSystemStabilizerDynamics {

	/**
	 * Time step related to activation of controls (Dtc).  Typical Value = 0.025.
	 */
	public Seconds dtc;
	/**
	 * Time step frequency calculation (Dtf).  Typical Value = 0.025.
	 */
	public Seconds dtf;
	/**
	 * Time step active power calculation (Dtp).  Typical Value = 0.0125.
	 */
	public Seconds dtp;
	/**
	 * Gain (K).  Typical Value = 9.
	 */
	public PU k;
	/**
	 * (M).  M=2*H.  Typical Value = 5.
	 */
	public PU m;
	/**
	 * Time constant (T1).  Typical Value = 0.3.
	 */
	public Seconds t1;
	/**
	 * Time constant (T2).  Typical Value = 1.
	 */
	public Seconds t2;
	/**
	 * Time constant (T3).  Typical Value = 0.2.
	 */
	public Seconds t3;
	/**
	 * Time constant (T4).  Typical Value = 0.05.
	 */
	public Seconds t4;
	/**
	 * Time constant (Tf).  Typical Value = 0.2.
	 */
	public Seconds tf;
	/**
	 * Time constant (Tp).  Typical Value = 0.2.
	 */
	public Seconds tp;

	public PssPTIST1(){

	}
}//end PssPTIST1