package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;

/**
 * Hydro turbine and governor. Represents plants with straight forward penstock
 * configurations and "three term" electro-hydraulic governors (i.e. Woodard
 * electronic).
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovHydroPID2 extends TurbineGovernorDynamics {

	/**
	 * Factor multiplying Tw (Atw).  Typical Value = 0.
	 */
	public PU atw;
	/**
	 * Turbine damping factor (D).  Unit = delta P / delta speed.  Typical Value = 0.
	 */
	public PU d;
	/**
	 * Feedback signal type flag (Flag).
	 * true = use gate position feedback signal
	 * false = use Pe.
	 */
	public Boolean feedbackSignal;
	/**
	 * Gate opening at speed no load (G0).  Typical Value = 0.
	 */
	public PU g0;
	/**
	 * Intermediate gate opening (G1).  Typical Value = 0.
	 */
	public PU g1;
	/**
	 * Intermediate gate opening (G2).  Typical Value = 0.
	 */
	public PU g2;
	/**
	 * Maximum gate opening (Gmax).  Typical Value = 0.
	 */
	public PU gmax;
	/**
	 * Minimum gate opening (Gmin).  Typical Value = 0.
	 */
	public PU gmin;
	/**
	 * Derivative gain (Kd).  Typical Value = 0.
	 */
	public PU kd;
	/**
	 * Reset gain (Ki).  Unit = PU/ sec.  Typical Value = 0.
	 */
	public Float ki;
	/**
	 * Proportional gain (Kp).  Typical Value = 0.
	 */
	public PU kp;
	/**
	 * Base for power values (MWbase) (>0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Power at gate opening G1 (P1).  Typical Value = 0.
	 */
	public PU p1;
	/**
	 * Power at gate opening G2 (P2).  Typical Value = 0.
	 */
	public PU p2;
	/**
	 * Power at full opened gate (P3).  Typical Value = 0.
	 */
	public PU p3;
	/**
	 * Permanent drop (Rperm).  Typical Value = 0.
	 */
	public PU rperm;
	/**
	 * Controller time constant (Ta) (>0).  Typical Value = 0.
	 */
	public Seconds ta;
	/**
	 * Gate servo time constant (Tb) (>0).  Typical Value = 0.
	 */
	public Seconds tb;
	/**
	 * Speed detector time constant (Treg).  Typical Value = 0.
	 */
	public Seconds treg;
	/**
	 * Water inertia time constant (Tw) (>0).  Typical Value = 0.
	 */
	public Seconds tw;
	/**
	 * Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0.
	 */
	public Float velmax;
	/**
	 * Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0.
	 */
	public Float velmin;

	public GovHydroPID2(){

	}
}//end GovHydroPID2