package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Simplified governor model.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class GovSteam2 extends TurbineGovernorDynamics {

	/**
	 * Frequency dead band (DBF).  Typical Value = 0.
	 */
	public PU dbf;
	/**
	 * Governor gain (reciprocal of droop) (K).  Typical Value = 20.
	 */
	public Float k;
	/**
	 * Fuel flow maximum negative error value (MN<sub>EF</sub>).  Typical Value = -1.
	 */
	public PU mnef;
	/**
	 * Fuel flow maximum positive error value (MX<sub>EF</sub>).  Typical Value = 1.
	 */
	public PU mxef;
	/**
	 * Maximum fuel flow (P<sub>MAX</sub>).  Typical Value = 1.
	 */
	public PU pmax;
	/**
	 * Minimum fuel flow (P<sub>MIN</sub>).  Typical Value = 0.
	 */
	public PU pmin;
	/**
	 * Governor lag time constant (T<sub>1</sub>) (>0).  Typical Value = 0.45.
	 */
	public Seconds t1;
	/**
	 * Governor lead time constant (T<sub>2</sub>) (may be 0).  Typical Value = 0.
	 */
	public Seconds t2;

	public GovSteam2(){

	}
}//end GovSteam2