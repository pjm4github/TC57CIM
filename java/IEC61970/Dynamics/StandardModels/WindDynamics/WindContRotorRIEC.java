package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Rotor resistance control model.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.5.3.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindContRotorRIEC extends IdentifiedObject {

	/**
	 * Integral gain in rotor resistance PI controller (<i>K</i><sub>Irr</sub>). It is
	 * type dependent parameter.
	 */
	public PU kirr;
	/**
	 * Filter gain for generator speed measurement (K<sub>omegafilt</sub>). It is type
	 * dependent parameter.
	 */
	public Float komegafilt;
	/**
	 * Filter gain for power measurement (<i>K</i><sub>pfilt</sub>). It is type
	 * dependent parameter.
	 */
	public Float kpfilt;
	/**
	 * Proportional gain in rotor resistance PI controller (<i>K</i><sub>Prr</sub>).
	 * It is type dependent parameter.
	 */
	public PU kprr;
	/**
	 * Maximum rotor resistance (<i>r</i><sub>max</sub>). It is type dependent
	 * parameter.
	 */
	public PU rmax;
	/**
	 * Minimum rotor resistance (<i>r</i><sub>min</sub>). It is type dependent
	 * parameter.
	 */
	public PU rmin;
	/**
	 * Filter time constant for generator speed measurement
	 * (<i>T</i><sub>omegafiltrr</sub>). It is type dependent parameter.
	 */
	public Seconds tomegafiltrr;
	/**
	 * Filter time constant for power measurement (<i>T</i><sub>pfiltrr</sub>). It is
	 * type dependent parameter.
	 */
	public Seconds tpfiltrr;
	/**
	 * Wind turbine type 2 model with whitch this wind control rotor resistance model
	 * is associated.
	 */
	public WindGenTurbineType2IEC WindGenTurbineType2IEC;

	public WindContRotorRIEC(){

	}
}//end WindContRotorRIEC