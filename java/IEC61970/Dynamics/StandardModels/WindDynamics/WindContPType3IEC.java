package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * P control model Type 3.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.5.4.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindContPType3IEC extends IdentifiedObject {

	/**
	 * Maximum wind turbine power ramp rate (<i>dp</i><sub>max</sub>). It is type
	 * dependent parameter.
	 */
	public PU dpmax;
	/**
	 * Maximum ramp rate of wind turbine reference power (d<i>p</i><sub>refmax</sub>).
	 * It is project dependent parameter.
	 */
	public PU dprefmax;
	/**
	 * Minimum ramp rate of wind turbine reference power (d<i>p</i><sub>refmin</sub>).
	 * It is project dependent parameter.
	 */
	public PU dprefmin;
	/**
	 * Ramp limitation of torque, required in some grid codes
	 * (d<i>t</i><sub>max</sub>). It is project dependent parameter.
	 */
	public PU dthetamax;
	/**
	 * Limitation of torque rise rate during UVRT (d<i>theta</i><sub>maxUVRT</sub>).
	 * It is project dependent parameter.
	 */
	public PU dthetamaxuvrt;
	/**
	 * Gain for active drive train damping (<i>K</i><sub>DTD</sub>). It is type
	 * dependent parameter.
	 */
	public PU kdtd;
	/**
	 * PI controller integration parameter (<i>K</i><sub>Ip</sub>). It is type
	 * dependent parameter.
	 */
	public PU kip;
	/**
	 * PI controller proportional gain (<i>K</i><sub>Pp</sub>). It is type dependent
	 * parameter.
	 */
	public PU kpp;
	/**
	 * Enable UVRT power control mode (M<sub>pUVRT).</sub>
	 * true = 1: voltage control
	 * false = 0: reactive power control.
	 * It is project dependent parameter.
	 */
	public Boolean mpuvrt;
	/**
	 * Offset to reference value that limits controller action during rotor speed
	 * changes (omega<sub>offset</sub>). It is case dependent parameter.
	 */
	public PU omegaoffset;
	/**
	 * Maximum active drive train damping power (<i>p</i><sub>DTDmax</sub>). It is
	 * type dependent parameter.
	 */
	public PU pdtdmax;
	/**
	 * Time<sub> </sub>delay after deep voltage sags (T<sub>DVS</sub>). It is project
	 * dependent parameter.
	 */
	public Seconds tdvs;
	/**
	 * Minimum electrical generator torque (<i>t</i><sub>emin</sub>). It is type
	 * dependent parameter.
	 */
	public PU thetaemin;
	/**
	 * Voltage scaling factor of reset-torque (<i>t</i><sub>uscale</sub>). It is
	 * project dependent parameter.
	 */
	public PU thetauscale;
	/**
	 * Filter time constant for generator speed measurement
	 * (<i>T</i><sub>omegafiltp3</sub>). It is type dependent parameter.
	 */
	public Seconds tomegafiltp3;
	/**
	 * Filter time constant for power measurement (<i>T</i><sub>pfiltp3</sub>). It is
	 * type dependent parameter.
	 */
	public Seconds tpfiltp3;
	/**
	 * Time constant in power order lag (<i>T</i><sub>pord</sub>). It is type
	 * dependent parameter.
	 */
	public PU tpord;
	/**
	 * Filter time constant for voltage measurement (<i>T</i><sub>ufiltp3</sub>). It
	 * is type dependent parameter.
	 */
	public Seconds tufiltp3;
	/**
	 * Time constant in speed reference filter (<i>T</i><sub>omega,ref</sub>). It is
	 * type dependent parameter.
	 */
	public Seconds twref;
	/**
	 * Voltage limit for hold UVRT status after deep voltage sags
	 * (<i>u</i><i><sub>DVS</sub></i>). It is project dependent parameter.
	 */
	public PU udvs;
	/**
	 * Voltage dip threshold for P-control (<i>u</i><sub>Pdip</sub>).  Part of turbine
	 * control, often different (e.g 0.8) from converter thresholds. It is project
	 * dependent parameter.
	 */
	public PU updip;
	/**
	 * Active drive train damping frequency (omega<sub>DTD</sub>). It can be
	 * calculated from two mass model parameters. It is type dependent parameter.
	 */
	public PU wdtd;
	/**
	 * Coefficient for active drive train damping (zeta). It is type dependent
	 * parameter.
	 */
	public Float zeta;
	/**
	 * Wind turbine type 3 model with which this Wind control P type 3 model is
	 * associated.
	 */
	public WindTurbineType3IEC WindTurbineType3IEC;

	public WindContPType3IEC(){

	}
}//end WindContPType3IEC