package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.AngleDegrees;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Pitch angle control model.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.5.2.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindContPitchAngleIEC extends IdentifiedObject {

	/**
	 * Maximum pitch positive ramp rate (d<i>theta</i><sub>max</sub>). It is type
	 * dependent parameter. Unit = degrees/sec. 
	 */
	public Float dthetamax;
	/**
	 * Maximum pitch negative ramp rate (d<i>theta</i><sub>min</sub>). It is type
	 * dependent parameter. Unit = degrees/sec. 
	 */
	public Float dthetamin;
	/**
	 * Power PI controller integration gain (<i>K</i><sub>Ic</sub>). It is type
	 * dependent parameter.
	 */
	public PU kic;
	/**
	 * Speed PI controller integration gain (<i>K</i><sub>Iomega</sub>). It is type
	 * dependent parameter.
	 */
	public PU kiomega;
	/**
	 * Power PI controller proportional gain (<i>K</i><sub>Pc</sub>). It is type
	 * dependent parameter.
	 */
	public PU kpc;
	/**
	 * Speed PI controller proportional gain (<i>K</i><sub>Pomega</sub>). It is type
	 * dependent parameter.
	 */
	public PU kpomega;
	/**
	 * Pitch cross coupling gain (K<sub>PX</sub>). It is type dependent parameter.
	 */
	public PU kpx;
	/**
	 * Maximum pitch angle (<i>theta</i><sub>max</sub>). It is type dependent
	 * parameter.
	 */
	public AngleDegrees thetamax;
	/**
	 * Minimum pitch angle (<i>theta</i><sub>min</sub>). It is type dependent
	 * parameter.
	 */
	public AngleDegrees thetamin;
	/**
	 * Pitch time constant (t<i>theta</i>). It is type dependent parameter.
	 */
	public Seconds ttheta;
	/**
	 * Wind turbine type 3 model with which this pitch control model is associated.
	 */
	public WindTurbineType3IEC WindTurbineType3IEC;

	public WindContPitchAngleIEC(){

	}
}//end WindContPitchAngleIEC