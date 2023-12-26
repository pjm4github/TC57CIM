package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Generic turbogas.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovGAST4 extends TurbineGovernorDynamics {

	/**
	 * Droop (bp).  Typical Value = 0.05.
	 */
	public PU bp;
	/**
	 * Compressor gain (K<sub>tm</sub>).  Typical Value = 0.
	 */
	public PU ktm;
	/**
	 * Fuel flow maximum negative error value (MN<sub>EF</sub>).  Typical Value = -0.
	 * 05.
	 */
	public PU mnef;
	/**
	 * Fuel flow maximum positive error value (MX<sub>EF</sub>).  Typical Value = 0.05.
	 */
	public PU mxef;
	/**
	 * Minimum valve opening (RYMN).  Typical Value = 0.
	 */
	public PU rymn;
	/**
	 * Maximum valve opening (RYMX).  Typical Value = 1.1.
	 */
	public PU rymx;
	/**
	 * Maximum gate opening velocity (T<sub>A</sub>).  Typical Value = 3.
	 */
	public Seconds ta;
	/**
	 * Maximum gate closing velocity (T<sub>c</sub>).  Typical Value = 0.5.
	 */
	public Seconds tc;
	/**
	 * Fuel control time constant (T<sub>cm</sub>).  Typical Value = 0.1.
	 */
	public Seconds tcm;
	/**
	 * Compressor discharge volume time constant (T<sub>m</sub>).  Typical Value = 0.2.
	 */
	public Seconds tm;
	/**
	 * Time constant of fuel valve positioner (T<sub>y</sub>).  Typical Value = 0.1.
	 */
	public Seconds tv;

	public GovGAST4(){

	}
}//end GovGAST4