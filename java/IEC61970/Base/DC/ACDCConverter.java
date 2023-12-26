package IEC61970.Base.DC;

import IEC61970.Base.Domain.ApparentPower;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.ReactivePower;
import IEC61970.Base.Domain.Resistance;
import IEC61970.Base.Domain.ActivePowerPerCurrentFlow;
import IEC61970.Base.Core.Terminal;
import IEC61970.Base.Core.ConductingEquipment;

/**
 * A unit with valves for three phases, together with unit control equipment,
 * essential protective and switching devices, DC storage capacitors, phase
 * reactors and auxiliaries, if any, used for conversion.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class ACDCConverter extends ConductingEquipment {

	/**
	 * Base apparent power of the converter pole.
	 */
	public ApparentPower baseS;
	/**
	 * Converter DC current, also called Id. Converter state variable, result from
	 * power flow.
	 */
	public CurrentFlow idc;
	/**
	 * Active power loss in pole at no power transfer. Converter configuration data
	 * used in power flow.
	 */
	public ActivePower idleLoss;
	/**
	 * The maximum voltage on the DC side at which the converter should operate.
	 * Converter configuration data used in power flow.
	 */
	public Voltage maxUdc;
	/**
	 * Min allowed converter DC voltage. Converter configuration data used in power
	 * flow.
	 */
	public Voltage minUdc;
	/**
	 * Number of valves in the converter. Used in loss calculations.
	 */
	public Integer numberOfValves;
	/**
	 * Active power at the point of common coupling. Load sign convention is used, i.e.
	 * positive sign means flow out from a node.
	 * Starting value for a steady state solution in the case a simplified power flow
	 * model is used.
	 */
	public ActivePower p;
	/**
	 * The active power loss at a DC Pole
	 * = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2
	 * For lossless operation Pdc=Pac
	 * For rectifier operation with losses Pdc=Pac-lossP
	 * For inverter operation with losses Pdc=Pac+lossP
	 * Converter state variable used in power flow.
	 */
	public ActivePower poleLossP;
	/**
	 * Reactive power at the point of common coupling. Load sign convention is used, i.
	 * e. positive sign means flow out from a node.
	 * Starting value for a steady state solution in the case a simplified power flow
	 * model is used.
	 */
	public ReactivePower q;
	/**
	 * Rated converter DC voltage, also called UdN. Converter configuration data used
	 * in power flow.
	 */
	public Voltage ratedUdc;
	/**
	 * Converter configuration data used in power flow. Refer to poleLossP.
	 */
	public Resistance resistiveLoss;
	/**
	 * Switching losses, relative to the base apparent power 'baseS'.
	 * Refer to poleLossP.
	 */
	public ActivePowerPerCurrentFlow switchingLoss;
	/**
	 * Real power injection target in AC grid, at point of common coupling.
	 */
	public ActivePower targetPpcc;
	/**
	 * Target value for DC voltage magnitude.
	 */
	public Voltage targetUdc;
	/**
	 * Line-to-line converter voltage, the voltage at the AC side of the valve.
	 * Converter state variable, result from power flow.
	 */
	public Voltage uc;
	/**
	 * Converter voltage at the DC side, also called Ud. Converter state variable,
	 * result from power flow.
	 */
	public Voltage udc;
	/**
	 * Valve threshold voltage, also called Uvalve. Forward voltage drop when the
	 * valve is conducting. Used in loss calculations, i.e. the switchLoss depend on
	 * numberOfValves * valveU0.
	 */
	public Voltage valveU0;
	/**
	 * Point of common coupling terminal for this converter DC side. It is typically
	 * the terminal on the power transformer (or switch) closest to the AC network.
	 * The power flow measurement must be the sum of all flows into the transformer.
	 */
	public Terminal PccTerminal;

	public ACDCConverter(){

	}
}//end ACDCConverter