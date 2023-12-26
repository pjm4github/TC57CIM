package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;

/**
 * IEEE Simplified Hydro Governor-Turbine Model.  Used for Mechanical-Hydraulic
 * and Electro-Hydraulic turbine governors, with our without steam feedback.
 * Typical values given are for Mechanical-Hydraulic.
 * 
 * Ref<font color="#0f0f0f">erence: IEEE Transactions on Power Apparatus and
 * Systems</font>
 * <font color="#0f0f0f">November/December 1973, Volume PAS-92, Number 6</font>
 * <font color="#0f0f0f"><i><u>Dynamic Models for Steam and Hydro Turbines in
 * Power System Studies</u></i>, Page 1904.</font>
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovHydroIEEE0 extends TurbineGovernorDynamics {

	/**
	 * Governor gain (K<i>)</i>.
	 */
	public PU k;
	/**
	 * Base for power values (MWbase) (> 0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Gate maximum (Pmax). 
	 */
	public PU pmax;
	/**
	 * Gate minimum (Pmin). 
	 */
	public PU pmin;
	/**
	 * Governor lag time constant (T1).  Typical Value = 0.25.
	 */
	public Seconds t1;
	/**
	 * Governor lead time constant (T2<i>)</i>.  Typical Value = 0.
	 */
	public Seconds t2;
	/**
	 * Gate actuator time constant (T3).  Typical Value = 0.1.
	 */
	public Seconds t3;
	/**
	 * Water starting time (T4). 
	 */
	public Seconds t4;

	public GovHydroIEEE0(){

	}
}//end GovHydroIEEE0