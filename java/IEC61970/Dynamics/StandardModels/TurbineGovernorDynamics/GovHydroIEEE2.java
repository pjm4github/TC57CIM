package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Float;

/**
 * IEEE hydro turbine governor model represents plants with straightforward
 * penstock configurations and hydraulic-dashpot governors.
 * 
 * Ref<font color="#0f0f0f">erence: IEEE Transactions on Power Apparatus and
 * Systems</font>
 * <font color="#0f0f0f">November/December 1973, Volume PAS-92, Number 6</font>
 * <font color="#0f0f0f"><i><u>Dynamic Models for Steam and Hydro Turbines in
 * Power System Studies</u></i>, Page 1904.</font>
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovHydroIEEE2 extends TurbineGovernorDynamics {

	/**
	 * Turbine numerator multiplier (Aturb).  Typical Value = -1.
	 */
	public PU aturb;
	/**
	 * Turbine denominator multiplier (Bturb).  Typical Value = 0.5.
	 */
	public PU bturb;
	/**
	 * Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0.
	 */
	public PU gv1;
	/**
	 * Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0.
	 */
	public PU gv2;
	/**
	 * Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0.
	 */
	public PU gv3;
	/**
	 * Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0.
	 */
	public PU gv4;
	/**
	 * Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0.
	 */
	public PU gv5;
	/**
	 * Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0.
	 */
	public PU gv6;
	/**
	 * Turbine gain (Kturb).  Typical Value = 1.
	 */
	public PU kturb;
	/**
	 * Base for power values (MWbase) (> 0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0.
	 */
	public PU pgv1;
	/**
	 * Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0.
	 */
	public PU pgv2;
	/**
	 * Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0.
	 */
	public PU pgv3;
	/**
	 * Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0.
	 */
	public PU pgv4;
	/**
	 * Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.
	 */
	public PU pgv5;
	/**
	 * Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0.
	 */
	public PU pgv6;
	/**
	 * Maximum gate opening (Pmax).  Typical Value = 1.
	 */
	public PU pmax;
	/**
	 * Minimum gate opening (Pmin).  Typical Value = 0.
	 */
	public PU pmin;
	/**
	 * Permanent droop (Rperm).  Typical Value = 0.05.
	 */
	public PU rperm;
	/**
	 * Temporary droop (Rtemp).  Typical Value = 0.5.
	 */
	public PU rtemp;
	/**
	 * Gate servo time constant (Tg).  Typical Value = 0.5.
	 */
	public Seconds tg;
	/**
	 * Pilot servo valve time constant (Tp).  Typical Value = 0.03.
	 */
	public Seconds tp;
	/**
	 * Dashpot time constant (Tr).  Typical Value = 12.
	 */
	public Seconds tr;
	/**
	 * Water inertia time constant (Tw).  Typical Value = 2.
	 */
	public Seconds tw;
	/**
	 * Maximum gate closing velocity (Uc) (<0).  Typical Value = -0.1.
	 */
	public Float uc;
	/**
	 * Maximum gate opening velocity (Uo). Unit = PU/sec.  Typical Value = 0.1.
	 */
	public Float uo;

	public GovHydroIEEE2(){

	}
}//end GovHydroIEEE2