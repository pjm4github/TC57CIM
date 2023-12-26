package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;

/**
 * Woodward PID Hydro Governor.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovHydroWPID extends TurbineGovernorDynamics {

	/**
	 * Turbine damping factor (D).  Unit = delta P / delta speed.
	 */
	public PU d;
	/**
	 * Gate opening Limit Maximum (Gatmax).
	 */
	public PU gatmax;
	/**
	 * Gate opening Limit Minimum (Gatmin).
	 */
	public PU gatmin;
	/**
	 * Gate position 1 (Gv1).
	 */
	public PU gv1;
	/**
	 * Gate position 2 (Gv2). 
	 */
	public PU gv2;
	/**
	 * Gate position 3 (Gv3).
	 */
	public PU gv3;
	/**
	 * Derivative gain (Kd).  Typical Value = 1.11.
	 */
	public PU kd;
	/**
	 * Reset gain (Ki).  Typical Value = 0.36.
	 */
	public PU ki;
	/**
	 * Proportional gain (Kp).  Typical Value = 0.1.
	 */
	public PU kp;
	/**
	 * Base for power values  (MWbase) (>0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Output at Gv1 PU of MWbase (Pgv1).
	 */
	public PU pgv1;
	/**
	 * Output at Gv2 PU of MWbase (Pgv2).
	 */
	public PU pgv2;
	/**
	 * Output at Gv3 PU of MWbase (Pgv3). 
	 */
	public PU pgv3;
	/**
	 * Maximum Power Output (Pmax).
	 */
	public PU pmax;
	/**
	 * Minimum Power Output (Pmin).
	 */
	public PU pmin;
	/**
	 * Permanent drop (Reg).
	 */
	public PU reg;
	/**
	 * Controller time constant (Ta) (>0).  Typical Value = 0.
	 */
	public Seconds ta;
	/**
	 * Gate servo time constant (Tb) (>0).  Typical Value = 0.
	 */
	public Seconds tb;
	/**
	 * Speed detector time constant (Treg).
	 */
	public Seconds treg;
	/**
	 * Water inertia time constant (Tw) (>0).  Typical Value = 0.
	 */
	public Seconds tw;
	/**
	 * Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0.
	 */
	public PU velmax;
	/**
	 * Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0.
	 */
	public PU velmin;

	public GovHydroWPID(){

	}
}//end GovHydroWPID