package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Temperature;

/**
 * Woodward Gas turbine governor model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovGASTWD extends TurbineGovernorDynamics {

	/**
	 * Valve positioner (<i>A</i>).
	 */
	public Float a;
	/**
	 * Exhaust temperature Parameter (Af1).
	 */
	public PU af1;
	/**
	 * Coefficient equal to 0.5(1-speed) (Af2).
	 */
	public PU af2;
	/**
	 * Valve positioner (<i>B</i>). 
	 */
	public Float b;
	/**
	 * (Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x
	 * Tr.
	 */
	public PU bf1;
	/**
	 * Turbine Torque Coefficient K<sub>hhv</sub> (depends on heating value of fuel
	 * stream in combustion chamber) (Bf2).
	 */
	public PU bf2;
	/**
	 * Valve positioner (<i>C</i>). 
	 */
	public Float c;
	/**
	 * Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but
	 * no output.  Typically 0.23 x K<sub>hhv </sub>(23% fuel flow).
	 */
	public PU cf2;
	/**
	 * Combustion reaction time delay (Ecr).
	 */
	public Seconds ecr;
	/**
	 * Turbine and exhaust delay (Etd).
	 */
	public Seconds etd;
	/**
	 * Ratio of Fuel Adjustment (K3).
	 */
	public PU k3;
	/**
	 * Gain of radiation shield (K4).
	 */
	public PU k4;
	/**
	 * Gain of radiation shield (K5).
	 */
	public PU k5;
	/**
	 * Minimum fuel flow (K6). 
	 */
	public PU k6;
	/**
	 * Drop Governor Gain (Kd).
	 */
	public PU kd;
	/**
	 * (Kdroop).
	 */
	public PU kdroop;
	/**
	 * Fuel system feedback (Kf).
	 */
	public PU kf;
	/**
	 * Isochronous Governor Gain (Ki).
	 */
	public PU ki;
	/**
	 * PID Proportional gain (Kp).
	 */
	public PU kp;
	/**
	 * Base for power values (MWbase) (> 0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Fuel Control Time Constant (T).
	 */
	public Seconds t;
	/**
	 * Radiation shield time constant (T3).
	 */
	public Seconds t3;
	/**
	 * Thermocouple time constant (T4).
	 */
	public Seconds t4;
	/**
	 * Temperature control time constant (T5).
	 */
	public Seconds t5;
	/**
	 * Temperature control (Tc).
	 */
	public Temperature tc;
	/**
	 * Compressor discharge time constant (Tcd).
	 */
	public Seconds tcd;
	/**
	 * Power transducer time constant (Td).
	 */
	public Seconds td;
	/**
	 * Fuel system time constant (Tf).
	 */
	public Seconds tf;
	/**
	 * Maximum Turbine limit (Tmax).
	 */
	public PU tmax;
	/**
	 * Minimum Turbine limit (Tmin).
	 */
	public PU tmin;
	/**
	 * Rated temperature (Tr).
	 */
	public Temperature tr;
	/**
	 * Turbine rating (Trate).  Unit = MW.
	 */
	public ActivePower trate;
	/**
	 * Temperature controller integration rate (Tt).
	 */
	public Seconds tt;

	public GovGASTWD(){

	}
}//end GovGASTWD