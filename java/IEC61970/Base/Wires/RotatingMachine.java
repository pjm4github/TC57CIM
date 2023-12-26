package IEC61970.Base.Wires;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.ReactivePower;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.ApparentPower;
import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Generation.Production.HydroPump;

/**
 * A rotating machine which may be used as a generator or motor.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class RotatingMachine extends RegulatingCondEq {

	/**
	 * Active power injection. Load sign convention is used, i.e. positive sign means
	 * flow out from a node.
	 * Starting value for a steady state solution.
	 */
	public ActivePower p;
	/**
	 * Reactive power injection. Load sign convention is used, i.e. positive sign
	 * means flow out from a node.
	 * Starting value for a steady state solution.
	 */
	public ReactivePower q;
	/**
	 * Power factor (nameplate data). It is primarily used for short circuit data
	 * exchange according to IEC 60909.
	 */
	public Float ratedPowerFactor;
	/**
	 * Nameplate apparent power rating for the unit.
	 * The attribute shall have a positive value.
	 */
	public ApparentPower ratedS;
	/**
	 * Rated voltage (nameplate data, Ur in IEC 60909-0). It is primarily used for
	 * short circuit data exchange according to IEC 60909.
	 */
	public Voltage ratedU;
	/**
	 * The synchronous machine drives the turbine which moves the water from a low
	 * elevation to a higher elevation. The direction of machine rotation for pumping
	 * may or may not be the same as for generating.
	 */
	public HydroPump HydroPump;

	public RotatingMachine(){

	}
}//end RotatingMachine