package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Current limitation model.  The current limitation model combines the physical
 * limits and the control limits.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.5.8.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindContCurrLimIEC extends IdentifiedObject {

	/**
	 * Maximum continuous current at the wind turbine terminals
	 * (<i>i</i><sub>max</sub>). It is type dependent parameter.
	 */
	public PU imax;
	/**
	 * Maximum current during voltage dip at the wind turbine terminals
	 * (<i>i</i><sub>maxdip</sub>). It is project dependent parameter.
	 */
	public PU imaxdip;
	/**
	 * Partial derivative of reactive current limit (<i>K</i><sub>pqu</sub>). It is
	 * type dependent parameter.
	 */
	public PU kpqu;
	/**
	 * Limitation of type 3 stator current  (<i>M</i><sub>DFSLim</sub>):
	 * - false=0: total current limitation,
	 * - true=1: stator current limitation).
	 * 
	 * It is type dependent parameter.
	 */
	public Boolean mdfslim;
	/**
	 * Prioritisation of q control during UVRT (<i>M</i><sub>qpri</sub>):
	 * - true = 1: reactive power priority,
	 * - false = 0: active power priority.
	 * 
	 * It is project dependent parameter.
	 */
	public Boolean mqpri;
	/**
	 * Voltage measurement filter time constant (<i>T</i><sub>ufiltcl</sub>). It is
	 * type dependent parameter.
	 */
	public Seconds tufiltcl;
	/**
	 * Wind turbine voltage in the operation point where zero reactive current can be
	 * delivered (<i>u</i><sub>pqumax</sub>). It is type dependent parameter.
	 */
	public PU upqumax;
	/**
	 * Wind turbine type 3 or 4 model with which this wind control current limitation
	 * model is associated.
	 */
	public WindTurbineType3or4IEC WindTurbineType3or4IEC;

	public WindContCurrLimIEC(){

	}
}//end WindContCurrLimIEC