package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.ActivePowerPerFrequency;
import TC57CIM.IEC61970.Base.Domain.Boolean;
import TC57CIM.IEC61970.Base.Domain.CurrentFlow;
import TC57CIM.IEC61970.Base.Domain.ActivePower;
import TC57CIM.IEC61970.Base.Domain.ReactivePower;
import TC57CIM.IEC61970.Base.Domain.Float;
import TC57CIM.IEC61970.Base.Domain.Integer;
import TC57CIM.IEC61970.Base.Domain.PU;

/**
 * This class represents external network and it is used for IEC 60909
 * calculations.
 * @author Jean-Luc
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class ExternalNetworkInjection extends RegulatingCondEq {

	/**
	 * Power Frequency Bias. This is the change in power injection divided by the
	 * change in frequency and negated.  A positive value of the power frequency bias
	 * provides additional power injection upon a drop in frequency.
	 */
	public ActivePowerPerFrequency governorSCD;
	/**
	 * Indicates whether initial symmetrical short-circuit current and power have been
	 * calculated according to IEC (Ik").
	 */
	public Boolean ikSecond;
	/**
	 *  Maximum initial symmetrical short-circuit currents (Ik" max) in A (Ik" =
	 * Sk"/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909
	 */
	public CurrentFlow maxInitialSymShCCurrent;
	/**
	 * Maximum active power of the injection.
	 */
	public ActivePower maxP;
	/**
	 * Not for short circuit modelling; It is used for modelling of infeed for load
	 * flow exchange. If maxQ and minQ are not used ReactiveCapabilityCurve can be
	 * used 
	 */
	public ReactivePower maxQ;
	/**
	 * Maximum ratio of zero sequence resistance of Network Feeder to its zero
	 * sequence reactance (R(0)/X(0) max). Used for short circuit data exchange
	 * according to IEC 60909
	 */
	public Float maxR0ToX0Ratio;
	/**
	 * Maximum ratio of positive sequence resistance of Network Feeder to its positive
	 * sequence reactance (R(1)/X(1) max). Used for short circuit data exchange
	 * according to IEC 60909
	 */
	public Float maxR1ToX1Ratio;
	/**
	 * Maximum ratio of zero sequence impedance to its positive sequence impedance
	 * (Z(0)/Z(1) max). Used for short circuit data exchange according to IEC 60909
	 */
	public Float maxZ0ToZ1Ratio;
	/**
	 * Minimum initial symmetrical short-circuit currents (Ik" min) in A (Ik" =
	 * Sk"/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909
	 */
	public CurrentFlow minInitialSymShCCurrent;
	/**
	 * Minimum active power of the injection.
	 */
	public ActivePower minP;
	/**
	 * Not for short circuit modelling; It is used for modelling of infeed for load
	 * flow exchange. If maxQ and minQ are not used ReactiveCapabilityCurve can be used
	 */
	public ReactivePower minQ;
	/**
	 * Indicates whether initial symmetrical short-circuit current and power have been
	 * calculated according to IEC (Ik"). Used for short circuit data exchange
	 * according to IEC 6090
	 */
	public Float minR0ToX0Ratio;
	/**
	 * Minimum ratio of positive sequence resistance of Network Feeder to its positive
	 * sequence reactance (R(1)/X(1) min). Used for short circuit data exchange
	 * according to IEC 60909
	 */
	public Float minR1ToX1Ratio;
	/**
	 * Minimum ratio of zero sequence impedance to its positive sequence impedance
	 * (Z(0)/Z(1) min). Used for short circuit data exchange according to IEC 60909
	 */
	public Float minZ0ToZ1Ratio;
	/**
	 * Active power injection. Load sign convention is used, i.e. positive sign means
	 * flow out from a node.
	 * Starting value for steady state solutions.
	 */
	public ActivePower p;
	/**
	 * Reactive power injection. Load sign convention is used, i.e. positive sign
	 * means flow out from a node.
	 * Starting value for steady state solutions.
	 */
	public ReactivePower q;
	/**
	 * Priority of unit for use as powerflow voltage phase angle reference bus
	 * selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and
	 * so on.
	 */
	public Integer referencePriority;
	/**
	 * Voltage factor in pu, which was used to calculate short-circuit current Ik" and
	 * power Sk".
	 */
	public PU voltageFactor;

	public ExternalNetworkInjection(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}