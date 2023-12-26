package IEC61970.Dynamics.StandardModels.LoadDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * This model combines static load and induction motor load effects.
 * The dynamics of the motor are simplified by linearizing the induction machine
 * equations.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class LoadComposite extends LoadDynamics {

	/**
	 * Active load-frequency dependence index (dynamic) (Epfd).  Typical Value = 1.5.
	 */
	public Float epfd;
	/**
	 * Active load-frequency dependence index (static) (Epfs).  Typical Value = 1.5.
	 */
	public Float epfs;
	/**
	 * Active load-voltage dependence index (dynamic) (Epvd).  Typical Value = 0.7.
	 */
	public Float epvd;
	/**
	 * Active load-voltage dependence index (static) (Epvs).  Typical Value = 0.7.
	 */
	public Float epvs;
	/**
	 * Reactive load-frequency dependence index (dynamic) (Eqfd).  Typical Value = 0.
	 */
	public Float eqfd;
	/**
	 * Reactive load-frequency dependence index (static) (Eqfs).  Typical Value = 0.
	 */
	public Float eqfs;
	/**
	 * Reactive load-voltage dependence index (dynamic) (Eqvd).  Typical Value = 2.
	 */
	public Float eqvd;
	/**
	 * Reactive load-voltage dependence index (static) (Eqvs).  Typical Value = 2.
	 */
	public Float eqvs;
	/**
	 * Inertia constant (H).  Typical Value = 2.5.
	 */
	public Seconds h;
	/**
	 * Loading factor - ratio of initial P to motor MVA base (Lfrac).  Typical Value =
	 * 0.8.
	 */
	public Float lfrac;
	/**
	 * Fraction of constant-power load to be represented by this motor model (Pfrac)
	 * (>=0.0 and <=1.0).  Typical Value = 0.5.
	 */
	public Float pfrac;

	public LoadComposite(){

	}
}//end LoadComposite