package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Pitch control power model.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.5.1.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindPitchContPowerIEC extends IdentifiedObject {

	/**
	 * Rate limit for increasing power (d<i>p</i><sub>max</sub>). It is type dependent
	 * parameter.
	 */
	public PU dpmax;
	/**
	 * Rate limit for decreasing power (d<i>p</i><sub>min</sub>). It is type dependent
	 * parameter.
	 */
	public PU dpmin;
	/**
	 * Minimum power setting (<i>p</i><sub>min</sub>). It is type dependent parameter.
	 */
	public PU pmin;
	/**
	 * If <i>p</i><sub>init </sub>< <i>p</i><sub>set </sub>then power will ne ramped
	 * down to <i>p</i><sub>min</sub>. It is (<i>p</i><sub>set</sub>) in the IEC 61400-
	 * 27-1. It is type dependent parameter.
	 */
	public PU pset;
	/**
	 * Lag time constant (<i>T</i><sub>1</sub>). It is type dependent parameter.
	 */
	public Seconds t1;
	/**
	 * Voltage measurement time constant (<i>T</i><sub>r</sub>). It is type dependent
	 * parameter.
	 */
	public Seconds tr;
	/**
	 * Dip detection threshold (u<sub>UVRT</sub>). It is type dependent parameter.
	 */
	public PU uuvrt;
	/**
	 * Wind turbine type 2 model with which this Pitch control power model is
	 * associated.
	 */
	public WindGenTurbineType2IEC WindGenTurbineType2IEC;

	public WindPitchContPowerIEC(){

	}
}//end WindPitchContPowerIEC