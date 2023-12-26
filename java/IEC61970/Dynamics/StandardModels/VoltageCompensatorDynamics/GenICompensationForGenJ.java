package IEC61970.Dynamics.StandardModels.VoltageCompensatorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.SynchronousMachineDynamics;

/**
 * This class provides the resistive and reactive components of compensation for
 * the generator associated with the IEEE Type 2 voltage compensator for current
 * flow out of one of the other generators in the interconnection.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GenICompensationForGenJ extends IdentifiedObject {

	/**
	 * <font color="#0f0f0f">Resistive component of compensation of generator
	 * associated with this IEEE Type 2 voltage compensator for current flow out of
	 * another generator (Rcij).</font>
	 */
	public PU rcij;
	/**
	 * <font color="#0f0f0f">Reactive component of compensation of generator
	 * associated with this IEEE Type 2 voltage compensator for current flow out of
	 * another generator (Xcij).</font>
	 */
	public PU xcij;
	/**
	 * The standard IEEE Type 2 voltage compensator of this compensation.
	 */
	public VCompIEEEType2 VcompIEEEType2;
	/**
	 * Standard synchronous machine out of which current flow is being compensated for.
	 */
	public SynchronousMachineDynamics SynchronousMachineDynamics;

	public GenICompensationForGenJ(){

	}
}//end GenICompensationForGenJ