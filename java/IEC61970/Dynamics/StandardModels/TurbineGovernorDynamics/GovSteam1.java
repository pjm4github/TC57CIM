package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;

/**
 * Steam turbine governor model, based on the GovSteamIEEE1 model  (with optional
 * deadband and nonlinear valve gain added).
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovSteam1 extends TurbineGovernorDynamics {

	/**
	 * Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency db1;
	/**
	 * Unintentional deadband (db2).  Unit = MW.  Typical Value = 0.
	 */
	public ActivePower db2;
	/**
	 * Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency eps;
	/**
	 * Nonlinear gain valve position point 1 (GV1).  Typical Value = 0.
	 */
	public PU gv1;
	/**
	 * Nonlinear gain valve position point 2 (GV2).  Typical Value = 0.4.
	 */
	public PU gv2;
	/**
	 * Nonlinear gain valve position point 3 (GV3).  Typical Value = 0.5.
	 */
	public PU gv3;
	/**
	 * Nonlinear gain valve position point 4 (GV4).  Typical Value = 0.6.
	 */
	public PU gv4;
	/**
	 * Nonlinear gain valve position point 5 (GV5).  Typical Value = 1.
	 */
	public PU gv5;
	/**
	 * Nonlinear gain valve position point 6 (GV6).  Typical Value = 0.
	 */
	public PU gv6;
	/**
	 * Governor gain (reciprocal of droop) (K) (>0).  Typical Value = 25.
	 */
	public PU k;
	/**
	 * Fraction of HP shaft power after first boiler pass (K1).  Typical Value = 0.2.
	 */
	public Float k1;
	/**
	 * Fraction of LP shaft power after first boiler pass (K2).  Typical Value = 0.
	 */
	public Float k2;
	/**
	 * Fraction of HP shaft power after second boiler pass (K3).  Typical Value = 0.3.
	 */
	public Float k3;
	/**
	 * Fraction of LP shaft power after second boiler pass (K4).  Typical Value = 0.
	 */
	public Float k4;
	/**
	 * Fraction of HP shaft power after third boiler pass (K5).  Typical Value = 0.5.
	 */
	public Float k5;
	/**
	 * Fraction of LP shaft power after third boiler pass (K6).  Typical Value = 0.
	 */
	public Float k6;
	/**
	 * Fraction of HP shaft power after fourth boiler pass (K7).  Typical Value = 0.
	 */
	public Float k7;
	/**
	 * Fraction of LP shaft power after fourth boiler pass (K8).  Typical Value = 0.
	 */
	public Float k8;
	/**
	 * Base for power values (MWbase) (>0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Nonlinear gain power value point 1 (Pgv1).  Typical Value = 0.
	 */
	public PU pgv1;
	/**
	 * Nonlinear gain power value point 2 (Pgv2).  Typical Value = 0.75.
	 */
	public PU pgv2;
	/**
	 * Nonlinear gain power value point 3 (Pgv3).  Typical Value = 0.91.
	 */
	public PU pgv3;
	/**
	 * Nonlinear gain power value point 4 (Pgv4).  Typical Value = 0.98.
	 */
	public PU pgv4;
	/**
	 * Nonlinear gain power value point 5 (Pgv5).  Typical Value = 1.
	 */
	public PU pgv5;
	/**
	 * Nonlinear gain power value point 6 (Pgv6).  Typical Value = 0.
	 */
	public PU pgv6;
	/**
	 * Maximum valve opening (Pmax) (> Pmin).  Typical Value = 1.
	 */
	public PU pmax;
	/**
	 * Minimum valve opening (Pmin) (>=0).  Typical Value = 0.
	 */
	public PU pmin;
	/**
	 * Intentional deadband indicator.
	 * true = intentional deadband is applied
	 * false = intentional deadband is not applied.
	 * Typical Value = true.
	 */
	public Boolean sdb1;
	/**
	 * Unintentional deadband location.
	 * true = intentional deadband is applied before point "A"
	 * false = intentional deadband is applied after point "A".
	 * Typical Value = true.
	 */
	public Boolean sdb2;
	/**
	 * Governor lag time constant (T1).  Typical Value = 0.
	 */
	public Seconds t1;
	/**
	 * Governor lead time constant (T2).  Typical Value = 0.
	 */
	public Seconds t2;
	/**
	 * Valve positioner time constant (T3<i>) </i>(>0).  Typical Value = 0.1.
	 */
	public Seconds t3;
	/**
	 * Inlet piping/steam bowl time constant (T4).  Typical Value = 0.3.
	 */
	public Seconds t4;
	/**
	 * Time constant of second boiler pass (T5).  Typical Value = 5.
	 */
	public Seconds t5;
	/**
	 * Time constant of third boiler pass (T6).  Typical Value = 0.5.
	 */
	public Seconds t6;
	/**
	 * Time constant of fourth boiler pass (T7).  Typical Value = 0.
	 */
	public Seconds t7;
	/**
	 * Maximum valve closing velocity (Uc) (<0).  Unit = PU/sec.  Typical Value = -10.
	 */
	public Float uc;
	/**
	 * Maximum valve opening velocity (Uo) (>0).  Unit = PU/sec.  Typical Value = 1.
	 */
	public Float uo;
	/**
	 * Nonlinear valve characteristic.
	 * true = nonlinear valve characteristic is used
	 * false = nonlinear valve characteristic is not used.
	 * Typical Value = true.
	 */
	public Boolean valve;

	public GovSteam1(){

	}
}//end GovSteam1