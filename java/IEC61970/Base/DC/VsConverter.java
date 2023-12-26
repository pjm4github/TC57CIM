package IEC61970.Base.DC;

import IEC61970.Base.Domain.AngleDegrees;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Resistance;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.ReactivePower;
import IEC61970.Base.Domain.Voltage;

/**
 * DC side of the voltage source converter (VSC).
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class VsConverter extends ACDCConverter {

	/**
	 * Angle between uf and uc. Converter state variable used in power flow.
	 */
	public AngleDegrees delta;
	/**
	 * Droop constant; pu value is obtained as D [kV/MW] x Sb / Ubdc.
	 */
	public PU droop;
	/**
	 * Compensation constant. Used to compensate for voltage drop when controlling
	 * voltage at a distant bus.
	 */
	public Resistance droopCompensation;
	/**
	 * The max quotient between the AC converter voltage (Uc) and DC voltage (Ud). A
	 * factor typically less than 1. VSC configuration data used in power flow.
	 */
	public Float maxModulationIndex;
	/**
	 * The maximum current through a valve. This current limit is the basis for
	 * calculating the capability diagram. VSC  configuration data.
	 */
	public CurrentFlow maxValveCurrent;
	/**
	 * Kind of control of real power and/or DC voltage.
	 */
	public VsPpccControlKind pPccControl;
	public VsQpccControlKind qPccControl;
	/**
	 * Reactive power sharing factor among parallel converters on Uac control.
	 */
	public PerCent qShare;
	/**
	 * Reactive power injection target in AC grid, at point of common coupling.
	 */
	public ReactivePower targetQpcc;
	/**
	 * Voltage target in AC grid, at point of common coupling.
	 */
	public Voltage targetUpcc;
	/**
	 * Line-to-line voltage on the valve side of the converter transformer. Converter
	 * state variable, result from power flow.
	 */
	public Voltage uv;
	/**
	 * Capability curve of this converter.
	 */
	public VsCapabilityCurve CapabilityCurve;

	public VsConverter(){

	}
}//end VsConverter