package IEC61970.Base.Equivalents;

import IEC61970.Base.Domain.Resistance;
import IEC61970.Base.Domain.Reactance;

/**
 * The class represents equivalent branches.
 * @created 02-Jan-2024 10:45:56 PM
 */
public class EquivalentBranch extends EquivalentEquipment {

	/**
	 * Negative sequence series resistance from terminal sequence  1 to terminal
	 * sequence 2. Used for short circuit data exchange according to IEC 60909
	 * EquivalentBranch is a result of network reduction prior to the data exchange 
	 */
	public Resistance negativeR12;
	/**
	 * Negative sequence series resistance from terminal sequence 2 to terminal
	 * sequence 1. Used for short circuit data exchange according to IEC 60909
	 * EquivalentBranch is a result of network reduction prior to the data exchange
	 */
	public Resistance negativeR21;
	/**
	 * Negative sequence series reactance from terminal sequence  1 to terminal
	 * sequence 2. Used for short circuit data exchange according to IEC 60909
	 * Usage : EquivalentBranch is a result of network reduction prior to the data
	 * exchange
	 */
	public Reactance negativeX12;
	/**
	 * Negative sequence series reactance from terminal sequence 2 to terminal
	 * sequence 1. Used for short circuit data exchange according to IEC 60909.
	 * Usage: EquivalentBranch is a result of network reduction prior to the data
	 * exchange
	 */
	public Reactance negativeX21;
	/**
	 * Positive sequence series resistance from terminal sequence  1 to terminal
	 * sequence 2 . Used for short circuit data exchange according to IEC 60909.
	 * EquivalentBranch is a result of network reduction prior to the data exchange. 
	 */
	public Resistance positiveR12;
	/**
	 * Positive sequence series resistance from terminal sequence 2 to terminal
	 * sequence 1. Used for short circuit data exchange according to IEC 60909
	 * EquivalentBranch is a result of network reduction prior to the data exchange
	 */
	public Resistance positiveR21;
	/**
	 * Positive sequence series reactance from terminal sequence  1 to terminal
	 * sequence 2. Used for short circuit data exchange according to IEC 60909
	 * Usage : EquivalentBranch is a result of network reduction prior to the data
	 * exchange
	 */
	public Reactance positiveX12;
	/**
	 * Positive sequence series reactance from terminal sequence 2 to terminal
	 * sequence 1. Used for short circuit data exchange according to IEC 60909
	 * Usage : EquivalentBranch is a result of network reduction prior to the data
	 * exchange
	 */
	public Reactance positiveX21;
	/**
	 * Positive sequence series resistance of the reduced branch.
	 */
	public Resistance r;
	/**
	 * Resistance from terminal sequence 2 to terminal sequence 1 .Used for steady
	 * state power flow. This attribute is optional and represent unbalanced network
	 * such as off-nominal phase shifter. If only EquivalentBranch.r is given, then
	 * EquivalentBranch.r21 is assumed equal to EquivalentBranch.r.
	 * Usage rule : EquivalentBranch is a result of network reduction prior to the
	 * data exchange.
	 */
	public Resistance r21;
	/**
	 * Positive sequence series reactance of the reduced branch.
	 */
	public Reactance x;
	/**
	 * Reactance from terminal sequence 2 to terminal sequence 1 .Used for steady
	 * state power flow. This attribute is optional and represent unbalanced network
	 * such as off-nominal phase shifter. If only EquivalentBranch.x is given, then
	 * EquivalentBranch.x21 is assumed equal to EquivalentBranch.x.
	 * Usage rule : EquivalentBranch is a result of network reduction prior to the
	 * data exchange.
	 */
	public Reactance x21;
	/**
	 * Zero sequence series resistance from terminal sequence  1 to terminal sequence
	 * 2. Used for short circuit data exchange according to IEC 60909
	 * EquivalentBranch is a result of network reduction prior to the data exchange
	 */
	public Resistance zeroR12;
	/**
	 * Zero sequence series resistance from terminal sequence  2 to terminal sequence
	 * 1. Used for short circuit data exchange according to IEC 60909
	 * Usage : EquivalentBranch is a result of network reduction prior to the data
	 * exchange
	 */
	public Resistance zeroR21;
	/**
	 * Zero sequence series reactance from terminal sequence  1 to terminal sequence 2.
	 * Used for short circuit data exchange according to IEC 60909
	 * Usage : EquivalentBranch is a result of network reduction prior to the data
	 * exchange
	 */
	public Reactance zeroX12;
	/**
	 * Zero sequence series reactance from terminal sequence 2 to terminal sequence 1.
	 * Used for short circuit data exchange according to IEC 60909
	 * Usage : EquivalentBranch is a result of network reduction prior to the data
	 * exchange
	 */
	public Reactance zeroX21;

	public EquivalentBranch(){

	}
}//end EquivalentBranch