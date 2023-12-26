package IEC61970.Dynamics.StandardModels.DiscontinuousExcitationControlDynamics;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PU;

/**
 * The class represents IEEE Type DEC3A model. In some systems, the stabilizer
 * output is disconnected from the regulator immediately following a severe fault
 * to prevent the stabilizer from competing with action of voltage regulator
 * during the first swing.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 12.4.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class DiscExcContIEEEDEC3A extends DiscontinuousExcitationControlDynamics {

	/**
	 * Reset time delay (<i>T</i><i><sub>DR</sub></i>). 
	 */
	public Seconds tdr;
	/**
	 * Terminal undervoltage comparison level (<i>V</i><i><sub>TMIN</sub></i>). 
	 */
	public PU vtmin;

	public DiscExcContIEEEDEC3A(){

	}
}//end DiscExcContIEEEDEC3A