package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Hungarian Excitation System Model, with built-in voltage transducer.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcHU extends ExcitationSystemDynamics {

	/**
	 * Major loop PI tag gain factor (Ae).  Typical Value = 3.
	 */
	public PU ae;
	/**
	 * Minor loop PI tag gain factor (Ai).  Typical Value = 22.
	 */
	public PU ai;
	/**
	 * AVR constant (Atr).  Typical Value = 2.19.
	 */
	public PU atr;
	/**
	 * Field voltage control signal upper limit on AVR base (Emax).  Typical Value = 0.
	 * 996.
	 */
	public PU emax;
	/**
	 * Field voltage control signal lower limit on AVR base (Emin).  Typical Value = -
	 * 0.866.
	 */
	public PU emin;
	/**
	 * Major loop PI tag output signal upper limit (Imax).  Typical Value = 2.19.
	 */
	public PU imax;
	/**
	 * Major loop PI tag output signal lower limit (Imin).  Typical Value = 0.1.
	 */
	public PU imin;
	/**
	 * Voltage base conversion constant (Ke).  Typical Value = 4.666.
	 */
	public Float ke;
	/**
	 * Current base conversion constant (Ki).  Typical Value = 0.21428.
	 */
	public Float ki;
	/**
	 * Major loop PI tag integration time constant (Te).  Typical Value = 0.154.
	 */
	public Seconds te;
	/**
	 * Minor loop PI control tag integration time constant (Ti).  Typical Value = 0.
	 * 01333.
	 */
	public Seconds ti;
	/**
	 * Filter time constant (Tr). If a voltage compensator is used in conjunction with
	 * this excitation system model, Tr should be set to 0.  Typical Value = 0.01.
	 */
	public Seconds tr;

	public ExcHU(){

	}
}//end ExcHU