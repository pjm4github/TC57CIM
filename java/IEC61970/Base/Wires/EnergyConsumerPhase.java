package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.ActivePower;
import TC57CIM.IEC61970.Base.Domain.PerCent;
import TC57CIM.IEC61970.Base.Domain.ReactivePower;
import TC57CIM.IEC61970.Base.Core.PowerSystemResource;

/**
 * A single phase of an energy consumer.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class EnergyConsumerPhase extends PowerSystemResource {

	/**
	 * Active power of the load. Load sign convention is used, i.e. positive sign
	 * means flow out from a node.
	 * For voltage dependent loads the value is at rated voltage.
	 * Starting value for a steady state solution.
	 */
	public ActivePower p;
	/**
	 * Active power of the load that is a fixed quantity. Load sign convention is used,
	 * i.e. positive sign means flow out from a node.
	 */
	public ActivePower pfixed;
	/**
	 * Fixed active power as per cent of load group fixed active power. Load sign
	 * convention is used, i.e. positive sign means flow out from a node.
	 */
	public PerCent pfixedPct;
	/**
	 * Phase of this energy consumer component.   If the energy consumer is wye
	 * connected, the connection is from the indicated phase to the central ground or
	 * neutral point.  If the energy consumer is delta connected, the phase indicates
	 * an energy consumer connected from the indicated phase to the next logical non-
	 * neutral phase.
	 */
	public SinglePhaseKind phase;
	/**
	 * Reactive power of the load. Load sign convention is used, i.e. positive sign
	 * means flow out from a node.
	 * For voltage dependent loads the value is at rated voltage.
	 * Starting value for a steady state solution.
	 */
	public ReactivePower q;
	/**
	 * Reactive power of the load that is a fixed quantity. Load sign convention is
	 * used, i.e. positive sign means flow out from a node.
	 */
	public ReactivePower qfixed;
	/**
	 * Fixed reactive power as per cent of load group fixed reactive power. Load sign
	 * convention is used, i.e. positive sign means flow out from a node.
	 */
	public PerCent qfixedPct;

	public EnergyConsumerPhase(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}