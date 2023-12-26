package IEC61970.Dynamics.StandardModels.LoadDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * These load models (known also as generic non-linear dynamic (GNLD) load models)
 * can be used in mid-term and long-term voltage stability simulations (i.e., to
 * study voltage collapse), as they can replace a more detailed representation of
 * aggregate load, including induction motors, thermostatically controlled and
 * static loads.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class LoadGenericNonLinear extends LoadDynamics {

	/**
	 * Steady state voltage index for reactive power (BS).
	 */
	public Float bs;
	/**
	 * Transient voltage index for reactive power (BT).
	 */
	public Float bt;
	/**
	 * Type of generic non-linear load model.
	 */
	public GenericNonLinearLoadModelKind genericNonLinearLoadModelType;
	/**
	 * Steady state voltage index for active power (LS).
	 */
	public Float ls;
	/**
	 * Transient voltage index for active power (LT).
	 */
	public Float lt;
	/**
	 * Dynamic portion of active load (P<sub>T</sub>).
	 */
	public Float pt;
	/**
	 * Dynamic portion of reactive load (Q<sub>T</sub>).
	 */
	public Float qt;
	/**
	 * Time constant of lag function of active power (T<sub>P</sub>).
	 */
	public Seconds tp;
	/**
	 * Time constant of lag function of reactive power (T<sub>Q</sub>).
	 */
	public Seconds tq;

	public LoadGenericNonLinear(){

	}
}//end LoadGenericNonLinear