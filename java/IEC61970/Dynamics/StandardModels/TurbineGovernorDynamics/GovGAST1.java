package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified single shaft gas turbine.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovGAST1 extends TurbineGovernorDynamics {

	/**
	 * Turbine power time constant numerator scale factor (a).  Typical Value = 0.8.
	 */
	public Float a;
	/**
	 * Turbine power time constant denominator scale factor (b).  Typical Value = 1.
	 */
	public Float b;
	/**
	 * Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency db1;
	/**
	 * Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
	 */
	public ActivePower db2;
	/**
	 * Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency eps;
	/**
	 * Fuel flow at zero power output (Fidle).  Typical Value = 0.18.
	 */
	public PU fidle;
	/**
	 * Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0.
	 */
	public PU gv1;
	/**
	 * Nonlinear gain point 2,PU gv (Gv2).  Typical Value = 0.
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
	 * Governor gain (Ka).  Typical Value = 0.
	 */
	public PU ka;
	/**
	 * Temperature limiter gain (Kt).  Typical Value = 3.
	 */
	public PU kt;
	/**
	 * Ambient temperature load limit (Lmax).  Lmax is the turbine power output
	 * corresponding to the limiting exhaust gas temperature.  Typical Value = 1.
	 */
	public PU lmax;
	/**
	 * Valve position change allowed at fast rate (Loadinc).  Typical Value = 0.05.
	 */
	public PU loadinc;
	/**
	 * Maximum long term fuel valve opening rate (Ltrate).  Typical Value = 0.02.
	 */
	public Float ltrate;
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
	 * Permanent droop (R).  Typical Value = 0.04.
	 */
	public PU r;
	/**
	 * Maximum fuel valve opening rate (Rmax).  Unit = PU/sec.  Typical Value = 1.
	 */
	public Float rmax;
	/**
	 * Governor mechanism time constant (T1).  T1 represents the natural valve
	 * positioning time constant of the governor for small disturbances, as seen when
	 * rate limiting is not in effect.  Typical Value = 0.5.
	 */
	public Seconds t1;
	/**
	 * Turbine power time constant (T2).  T2 represents delay due to internal energy
	 * storage of the gas turbine engine. T2 can be used to give a rough approximation
	 * to the delay associated with acceleration of the compressor spool of a multi-
	 * shaft engine, or with the compressibility of gas in the plenum of the free
	 * power turbine of an aero-derivative unit, for example.  Typical Value = 0.5.
	 */
	public Seconds t2;
	/**
	 * Turbine exhaust temperature time constant (T3).  T3 represents delay in the
	 * exhaust temperature and load limiting system. Typical Value = 3.
	 */
	public Seconds t3;
	/**
	 * Governor lead time constant (T4).  Typical Value = 0.
	 */
	public Seconds t4;
	/**
	 * Governor lag time constant (T5).  Typical Value = 0.
	 */
	public Seconds t5;
	/**
	 * Valve position averaging time constant (Tltr).  Typical Value = 10.
	 */
	public Seconds tltr;
	/**
	 * Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1.
	 */
	public PU vmax;
	/**
	 * Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0.
	 */
	public PU vmin;

	public GovGAST1(){

	}
}//end GovGAST1