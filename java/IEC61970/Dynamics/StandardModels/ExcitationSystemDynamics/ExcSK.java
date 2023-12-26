package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.ApparentPower;
import IEC61970.Base.Domain.Seconds;

/**
 * Slovakian Excitation System Model.  UEL and secondary voltage control are
 * included in this model. When this model is used, there cannot be a separate
 * underexcitation limiter or VAr controller model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcSK extends ExcitationSystemDynamics {

	/**
	 * Field voltage clipping limit (Efdmax). 
	 */
	public PU efdmax;
	/**
	 * Field voltage clipping limit (Efdmin). 
	 */
	public PU efdmin;
	/**
	 * Maximum field voltage output (Emax).  Typical Value = 20.
	 */
	public PU emax;
	/**
	 * Minimum field voltage output (Emin).  Typical Value = -20.
	 */
	public PU emin;
	/**
	 * Gain (K).  Typical Value = 1.
	 */
	public PU k;
	/**
	 * Parameter of underexcitation limit (K1).  Typical Value = 0.1364.
	 */
	public PU k1;
	/**
	 * Parameter of underexcitation limit (K2).  Typical Value = -0.3861.
	 */
	public PU k2;
	/**
	 * PI controller gain (Kc).  Typical Value = 70.
	 */
	public PU kc;
	/**
	 * Rectifier regulation factor (Kce).  Typical Value = 0.
	 */
	public PU kce;
	/**
	 * Exciter internal reactance (Kd).  Typical Value = 0.
	 */
	public PU kd;
	/**
	 * P controller gain (Kgob).  Typical Value = 10.
	 */
	public PU kgob;
	/**
	 * PI controller gain (Kp).  Typical Value = 1.
	 */
	public PU kp;
	/**
	 * PI controller gain of integral component (Kqi).  Typical Value = 0.
	 */
	public PU kqi;
	/**
	 * Rate of rise of the reactive power (Kqob). 
	 */
	public PU kqob;
	/**
	 * PI controller gain (Kqp).  Typical Value = 0.
	 */
	public PU kqp;
	/**
	 * Dead band of reactive power (nq).  Determines the range of sensitivity.
	 * Typical Value = 0.001.
	 */
	public PU nq;
	/**
	 * Secondary voltage control state (Qc_on_off).
	 * true = secondary voltage control is ON
	 * false = secondary voltage control is OFF.
	 * Typical Value = false.
	 */
	public Boolean qconoff;
	/**
	 * Desired value (setpoint) of reactive power, manual setting (Qz). 
	 */
	public PU qz;
	/**
	 * Selector to apply automatic calculation in secondary controller model.
	 * true = automatic calculation is activated
	 * false = manual set is active; the use of desired value of reactive power (Qz)
	 * is required.
	 * Typical Value = true.
	 */
	public Boolean remote;
	/**
	 * Apparent power of the unit (Sbase).  Unit = MVA.  Typical Value = 259.
	 */
	public ApparentPower sbase;
	/**
	 * PI controller phase lead time constant (Tc).  Typical Value = 8.
	 */
	public Seconds tc;
	/**
	 * Time constant of gain block (Te).  Typical Value = 0.1.
	 */
	public Seconds te;
	/**
	 * PI controller phase lead time constant (Ti).  Typical Value = 2.
	 */
	public Seconds ti;
	/**
	 * Time constant (Tp).  Typical Value = 0.1.
	 */
	public Seconds tp;
	/**
	 * Voltage transducer time constant (Tr).  Typical Value = 0.01.
	 */
	public Seconds tr;
	/**
	 * Maximum error (Uimax).  Typical Value = 10.
	 */
	public PU uimax;
	/**
	 * Minimum error (UImin).  Typical Value = -10.
	 */
	public PU uimin;
	/**
	 * Maximum controller output (URmax).  Typical Value = 10.
	 */
	public PU urmax;
	/**
	 * Minimum controller output (URmin).  Typical Value = -10.
	 */
	public PU urmin;
	/**
	 * Maximum terminal voltage input (Vtmax).  Determines the range of voltage dead
	 * band.  Typical Value = 1.05.
	 */
	public PU vtmax;
	/**
	 * Minimum terminal voltage input (Vtmin).  Determines the range of voltage dead
	 * band.  Typical Value = 0.95.
	 */
	public PU vtmin;
	/**
	 * Maximum output (Yp).  Minimum output = 0.  Typical Value = 1.
	 */
	public PU yp;

	public ExcSK(){

	}
}//end ExcSK