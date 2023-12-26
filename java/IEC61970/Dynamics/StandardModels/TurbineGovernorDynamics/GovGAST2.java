package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Temperature;
import IEC61970.Base.Domain.Boolean;

/**
 * Gas turbine model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovGAST2 extends TurbineGovernorDynamics {

	/**
	 * Valve positioner (A).
	 */
	public Float a;
	/**
	 * Exhaust temperature Parameter (Af1).  Unit = per unit temperature.  Based on
	 * temperature in degrees C.
	 */
	public PU af1;
	/**
	 * Coefficient equal to 0.5(1-speed) (Af2).
	 */
	public PU af2;
	/**
	 * Valve positioner (B). 
	 */
	public Float b;
	/**
	 * (Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x
	 * Tr.  Unit = per unit temperature.  Based on temperature in degrees C.
	 */
	public PU bf1;
	/**
	 * Turbine Torque Coefficient K<sub>hhv</sub> (depends on heating value of fuel
	 * stream in combustion chamber) (Bf2).
	 */
	public PU bf2;
	/**
	 * Valve positioner (C). 
	 */
	public Float c;
	/**
	 * Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but
	 * no output.  Typically 0.23 x K<sub>hhv</sub> (23% fuel flow).
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
	 * Fuel system feedback (Kf).
	 */
	public PU kf;
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
	 * Temperature control (Tc).  Unit = øF or øC depending on constants Af1 and Bf1. 
	 */
	public Temperature tc;
	/**
	 * Compressor discharge time constant (Tcd).
	 */
	public Seconds tcd;
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
	 * Rated temperature (Tr).  Unit = øC depending on parameters Af1 and Bf1.
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
	/**
	 * Governor gain (1/droop) on turbine rating (W).
	 */
	public PU w;
	/**
	 * Governor lead time constant (X).
	 */
	public Seconds x;
	/**
	 * Governor lag time constant (Y) (>0).
	 */
	public Seconds y;
	/**
	 * Governor mode (Z).
	 * true = Droop
	 * false = ISO.
	 */
	public Boolean z;

	public GovGAST2(){

	}
}//end GovGAST2