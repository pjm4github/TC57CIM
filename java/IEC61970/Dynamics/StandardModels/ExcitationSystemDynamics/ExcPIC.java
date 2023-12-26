package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Proportional/Integral Regulator Excitation System Model.  This model can be
 * used to represent excitation systems with a proportional-integral (PI) voltage
 * regulator controller.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcPIC extends ExcitationSystemDynamics {

	/**
	 * Field voltage value 1 (E1).  Typical Value = 0.
	 */
	public PU e1;
	/**
	 * Field voltage value 2 (E2).  Typical Value = 0.
	 */
	public PU e2;
	/**
	 * Exciter maximum limit (Efdmax).  Typical Value = 8.
	 */
	public PU efdmax;
	/**
	 * Exciter minimum limit (Efdmin).  Typical Value = -0.87.
	 */
	public PU efdmin;
	/**
	 * PI controller gain (Ka).  Typical Value = 3.15.
	 */
	public PU ka;
	/**
	 * Exciter regulation factor (Kc).  Typical Value = 0.08.
	 */
	public PU kc;
	/**
	 * Exciter constant (Ke).  Typical Value = 0.
	 */
	public PU ke;
	/**
	 * Rate feedback gain (Kf).  Typical Value = 0.
	 */
	public PU kf;
	/**
	 * Current source gain (Ki).  Typical Value = 0.
	 */
	public PU ki;
	/**
	 * Potential source gain (Kp).  Typical Value = 6.5.
	 */
	public PU kp;
	/**
	 * Saturation factor at E1 (Se1).  Typical Value = 0.
	 */
	public PU se1;
	/**
	 * Saturation factor at E2 (Se2).  Typical Value = 0.
	 */
	public PU se2;
	/**
	 * PI controller time constant (Ta1).  Typical Value = 1.
	 */
	public Seconds ta1;
	/**
	 * Voltage regulator time constant (Ta2).  Typical Value = 0.01.
	 */
	public Seconds ta2;
	/**
	 * Lead time constant (Ta3).  Typical Value = 0.
	 */
	public Seconds ta3;
	/**
	 * Lag time constant (Ta4).  Typical Value = 0.
	 */
	public Seconds ta4;
	/**
	 * Exciter time constant (Te).  Typical Value = 0.
	 */
	public Seconds te;
	/**
	 * Rate feedback time constant (Tf1).  Typical Value = 0.
	 */
	public Seconds tf1;
	/**
	 * Rate feedback lag time constant (Tf2).  Typical Value = 0.
	 */
	public Seconds tf2;
	/**
	 * PI maximum limit (Vr1).  Typical Value = 1.
	 */
	public PU vr1;
	/**
	 * PI minimum limit (Vr2).  Typical Value = -0.87.
	 */
	public PU vr2;
	/**
	 * Voltage regulator maximum limit (Vrmax).  Typical Value = 1.
	 */
	public PU vrmax;
	/**
	 * Voltage regulator minimum limit (Vrmin).  Typical Value = -0.87.
	 */
	public PU vrmin;

	public ExcPIC(){

	}
}//end ExcPIC