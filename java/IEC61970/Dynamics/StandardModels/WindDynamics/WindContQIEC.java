package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Q control model.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.5.7.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindContQIEC extends IdentifiedObject {

	/**
	 * Maximum reactive current injection during dip (i<sub>qh1</sub>). It is type
	 * dependent parameter.
	 */
	public PU iqh1;
	/**
	 * Maximum reactive current injection (i<sub>qmax</sub>). It is type dependent
	 * parameter.
	 */
	public PU iqmax;
	/**
	 * Minimum reactive current injection (i<sub>qmin</sub>). It is type dependent
	 * parameter.
	 */
	public PU iqmin;
	/**
	 * Post fault reactive current injection (<i>i</i><sub>qpost</sub>). It is project
	 * dependent parameter.
	 */
	public PU iqpost;
	/**
	 * Reactive power PI controller integration gain (<i>K</i><sub>I,q</sub>). It is
	 * type dependent parameter.
	 */
	public PU kiq;
	/**
	 * Voltage PI controller integration gain (<i>K</i><sub>I,u</sub>). It is type
	 * dependent parameter.
	 */
	public PU kiu;
	/**
	 * Reactive power PI controller proportional gain (<i>K</i><sub>P,q</sub>). It is
	 * type dependent parameter.
	 */
	public PU kpq;
	/**
	 * Voltage PI controller proportional gain (<i>K</i><sub>P,u</sub>). It is type
	 * dependent parameter.
	 */
	public PU kpu;
	/**
	 * Voltage scaling factor for UVRT current (<i>K</i><sub>qv</sub>). It is project
	 * dependent parameter.
	 */
	public PU kqv;
	/**
	 * Resistive component of voltage drop impedance (<i>r</i><sub>droop</sub>). It is
	 * project dependent parameter.
	 */
	public PU rdroop;
	/**
	 * Power measurement filter time constant (<i>T</i><sub>pfiltq</sub>). It is type
	 * dependent parameter.
	 */
	public Seconds tpfiltq;
	/**
	 * Length of time period where post fault reactive power is injected
	 * (<i>T</i><sub>post</sub>). It is project dependent parameter.
	 */
	public Seconds tpost;
	/**
	 * Time constant in reactive power order lag (<i>T</i><sub>qord</sub>). It is type
	 * dependent parameter.
	 */
	public Seconds tqord;
	/**
	 * Voltage measurement filter time constant (<i>T</i><sub>ufiltq</sub>). It is
	 * type dependent parameter.
	 */
	public Seconds tufiltq;
	/**
	 * Voltage dead band lower limit (<i>u</i><sub>db1</sub>). It is type dependent
	 * parameter.
	 */
	public PU udb1;
	/**
	 * Voltage dead band upper limit (<i>u</i><sub>db2</sub>). It is type dependent
	 * parameter.
	 */
	public PU udb2;
	/**
	 * Maximum voltage in voltage PI controller integral term (u<sub>max</sub>). It is
	 * type dependent parameter.
	 */
	public PU umax;
	/**
	 * Minimum voltage in voltage PI controller integral term (u<sub>min</sub>). It is
	 * type dependent parameter.
	 */
	public PU umin;
	/**
	 * Voltage threshold for UVRT detection in q control (<i>u</i><sub>qdip</sub>). It
	 * is type dependent parameter.
	 */
	public PU uqdip;
	/**
	 * User defined bias in voltage reference (<i>u</i><sub>ref0</sub>), used when
	 * <i>M</i><sub>qG</sub> is set to voltage control. It is case dependent parameter.
	 */
	public PU uref0;
	/**
	 * Types of general wind turbine Q control modes (<i>M</i><sub>qG</sub>).  It is
	 * project dependent parameter.
	 */
	public WindQcontrolModeKind windQcontrolModesType;
	/**
	 * Types of UVRT Q control modes (<i>M</i><sub>qUVRT</sub>). It is project
	 * dependent parameter.
	 */
	public WindUVRTQcontrolModeKind windUVRTQcontrolModesType;
	/**
	 * Inductive component of voltage drop impedance (<i>x</i><sub>droop</sub>). It is
	 * project dependent parameter.
	 */
	public PU xdroop;
	/**
	 * Wind turbine type 3 or 4 model with which this reactive control model is
	 * associated.
	 */
	public WindTurbineType3or4IEC WindTurbineType3or4IEC;

	public WindContQIEC(){

	}
}//end WindContQIEC