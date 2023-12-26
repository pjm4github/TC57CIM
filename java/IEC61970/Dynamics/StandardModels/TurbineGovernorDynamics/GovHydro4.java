package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;

/**
 * Hydro turbine and governor. Represents plants with straight-forward penstock
 * configurations and hydraulic governors of traditional 'dashpot' type.  This
 * model can be used to represent simple, Francis, Pelton or Kaplan turbines.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovHydro4 extends TurbineGovernorDynamics {

	/**
	 * Turbine gain (At).  Typical Value = 1.2.
	 */
	public PU at;
	/**
	 * Kaplan blade servo point 0 (Bgv0).  Typical Value = 0.
	 */
	public PU bgv0;
	/**
	 * Kaplan blade servo point 1 (Bgv1).  Typical Value = 0.
	 */
	public PU bgv1;
	/**
	 * Kaplan blade servo point 2 (Bgv2).
	 * Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.1.
	 */
	public PU bgv2;
	/**
	 * Kaplan blade servo point 3 (Bgv3).
	 * Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.667.
	 */
	public PU bgv3;
	/**
	 * Kaplan blade servo point 4 (Bgv4).
	 * Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.9.
	 */
	public PU bgv4;
	/**
	 * Kaplan blade servo point 5 (Bgv5).
	 * Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.
	 */
	public PU bgv5;
	/**
	 * Maximum blade adjustment factor (Bmax).
	 * Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.1276.
	 */
	public Float bmax;
	/**
	 * Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency db1;
	/**
	 * Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
	 */
	public ActivePower db2;
	/**
	 * Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed
	 * (PU).
	 * Typical Value = 0.5.  Typical Value Francis = 1.1, Kaplan = 1.1.
	 */
	public PU dturb;
	/**
	 * Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency eps;
	/**
	 * Maximum gate opening, PU of MWbase (Gmax).  Typical Value = 1.
	 */
	public PU gmax;
	/**
	 * Minimum gate opening, PU of MWbase (Gmin).  Typical Value = 0.
	 */
	public PU gmin;
	/**
	 * Nonlinear gain point 0, PU gv (Gv0).
	 * Typical Value = 0.  Typical Value Francis = 0.1, Kaplan = 0.1.
	 */
	public PU gv0;
	/**
	 * Nonlinear gain point 1, PU gv (Gv1).
	 * Typical Value = 0.  Typical Value Francis = 0.4, Kaplan = 0.4.
	 */
	public PU gv1;
	/**
	 * Nonlinear gain point 2, PU gv (Gv2).
	 * Typical Value = 0.  Typical Value Francis = 0.5, Kaplan = 0.5.
	 */
	public PU gv2;
	/**
	 * Nonlinear gain point 3, PU gv (Gv3).
	 * Typical Value = 0.  Typical Value Francis = 0.7, Kaplan = 0.7.
	 */
	public PU gv3;
	/**
	 * Nonlinear gain point 4, PU gv (Gv4).
	 * Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.8.
	 */
	public PU gv4;
	/**
	 * Nonlinear gain point 5, PU gv (Gv5).
	 * Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.9.
	 */
	public PU gv5;
	/**
	 * Head available at dam (hdam).  Typical Value = 1.
	 */
	public PU hdam;
	/**
	 * Base for power values (MWbase) (>0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Nonlinear gain point 0, PU power (Pgv0).  Typical Value = 0.
	 */
	public PU pgv0;
	/**
	 * Nonlinear gain point 1, PU power (Pgv1).
	 * Typical Value = 0.  Typical Value Francis = 0.42, Kaplan = 0.35.
	 */
	public PU pgv1;
	/**
	 * Nonlinear gain point 2, PU power (Pgv2).
	 * Typical Value = 0.  Typical Value Francis = 0.56, Kaplan = 0.468.
	 */
	public PU pgv2;
	/**
	 * Nonlinear gain point 3, PU power (Pgv3).
	 * Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.796.
	 */
	public PU pgv3;
	/**
	 * Nonlinear gain point 4, PU power (Pgv4).
	 * Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.917.
	 */
	public PU pgv4;
	/**
	 * Nonlinear gain point 5, PU power (Pgv5).
	 * Typical Value = 0.  Typical Value Francis = 0.97, Kaplan = 0.99.
	 */
	public PU pgv5;
	/**
	 * No-load flow at nominal head (Qnl).
	 * Typical Value = 0.08.  Typical Value Francis = 0, Kaplan = 0.
	 */
	public PU qn1;
	/**
	 * Permanent droop (Rperm).  Typical Value = 0.05.
	 */
	public Seconds rperm;
	/**
	 * Temporary droop (Rtemp).  Typical Value = 0.3.
	 */
	public Seconds rtemp;
	/**
	 * Blade servo time constant (Tblade).  Typical Value = 100.
	 */
	public Seconds tblade;
	/**
	 * Gate servo time constant (Tg) (>0).  Typical Value = 0.5.
	 */
	public Seconds tg;
	/**
	 * Pilot servo time constant (Tp).  Typical Value = 0.1.
	 */
	public Seconds tp;
	/**
	 * Dashpot time constant (Tr) (>0).  Typical Value = 5.
	 */
	public Seconds tr;
	/**
	 * Water inertia time constant (Tw) (>0).  Typical Value = 1.
	 */
	public Seconds tw;
	/**
	 * Max gate closing velocity (Uc).  Typical Value = 0.2.
	 */
	public Float uc;
	/**
	 * Max gate opening velocity (Uo).  Typical Value = 0.2.
	 */
	public Float uo;

	public GovHydro4(){

	}
}//end GovHydro4