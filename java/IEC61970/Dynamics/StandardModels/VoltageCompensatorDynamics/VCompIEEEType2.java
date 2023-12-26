package IEC61970.Dynamics.StandardModels.VoltageCompensatorDynamics;

import IEC61970.Base.Domain.Seconds;

/**
 * <font color="#0f0f0f">The class represents the terminal voltage transducer and
 * the load compensator as defined in the IEEE Std 421.5-2005, Section 4. This
 * model is designed to cover the following types of compensation: </font>
 * <ul>
 * 	<li><font color="#0f0f0f">reactive droop</font></li>
 * 	<li><font color="#0f0f0f">transformer-drop or line-drop
 * compensation</font></li>
 * 	<li><font color="#0f0f0f">reactive differential compensation known also as
 * cross-current compensation.</font></li>
 * </ul>
 * <font color="#0f0f0f">
 * </font><font color="#0f0f0f">Reference: IEEE Standard 421.5-2005, Section 4.
 * </font>
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class VCompIEEEType2 extends VoltageCompensatorDynamics {

	/**
	 * <font color="#0f0f0f">Time constant which is used for the combined voltage
	 * sensing and compensation signal (Tr).</font>
	 */
	public Seconds tr;

	public VCompIEEEType2(){

	}
}//end VCompIEEEType2