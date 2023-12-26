package IEC61970.Dynamics.StandardModels.VoltageCompensatorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * <font color="#0f0f0f">The class represents the terminal voltage transducer and
 * the load compensator as defined in the IEEE Std 421.5-2005, Section 4. This
 * model is common to all excitation system models described in the IEEE Standard.
 * </font>
 * 
 * Reference: IEEE Standard 421.5-2005 Section 4.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class VCompIEEEType1 extends VoltageCompensatorDynamics {

	/**
	 * <font color="#0f0f0f">Resistive component of compensation of a generator (Rc).
	 * </font>
	 */
	public PU rc;
	/**
	 * <font color="#0f0f0f">Time constant which is used for the combined voltage
	 * sensing and compensation signal (Tr).</font>
	 */
	public Seconds tr;
	/**
	 * <font color="#0f0f0f">Reactive component of compensation of a generator (Xc).
	 * </font>
	 */
	public PU xc;

	public VCompIEEEType1(){

	}
}//end VCompIEEEType1