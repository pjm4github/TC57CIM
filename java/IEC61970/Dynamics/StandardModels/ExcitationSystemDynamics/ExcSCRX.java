package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Simple excitation system model representing generic characteristics of many
 * excitation systems; intended for use where negative field current may be a
 * problem.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcSCRX extends ExcitationSystemDynamics {

	/**
	 * Power source switch (Cswitch).
	 * true = fixed voltage of 1.0 PU
	 * false = generator terminal voltage.
	 */
	public Boolean cswitch;
	/**
	 * Maximum field voltage output (Emax).  Typical Value = 5.
	 */
	public PU emax;
	/**
	 * Minimum field voltage output (Emin).  Typical Value = 0.
	 */
	public PU emin;
	/**
	 * Gain (K) (>0).  Typical Value = 200.
	 */
	public PU k;
	/**
	 * Rc/Rfd - ratio of field discharge resistance to field winding resistance
	 * (RcRfd).  Typical Value = 0.
	 */
	public Float rcrfd;
	/**
	 * Ta/Tb - gain reduction ratio of lag-lead element (TaTb). The parameter Ta is
	 * not defined explicitly.  Typical Value = 0.1.
	 */
	public Float tatb;
	/**
	 * Denominator time constant of lag-lead block (Tb).  Typical Value = 10.
	 */
	public Seconds tb;
	/**
	 * Time constant of gain block (Te) (>0).  Typical Value = 0.02.
	 */
	public Seconds te;

	public ExcSCRX(){

	}
}//end ExcSCRX