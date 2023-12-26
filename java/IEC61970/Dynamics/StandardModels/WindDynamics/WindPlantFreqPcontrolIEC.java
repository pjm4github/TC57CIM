package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Frequency and active power controller model.
 * 
 * Reference: IEC Standard 61400-27-1 Annex D.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindPlantFreqPcontrolIEC extends IdentifiedObject {

	/**
	 * Maximum ramp rate of <i>p</i><sub>WTref</sub> request from the plant controller
	 * to the wind turbines (<i>dp</i><sub>refmax</sub>). It is case dependent
	 * parameter.
	 */
	public PU dprefmax;
	/**
	 * Minimum (negative) ramp rate of <i>p</i><sub>WTref</sub> request from the plant
	 * controller to the wind turbines (<i>dp</i><sub>refmin</sub>). It is project
	 * dependent parameter.
	 */
	public PU dprefmin;
	/**
	 * Maximum positive ramp rate for wind plant power reference
	 * (<i>dp</i><sub>WPrefmax</sub>). It is project dependent parameter.
	 */
	public PU dpwprefmax;
	/**
	 * Maximum negative ramp rate for wind plant power reference
	 * (<i>dp</i><sub>WPrefmin</sub>). It is project dependent parameter.
	 */
	public PU dpwprefmin;
	/**
	 * Plant P controller integral gain (<i>K</i><sub>IWPp</sub>). It is project
	 * dependent parameter.
	 */
	public Float kiwpp;
	/**
	 * Maximum PI integrator term (<i>K</i><sub>IWPpmax</sub>). It is project
	 * dependent parameter.
	 */
	public PU kiwppmax;
	/**
	 * Minimum PI integrator term (<i>K</i><sub>IWPpmin</sub>). It is project
	 * dependent parameter.
	 */
	public PU kiwppmin;
	/**
	 * Plant P controller proportional gain (<i>K</i><sub>PWPp</sub>). It is project
	 * dependent parameter.
	 */
	public Float kpwpp;
	/**
	 * Power reference gain (<i>K</i><sub>WPpref</sub>). It is project dependent
	 * parameter.
	 */
	public PU kwppref;
	/**
	 * Maximum <i>p</i><sub>WTref</sub> request from the plant controller to the wind
	 * turbines (<i>p</i><sub>refmax</sub>). It is project dependent parameter.
	 */
	public PU prefmax;
	/**
	 * Minimum <i>p</i><sub>WTref</sub> request from the plant controller to the wind
	 * turbines (<i>p</i><sub>refmin</sub>). It is project dependent parameter.
	 */
	public PU prefmin;
	/**
	 * Lead time constant in reference value transfer function
	 * (<i>T</i><sub>pft</sub>). It is project dependent parameter.
	 */
	public Seconds tpft;
	/**
	 * Lag time constant in reference value transfer function (<i>T</i><sub>pfv</sub>).
	 * It is project dependent parameter.
	 */
	public Seconds tpfv;
	/**
	 * Filter time constant for frequency measurement (<i>T</i><sub>WPffiltp</sub>).
	 * It is project dependent parameter.
	 */
	public Seconds twpffiltp;
	/**
	 * Filter time constant for active power measurement (<i>T</i><sub>WPpfiltp</sub>).
	 * It is project dependent parameter.
	 */
	public Seconds twppfiltp;
	/**
	 * Wind plant model with which this wind plant frequency and active power control
	 * is associated.
	 */
	public WindPlantIEC WindPlantIEC;

	public WindPlantFreqPcontrolIEC(){

	}
}//end WindPlantFreqPcontrolIEC