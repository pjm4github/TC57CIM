package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Temperature;
import IEC61970.Base.Domain.Seconds;

/**
 * Generic turbogas with acceleration and temperature controller.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovGAST3 extends TurbineGovernorDynamics {

	/**
	 * Acceleration limit set-point (Bca).  Unit = 1/s.  Typical Value = 0.01.
	 */
	public Float bca;
	/**
	 * Droop (bp).  Typical Value = 0.05.
	 */
	public PU bp;
	/**
	 * Exhaust temperature variation due to fuel flow increasing from 0 to 1 PU
	 * (deltaTc).  Typical Value = 390.
	 */
	public Temperature dtc;
	/**
	 * Minimum fuel flow (Ka).  Typical Value = 0.23.
	 */
	public PU ka;
	/**
	 * Fuel system feedback (K<sub>AC</sub>).  Typical Value = 0.
	 */
	public Float kac;
	/**
	 * Acceleration control integral gain (Kca). Unit = 1/s.  Typical Value = 100.
	 */
	public Float kca;
	/**
	 * Gain of radiation shield (Ksi).  Typical Value = 0.8.
	 */
	public Float ksi;
	/**
	 * Coefficient of transfer function of fuel valve positioner (Ky).  Typical Value
	 * = 1.
	 */
	public Float ky;
	/**
	 * Fuel flow maximum negative error value (MN<sub>EF</sub>).  Typical Value = -0.
	 * 05.
	 */
	public PU mnef;
	/**
	 * Fuel flow maximum positive error value (MX<sub>EF</sub>).  Typical Value = 0.05.
	 */
	public PU mxef;
	/**
	 * Minimum fuel flow (RCMN).  Typical Value = -0.1.
	 */
	public PU rcmn;
	/**
	 * Maximum fuel flow (RCMX).  Typical Value = 1.
	 */
	public PU rcmx;
	/**
	 * Fuel control time constant (Tac).  Typical Value = 0.1.
	 */
	public Seconds tac;
	/**
	 * Compressor discharge volume time constant (Tc).  Typical Value = 0.2.
	 */
	public Seconds tc;
	/**
	 * Temperature controller derivative gain (Td).  Typical Value = 3.3.
	 */
	public Seconds td;
	/**
	 * Turbine rated exhaust temperature correspondent to Pm=1 PU (Tfen).  Typical
	 * Value = 540.
	 */
	public Temperature tfen;
	/**
	 * Time constant of speed governor (Tg).  Typical Value = 0.05.
	 */
	public Seconds tg;
	/**
	 * Time constant of radiation shield (Tsi).  Typical Value = 15.
	 */
	public Seconds tsi;
	/**
	 * Temperature controller integration rate (Tt).  Typical Value = 250.
	 */
	public Temperature tt;
	/**
	 * Time constant of thermocouple (Ttc).  Typical Value = 2.5.
	 */
	public Seconds ttc;
	/**
	 * Time constant of fuel valve positioner (Ty).  Typical Value = 0.2.
	 */
	public Seconds ty;

	public GovGAST3(){

	}
}//end GovGAST3