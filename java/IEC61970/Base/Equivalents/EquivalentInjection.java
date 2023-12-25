package TC57CIM.IEC61970.Base.Equivalents;

import TC57CIM.IEC61970.Base.Domain.ActivePower;
import TC57CIM.IEC61970.Base.Domain.ReactivePower;
import TC57CIM.IEC61970.Base.Domain.Resistance;
import TC57CIM.IEC61970.Base.Domain.Boolean;
import TC57CIM.IEC61970.Base.Domain.Voltage;
import TC57CIM.IEC61970.Base.Domain.Reactance;

/**
 * This class represents equivalent injections (generation or load).  Voltage
 * regulation is allowed only at the point of connection.
 * @author KLH
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class EquivalentInjection extends EquivalentEquipment {

	/**
	 * Maximum active power of the injection.
	 */
	public ActivePower maxP;
	/**
	 * Used for modeling of infeed for load flow exchange. Not used for short circuit
	 * modeling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used.   
	 */
	public ReactivePower maxQ;
	/**
	 * Minimum active power of the injection.
	 */
	public ActivePower minP;
	/**
	 * Used for modeling of infeed for load flow exchange. Not used for short circuit
	 * modeling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used.
	 */
	public ReactivePower minQ;
	/**
	 * Equivalent active power injection. Load sign convention is used, i.e. positive
	 * sign means flow out from a node.
	 * Starting value for steady state solutions.
	 */
	public ActivePower p;
	/**
	 * Equivalent reactive power injection. Load sign convention is used, i.e.
	 * positive sign means flow out from a node.
	 * Starting value for steady state solutions.
	 */
	public ReactivePower q;
	/**
	 * Positive sequence resistance. Used to represent Extended-Ward (IEC 60909).
	 * Usage : Extended-Ward is a result of network reduction prior to the data
	 * exchange. 
	 */
	public Resistance r;
	/**
	 * Zero sequence resistance. Used to represent Extended-Ward (IEC 60909).
	 * Usage : Extended-Ward is a result of network reduction prior to the data
	 * exchange. 
	 */
	public Resistance r0;
	/**
	 * Negative sequence resistance. Used to represent Extended-Ward (IEC 60909).
	 * Usage : Extended-Ward is a result of network reduction prior to the data
	 * exchange. 
	 */
	public Resistance r2;
	/**
	 * Specifies whether or not the EquivalentInjection has the capability to regulate
	 * the local voltage.
	 */
	public Boolean regulationCapability;
	/**
	 * Specifies the default regulation status of the EquivalentInjection.  True is
	 * regulating.  False is not regulating.
	 */
	public Boolean regulationStatus;
	/**
	 * The target voltage for voltage regulation.
	 */
	public Voltage regulationTarget;
	/**
	 * Positive sequence reactance. Used to represent Extended-Ward (IEC 60909).
	 * Usage : Extended-Ward is a result of network reduction prior to the data
	 * exchange. 
	 */
	public Reactance x;
	/**
	 * Zero sequence reactance. Used to represent Extended-Ward (IEC 60909).
	 * Usage : Extended-Ward is a result of network reduction prior to the data
	 * exchange. 
	 */
	public Reactance x0;
	/**
	 * Negative sequence reactance. Used to represent Extended-Ward (IEC 60909).
	 * Usage : Extended-Ward is a result of network reduction prior to the data
	 * exchange. 
	 */
	public Reactance x2;

	public EquivalentInjection(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}