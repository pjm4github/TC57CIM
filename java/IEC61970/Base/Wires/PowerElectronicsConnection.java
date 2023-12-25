package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.ReactivePower;
import TC57CIM.IEC61970.Base.Domain.ActivePower;
import TC57CIM.IEC61970.Base.Domain.Resistance;
import TC57CIM.IEC61970.Base.Domain.ApparentPower;
import TC57CIM.IEC61970.Base.Domain.Voltage;
import TC57CIM.IEC61970.Base.Domain.Reactance;
import TC57CIM.IEC61970.Base.Generation.Production.PowerElectronicsUnit;

/**
 * A connection to the AC network for energy production or consumption that uses
 * power electronics rather than rotating machines.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class PowerElectronicsConnection extends RegulatingCondEq {

	/**
	 * Maximum reactive power limit. This is the maximum (nameplate) limit for the
	 * unit.
	 */
	public ReactivePower maxQ;
	/**
	 * Minimum reactive power limit for the unit. This is the minimum (nameplate)
	 * limit for the unit.
	 */
	public ReactivePower minQ;
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
	 * Equivalent resistance (RG) of generator. RG is considered for the calculation
	 * of all currents, except for the calculation of the peak current ip. Used for
	 * short circuit data exchange according to IEC 60909.
	 */
	public Resistance r;
	/**
	 * Zero sequence resistance of the synchronous machine.
	 */
	public Resistance r0;
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
	 * Negative sequence Thevenin resistance.
	 */
	public Resistance rn;
	/**
	 * Positive sequence Thevenin reactance.
	 */
	public Reactance x;
	/**
	 * Zero sequence Thevenin reactance.
	 */
	public Reactance x0;
	/**
	 * Negative sequence Thevenin reactance.
	 */
	public Reactance xn;
	public PowerElectronicsUnit PowerElectronicsUnit;

	public PowerElectronicsConnection(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}