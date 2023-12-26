package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;

/**
 * IEEE steam turbine governor model.
 * 
 * Ref<font color="#0f0f0f">erence: IEEE Transactions on Power Apparatus and
 * Systems</font>
 * <font color="#0f0f0f">November/December 1973, Volume PAS-92, Number 6</font>
 * <font color="#0f0f0f"><i><u>Dynamic Models for Steam and Hydro Turbines in
 * Power System Studies</u></i>, Page 1904.</font>
 * 
 * <b>Parameter Notes:</b>
 * <ol>
 * 	<li>Per unit parameters are on base of <b>MWbase</b>, which is normally the MW
 * capability of the turbine.</li>
 * 	<li><b>T3</b> must be greater than zero.  All other time constants may be zero.
 * </li>
 * 	<li>For a tandem-compound turbine the parameters <b>K2</b>, <b>K4</b>,
 * <b>K6</b>, and <b>K8</b> are ignored. For a cross-compound turbine, two
 * generators are connected to this turbine-governor model.</li>
 * 	<li>Each generator must be represented in the load flow by data on its own MVA
 * base.  The values of <b>K1</b>, <b>K3</b>, <b>K5</b>, <b>K7</b> must be
 * specified to describe the proportionate development of power on the first
 * turbine shaft.  <b>K2</b>, <b>K4</b>, <b>K6</b>, <b>K8</b> must describe the
 * second turbine shaft. Normally <b>K1</b> + <b>K3</b> + <b>K5</b> + <b>K7</b> =
 * 1.0 and <b>K2</b> + <b>K4</b> + <b>K6</b> + <b>K8</b> = 1.0  (if second
 * generator is present).</li>
 * 	<li>The division of power between the two shafts is in proportion to the
 * values of MVA bases of the two generators.  The initial condition load flow
 * should, therefore, have the two generators loaded to the same fraction of each
 * one's MVA base.</li>
 * </ol>
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class GovSteamIEEE1 extends TurbineGovernorDynamics {

	/**
	 * Governor gain (reciprocal of droop) (K) (> 0).  Typical Value = 25.
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
	 * Base for power values (MWbase) (> 0)<i>.</i>
	 */
	public ActivePower mwbase;
	/**
	 * Maximum valve opening (Pmax) (> Pmin).  Typical Value = 1.
	 */
	public PU pmax;
	/**
	 * Minimum valve opening (Pmin) (>= 0).  Typical Value = 0.
	 */
	public PU pmin;
	/**
	 * Governor lag time constant (T1).  Typical Value = 0.
	 */
	public Seconds t1;
	/**
	 * Governor lead time constant (T2).  Typical Value = 0.
	 */
	public Seconds t2;
	/**
	 * Valve positioner time constant (T3) (> 0).  Typical Value = 0.1.
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
	 * Maximum valve closing velocity (Uc) (< 0).  Unit = PU/sec.  Typical Value = -10.
	 */
	public Float uc;
	/**
	 * Maximum valve opening velocity (Uo) (> 0).  Unit = PU/sec.  Typical Value = 1.
	 */
	public Float uo;

	public GovSteamIEEE1(){

	}
}//end GovSteamIEEE1