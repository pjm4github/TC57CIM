package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;

/**
 * Transformer fed static excitation system (static with ABB regulator). This
 * model represents a static excitation system in which a gated thyristor bridge
 * fed by a transformer at the main generator terminals feeds the main generator
 * directly.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcBBC extends ExcitationSystemDynamics {

	/**
	 * Maximum open circuit exciter voltage (Efdmax).  Typical Value = 5.
	 */
	public PU efdmax;
	/**
	 * Minimum open circuit exciter voltage (Efdmin).  Typical Value = -5.
	 */
	public PU efdmin;
	/**
	 * Steady state gain (K).  Typical Value = 300.
	 */
	public PU k;
	/**
	 * Supplementary signal routing selector (switch).
	 * true = Vs connected to 3rd summing point
	 * false =  Vs connected to 1st summing point (see diagram).
	 * Typical Value = true.
	 */
	public Boolean switch;
	/**
	 * Controller time constant (T1).  Typical Value = 6.
	 */
	public Seconds t1;
	/**
	 * Controller time constant (T2).  Typical Value = 1.
	 */
	public Seconds t2;
	/**
	 * Lead/lag time constant (T3).  Typical Value = 0.05.
	 */
	public Seconds t3;
	/**
	 * Lead/lag time constant (T4).  Typical Value = 0.01.
	 */
	public Seconds t4;
	/**
	 * Maximum control element output (Vrmax).  Typical Value = 5.
	 */
	public PU vrmax;
	/**
	 * Minimum control element output (Vrmin).  Typical Value = -5.
	 */
	public PU vrmin;
	/**
	 * Effective excitation transformer reactance (Xe).  Typical Value = 0.05.
	 */
	public PU xe;

	public ExcBBC(){

	}
}//end ExcBBC