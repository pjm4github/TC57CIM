package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.RotationSpeed;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Resistance;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Reactance;

/**
 * A rotating machine whose shaft rotates asynchronously with the electrical field.
 *  Also known as an induction machine with no external connection to the rotor
 * windings, e.g squirrel-cage induction machine.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class AsynchronousMachine extends RotatingMachine {

	/**
	 * Indicates the type of Asynchronous Machine (motor or generator).
	 */
	public AsynchronousMachineKind asynchronousMachineType;
	/**
	 * Indicates whether the machine is a converter fed drive. Used for short circuit
	 * data exchange according to IEC 60909
	 */
	public Boolean converterFedDrive;
	/**
	 * Efficiency of the asynchronous machine at nominal operation in percent.
	 * Indicator for converter drive motors. Used for short circuit data exchange
	 * according to IEC 60909
	 */
	public PerCent efficiency;
	/**
	 * Ratio of locked-rotor current to the rated current of the motor (Ia/Ir). Used
	 * for short circuit data exchange according to IEC 60909
	 */
	public Float iaIrRatio;
	/**
	 * Nameplate data indicates if the machine is 50 or 60 Hz.
	 */
	public Frequency nominalFrequency;
	/**
	 * Nameplate data.  Depends on the slip and number of pole pairs.
	 */
	public RotationSpeed nominalSpeed;
	/**
	 * Number of pole pairs of stator. Used for short circuit data exchange according
	 * to IEC 60909
	 */
	public Integer polePairNumber;
	/**
	 * Rated mechanical power (Pr in the IEC 60909-0). Used for short circuit data
	 * exchange according to IEC 60909.
	 */
	public ActivePower ratedMechanicalPower;
	/**
	 * Indicates for converter drive motors if the power can be reversible. Used for
	 * short circuit data exchange according to IEC 60909
	 */
	public Boolean reversible;
	/**
	 * Damper 1 winding resistance.
	 */
	public Resistance rr1;
	/**
	 * Damper 2 winding resistance.
	 */
	public Resistance rr2;
	/**
	 * Locked rotor ratio (R/X). Used for short circuit data exchange according to IEC
	 * 60909
	 */
	public Float rxLockedRotorRatio;
	/**
	 * Transient rotor time constant (greater than tppo).
	 */
	public Seconds tpo;
	/**
	 * Sub-transient rotor time constant (greater than 0).
	 */
	public Seconds tppo;
	/**
	 * Damper 1 winding leakage reactance.
	 */
	public Reactance xlr1;
	/**
	 * Damper 2 winding leakage reactance.
	 */
	public Reactance xlr2;
	/**
	 * Magnetizing reactance.
	 */
	public Reactance xm;
	/**
	 * Transient reactance (unsaturated) (greater than or equal to xpp).
	 */
	public Reactance xp;
	/**
	 * Sub-transient reactance (unsaturated) (greather than Xl).
	 */
	public Reactance xpp;
	/**
	 * Synchronous reactance (greather than xp).
	 */
	public Reactance xs;

	public AsynchronousMachine(){

	}
}//end AsynchronousMachine