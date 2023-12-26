package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Float;

/**
 * Modified IEEE Hydro Governor-Turbine Model.
 * 
 * This model differs from that defined in the IEEE modeling guideline paper in
 * that the limits on gate position and velocity do not permit "wind up" of the
 * upstream signals.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovHydro3 extends TurbineGovernorDynamics {

	/**
	 * Turbine gain (At).  Typical Value = 1.2.
	 */
	public PU at;
	/**
	 * Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency db1;
	/**
	 * Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
	 */
	public ActivePower db2;
	/**
	 * Turbine damping factor (Dturb).  Typical Value = 0.2.
	 */
	public PU dturb;
	/**
	 * Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency eps;
	/**
	 * Governor control flag (Cflag).
	 * true = PID control is active
	 * false = double derivative control is active.
	 * Typical Value = true.
	 */
	public Boolean governorControl;
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
	 * Turbine nominal head (H0).  Typical Value = 1.
	 */
	public PU h0;
	/**
	 * Derivative gain (K1).  Typical Value = 0.01.
	 */
	public PU k1;
	/**
	 * Double derivative gain, if Cflag = -1 (K2).  Typical Value = 2.5.
	 */
	public PU k2;
	/**
	 * Gate servo gain (Kg).  Typical Value = 2.
	 */
	public PU kg;
	/**
	 * Integral gain (Ki).  Typical Value = 0.5.
	 */
	public PU ki;
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
	 * Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1.
	 */
	public PU pmax;
	/**
	 * Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0.
	 */
	public PU pmin;
	/**
	 * No-load turbine flow at nominal head (Qnl).  Typical Value = 0.08.
	 */
	public PU qnl;
	/**
	 * Steady-state droop, PU, for electrical power feedback (Relec).  Typical Value =
	 * 0.05.
	 */
	public PU relec;
	/**
	 * Steady-state droop, PU, for governor output feedback (Rgate).  Typical Value =
	 * 0.
	 */
	public PU rgate;
	/**
	 * Input filter time constant (Td).  Typical Value = 0.05.
	 */
	public Seconds td;
	/**
	 * Washout time constant (Tf).  Typical Value = 0.1.
	 */
	public Seconds tf;
	/**
	 * Gate servo time constant (Tp).  Typical Value = 0.05.
	 */
	public Seconds tp;
	/**
	 * Power feedback time constant (Tt).  Typical Value = 0.2.
	 */
	public Seconds tt;
	/**
	 * Water inertia time constant (Tw).  Typical Value = 1.
	 */
	public Seconds tw;
	/**
	 * Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.2.
	 */
	public Float velcl;
	/**
	 * Maximum gate opening velocity (Velop).  Unit = PU/sec. Typical Value = 0.2.
	 */
	public Float velop;

	public GovHydro3(){

	}
}//end GovHydro3