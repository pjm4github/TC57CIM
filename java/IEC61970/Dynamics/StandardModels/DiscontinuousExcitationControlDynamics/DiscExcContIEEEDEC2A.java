package IEC61970.Dynamics.StandardModels.DiscontinuousExcitationControlDynamics;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PU;

/**
 * The class represents IEEE Type DEC2A model for the discontinuous excitation
 * control. This system provides transient excitation boosting via an open-loop
 * control as initiated by a trigger signal generated remotely.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 12.3.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class DiscExcContIEEEDEC2A extends DiscontinuousExcitationControlDynamics {

	/**
	 * Discontinuous controller time constant (<i>T</i><i><sub>D1</sub></i>). 
	 */
	public Seconds td1;
	/**
	 * Discontinuous controller washout time constant (<i>T</i><i><sub>D2</sub></i>). 
	 */
	public Seconds td2;
	/**
	 * Limiter (<i>V</i><i><sub>DMAX</sub></i>). 
	 */
	public PU vdmax;
	/**
	 * Limiter (<i>V</i><i><sub>DMIN</sub></i>). 
	 */
	public PU vdmin;
	/**
	 * Discontinuous controller input reference (<i>V</i><i><sub>K</sub></i>). 
	 */
	public PU vk;

	public DiscExcContIEEEDEC2A(){

	}
}//end DiscExcContIEEEDEC2A