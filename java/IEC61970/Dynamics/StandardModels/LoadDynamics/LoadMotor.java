package IEC61970.Dynamics.StandardModels.LoadDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Aggregate induction motor load. This model  is used to represent a fraction of
 * an ordinary load as "induction motor load".  It allows load that is treated as
 * ordinary constant power in power flow analysis to be represented by an
 * induction motor in dynamic simulation.  If <b>Lpp</b> = 0. or <b>Lpp</b> =
 * <b>Lp</b>, or <b>Tppo</b> = 0.,  only one cage is represented. Magnetic
 * saturation is not modelled. Either a "one-cage" or "two-cage" model of the
 * induction machine can be modelled. Magnetic saturation is not modelled.
 * 
 * This model is intended for representation of aggregations of many motors
 * dispersed through a load represented at a high voltage bus but where there is
 * no information on the characteristics of individual motors.
 * 
 * This model treats a fraction of the constant power part of a load as a motor.
 * During initialisation, the initial power drawn by the motor is set equal to
 * <b>Pfrac</b> times the constant <b>P</b> part of the static load.  The
 * remainder of the load is left as static load.
 * 
 * The reactive power demand of the motor is calculated during initialisation as a
 * function of voltage at the load bus. This reactive power demand may be less
 * than or greater than the constant <b>Q</b> component of the load.  If the
 * motor's reactive demand is greater than the constant <b>Q</b> component of the
 * load, the model inserts a shunt capacitor at the terminal of the motor to bring
 * its reactive demand down to equal the constant <b>Q</b> reactive load.
 * If a motor model and a static load model are both present for a load, the motor
 * <b>Pfrac</b> is assumed to be subtracted from the power flow constant <b>P</b>
 * load before the static load model is applied.  The remainder of the load, if
 * any, is then represented by the static load model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class LoadMotor extends IdentifiedObject {

	/**
	 * Damping factor (D).  Unit = delta P/delta speed.  Typical Value = 2.
	 */
	public Float d;
	/**
	 * Inertia constant (H) (not=0).  Typical Value = 0.4.
	 */
	public Seconds h;
	/**
	 * Loading factor - ratio of initial P to motor MVA base (Lfac).  Typical Value =
	 * 0.8.
	 */
	public Float lfac;
	/**
	 * Transient reactance (Lp).  Typical Value = 0.15.
	 */
	public PU lp;
	/**
	 * Subtransient reactance (Lpp).  Typical Value = 0.15.
	 */
	public PU lpp;
	/**
	 * Synchronous reactance (Ls).  Typical Value = 3.2.
	 */
	public PU ls;
	/**
	 * Fraction of constant-power load to be represented by this motor model (Pfrac)
	 * (>=0.0 and <=1.0).  Typical Value = 0.3.
	 */
	public Float pfrac;
	/**
	 * Stator resistance (Ra).  Typical Value = 0.
	 */
	public PU ra;
	/**
	 * Circuit breaker operating time (Tbkr).  Typical Value = 0.08.
	 */
	public Seconds tbkr;
	/**
	 * Transient rotor time constant (Tpo) (not=0).  Typical Value = 1.
	 */
	public Seconds tpo;
	/**
	 * Subtransient rotor time constant (Tppo).  Typical Value = 0.02.
	 */
	public Seconds tppo;
	/**
	 * Voltage trip pickup time (Tv).  Typical Value = 0.1.
	 */
	public Seconds tv;
	/**
	 * Voltage threshold for tripping (Vt).  Typical Value = 0.7.
	 */
	public PU vt;
	/**
	 * Aggregate load to which this aggregate motor (dynamic) load belongs.
	 */
	public LoadAggregate LoadAggregate;

	public LoadMotor(){

	}
}//end LoadMotor