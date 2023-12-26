package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Float;

/**
 * Double derivative hydro governor and turbine.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovHydroDD extends TurbineGovernorDynamics {

	/**
	 * Turbine numerator multiplier (Aturb) (note 3).  Typical Value = -1.
	 */
	public PU aturb;
	/**
	 * Turbine denominator multiplier (Bturb) (note 3).  Typical Value = 0.5.
	 */
	public PU bturb;
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
	 * Maximum gate opening (Gmax).  Typical Value = 0.
	 */
	public PU gmax;
	/**
	 * Minimum gate opening (Gmin).  Typical Value = 0.
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
	 * Input signal switch (Flag).
	 * true = Pe input is used
	 * false = feedback is received from CV.
	 * Flag is normally dependent on Tt.  If Tf is zero, Flag is set to false. If Tf
	 * is not zero, Flag is set to true.
	 * Typical Value = true.
	 */
	public Boolean inputSignal;
	/**
	 * Single derivative gain (K1).  Typical Value = 3.6.
	 */
	public PU k1;
	/**
	 * Double derivative gain (K2).  Typical Value = 0.2.
	 */
	public PU k2;
	/**
	 * Gate servo gain (Kg).  Typical Value = 3.
	 */
	public PU kg;
	/**
	 * Integral gain (Ki).  Typical Value = 1.
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
	 * Steady state droop (R).  Typical Value = 0.05.
	 */
	public PU r;
	/**
	 * Input filter time constant (Td).  Typical Value = 0.
	 */
	public Seconds td;
	/**
	 * Washout time constant (Tf).  Typical Value = 0.1.
	 */
	public Seconds tf;
	/**
	 * Gate servo time constant (Tp).  Typical Value = 0.35.
	 */
	public Seconds tp;
	/**
	 * Power feedback time constant (Tt).  Typical Value = 0.02.
	 */
	public Seconds tt;
	/**
	 * Turbine time constant (Tturb) (note 3).  Typical Value = 0.8.
	 */
	public Seconds tturb;
	/**
	 * Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.14.
	 */
	public Float velcl;
	/**
	 * Maximum gate opening velocity (Velop).  Unit = PU/sec.  Typical Value = 0.09.
	 */
	public Float velop;

	public GovHydroDD(){

	}
}//end GovHydroDD