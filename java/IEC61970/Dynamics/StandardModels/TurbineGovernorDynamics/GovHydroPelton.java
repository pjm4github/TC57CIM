package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.Area;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.Length;
import IEC61970.Base.Domain.VolumeFlowRate;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Float;

/**
 * Detailed hydro unit - Pelton model.  This model can be used to represent the
 * dynamic related to water tunnel and surge chamber.
 * A schematic of the hydraulic system of detailed hydro unit models, like Francis
 * and Pelton, is located under the GovHydroFrancis class.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovHydroPelton extends TurbineGovernorDynamics {

	/**
	 * Area of the surge tank (A<sub>V0</sub>). Unit = m<sup>2</sup>. Typical Value =
	 * 30.
	 */
	public Area av0;
	/**
	 * Area of the compensation tank (A<sub>V1</sub>). Unit = m<sup>2</sup>. Typical
	 * Value = 700.
	 */
	public Area av1;
	/**
	 * Droop (bp).  Typical Value = 0.05.
	 */
	public PU bp;
	/**
	 * Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency db1;
	/**
	 * Intentional dead-band width of valve opening error (DB2). Unit = Hz.  Typical
	 * Value = 0.01.
	 */
	public Frequency db2;
	/**
	 * Head of compensation chamber water level with respect to the level of penstock
	 * (H<sub>1</sub>).  Unit = m. Typical Value = 4.
	 */
	public Length h1;
	/**
	 * Head of surge tank water level with respect to the level of penstock
	 * (H<sub>2</sub>).  Unit = m. Typical Value = 40.
	 */
	public Length h2;
	/**
	 * Rated hydraulic head (H<sub>n</sub>).  Unit = m. Typical Value = 250.
	 */
	public Length hn;
	/**
	 * Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025.
	 */
	public PU kc;
	/**
	 * Water tunnel and surge chamber loss coefficient (due to friction) (Kg).
	 * Typical Value = -0.025.
	 */
	public PU kg;
	/**
	 * No-load turbine flow at nominal head (Qc0).  Typical Value = 0.05.
	 */
	public PU qc0;
	/**
	 * Rated flow (Q<sub>n</sub>). Unit = m<sup>3</sup>/s. Typical Value = 40.
	 */
	public VolumeFlowRate qn;
	/**
	 * Simplified Pelton model simulation (Sflag).
	 * true = enable of simplified Pelton model simulation
	 * false = enable of complete Pelton model simulation (non linear gain).
	 * Typical Value = false.
	 */
	public Boolean simplifiedPelton;
	/**
	 * Static compensating characteristic (Cflag).
	 * true = enable of static compensating characteristic
	 * false = inhibit of static compensating characteristic.
	 * Typical Value = false.
	 */
	public Boolean staticCompensating;
	/**
	 * Derivative gain (accelerometer time constant) (Ta).  Typical Value = 3.
	 */
	public Seconds ta;
	/**
	 * Gate servo time constant (Ts).  Typical Value = 0.15.
	 */
	public Seconds ts;
	/**
	 * Servomotor integrator time constant (TV).  Typical Value = 0.3.
	 */
	public Seconds tv;
	/**
	 * Water inertia time constant (Twnc).  Typical Value = 1.
	 */
	public Seconds twnc;
	/**
	 * Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3.
	 */
	public Seconds twng;
	/**
	 * Electronic integrator time constant (Tx).  Typical Value = 0.5.
	 */
	public Seconds tx;
	/**
	 * Maximum gate opening velocity (Va).  Unit = PU/sec.  Typical Value = 0.016.
	 */
	public Float va;
	/**
	 * Maximum gate opening (ValvMax).  Typical Value = 1.
	 */
	public PU valvmax;
	/**
	 * Minimum gate opening (ValvMin).  Typical Value = 0.
	 */
	public PU valvmin;
	/**
	 * Maximum servomotor valve opening velocity (Vav).  Typical Value = 0.017.
	 */
	public PU vav;
	/**
	 * Maximum gate closing velocity (Vc).  Unit = PU/sec.  Typical Value = -0.016.
	 */
	public Float vc;
	/**
	 * Maximum servomotor valve closing velocity (Vcv).  Typical Value = -0.017.
	 */
	public PU vcv;
	/**
	 * Water tunnel and surge chamber simulation (Tflag).
	 * true = enable of water tunnel and surge chamber simulation
	 * false = inhibit of water tunnel and surge chamber simulation.
	 * Typical Value = false.
	 */
	public Boolean waterTunnelSurgeChamberSimulation;
	/**
	 * Head of upper water level with respect to the level of penstock (Zsfc).  Unit =
	 * m. Typical Value = 25.
	 */
	public Length zsfc;

	public GovHydroPelton(){

	}
}//end GovHydroPelton