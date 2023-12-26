package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Float;

/**
 * Fourth order lead-lag governor and hydro turbine.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovHydroR extends TurbineGovernorDynamics {

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
	 * Maximum governor output (Gmax).  Typical Value = 1.05.
	 */
	public PU gmax;
	/**
	 * Minimum governor output (Gmin).  Typical Value = -0.05.
	 */
	public PU gmin;
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
	 * Input signal switch (Flag).
	 * true = Pe input is used
	 * false = feedback is received from CV.
	 * Flag is normally dependent on Tt.  If Tf is zero, Flag is set to false. If Tf
	 * is not zero, Flag is set to true.  Typical Value = true.
	 */
	public Boolean inputSignal;
	/**
	 * Gate servo gain (Kg).  Typical Value = 2.
	 */
	public PU kg;
	/**
	 * Integral gain (Ki).  Typical Value = 0.5.
	 */
	public PU ki;
	/**
	 * Base for power values (MWbase) (>0).  Unit = MW.
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
	 * Steady-state droop (R).  Typical Value = 0.05.
	 */
	public PU r;
	/**
	 * Lead time constant 1 (T1).  Typical Value = 1.5.
	 */
	public Seconds t1;
	/**
	 * Lag time constant 1 (T2).  Typical Value = 0.1.
	 */
	public Seconds t2;
	/**
	 * Lead time constant 2 (T3).  Typical Value = 1.5.
	 */
	public Seconds t3;
	/**
	 * Lag time constant 2 (T4).  Typical Value = 0.1.
	 */
	public Seconds t4;
	/**
	 * Lead time constant 3 (T5).  Typical Value = 0.
	 */
	public Seconds t5;
	/**
	 * Lag time constant 3 (T6).  Typical Value = 0.05.
	 */
	public Seconds t6;
	/**
	 * Lead time constant 4 (T7).  Typical Value = 0.
	 */
	public Seconds t7;
	/**
	 * Lag time constant 4 (T8).  Typical Value = 0.05.
	 */
	public Seconds t8;
	/**
	 * Input filter time constant (Td).  Typical Value = 0.05.
	 */
	public Seconds td;
	/**
	 * Gate servo time constant (Tp).  Typical Value = 0.05.
	 */
	public Seconds tp;
	/**
	 * Power feedback time constant (Tt).  Typical Value = 0.
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
	 * Maximum gate opening velocity (Velop).  Unit = PU/sec.  Typical Value = 0.2.
	 */
	public Float velop;

	public GovHydroR(){

	}
}//end GovHydroR