package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Woodward Electric Hydro Governor Model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovHydroWEH extends TurbineGovernorDynamics {

	/**
	 * Speed Dead Band (db).
	 */
	public PU db;
	/**
	 * Value to allow the integral controller to advance beyond the gate limits (Dicn).
	 */
	public PU dicn;
	/**
	 * Value to allow the Pilot valve controller to advance beyond the gate limits
	 * (Dpv).
	 */
	public PU dpv;
	/**
	 * Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed
	 * (PU).
	 */
	public PU dturb;
	/**
	 * Feedback signal selection (Sw).
	 * true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0)
	 * false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or
	 * false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0).
	 */
	public Boolean feedbackSignal;
	/**
	 * Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table
	 * representing water flow through the turbine as a function of gate position to
	 * produce steady state flow.
	 */
	public PU fl1;
	/**
	 * Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table
	 * representing water flow through the turbine as a function of gate position to
	 * produce steady state flow.
	 */
	public PU fl2;
	/**
	 * Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table
	 * representing water flow through the turbine as a function of gate position to
	 * produce steady state flow.
	 */
	public PU fl3;
	/**
	 * Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table
	 * representing water flow through the turbine as a function of gate position to
	 * produce steady state flow.
	 */
	public PU fl4;
	/**
	 * Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table
	 * representing water flow through the turbine as a function of gate position to
	 * produce steady state flow.
	 */
	public PU fl5;
	/**
	 * Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing
	 * per unit mechanical power on machine MVA rating as a function of turbine flow.
	 */
	public PU fp1;
	/**
	 * Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing
	 * per unit mechanical power on machine MVA rating as a function of turbine flow.
	 */
	public PU fp10;
	/**
	 * Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing
	 * per unit mechanical power on machine MVA rating as a function of turbine flow.
	 */
	public PU fp2;
	/**
	 * Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing
	 * per unit mechanical power on machine MVA rating as a function of turbine flow.
	 */
	public PU fp3;
	/**
	 * Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing
	 * per unit mechanical power on machine MVA rating as a function of turbine flow.
	 */
	public PU fp4;
	/**
	 * Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing
	 * per unit mechanical power on machine MVA rating as a function of turbine flow.
	 */
	public PU fp5;
	/**
	 * Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing
	 * per unit mechanical power on machine MVA rating as a function of turbine flow.
	 */
	public PU fp6;
	/**
	 * Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing
	 * per unit mechanical power on machine MVA rating as a function of turbine flow.
	 */
	public PU fp7;
	/**
	 * Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing
	 * per unit mechanical power on machine MVA rating as a function of turbine flow.
	 */
	public PU fp8;
	/**
	 * Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing
	 * per unit mechanical power on machine MVA rating as a function of turbine flow.
	 */
	public PU fp9;
	/**
	 * Maximum Gate Position (Gmax).
	 */
	public PU gmax;
	/**
	 * Minimum Gate Position (Gmin).
	 */
	public PU gmin;
	/**
	 * Maximum gate closing rate (Gtmxcl).
	 */
	public PU gtmxcl;
	/**
	 * Maximum gate opening rate (Gtmxop).
	 */
	public PU gtmxop;
	/**
	 * Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing
	 * water flow through the turbine as a function of gate position to produce steady
	 * state flow.
	 */
	public PU gv1;
	/**
	 * Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing
	 * water flow through the turbine as a function of gate position to produce steady
	 * state flow.
	 */
	public PU gv2;
	/**
	 * Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing
	 * water flow through the turbine as a function of gate position to produce steady
	 * state flow.
	 */
	public PU gv3;
	/**
	 * Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing
	 * water flow through the turbine as a function of gate position to produce steady
	 * state flow.
	 */
	public PU gv4;
	/**
	 * Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing
	 * water flow through the turbine as a function of gate position to produce steady
	 * state flow.
	 */
	public PU gv5;
	/**
	 * Derivative controller derivative gain (Kd).
	 */
	public PU kd;
	/**
	 * Derivative controller Integral gain (Ki).
	 */
	public PU ki;
	/**
	 * Derivative control gain (Kp).
	 */
	public PU kp;
	/**
	 * Base for power values (MWbase) (>0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1
	 * for lookup table representing per unit mechanical power on machine MVA rating
	 * as a function of turbine flow.
	 */
	public PU pmss1;
	/**
	 * Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10
	 * for lookup table representing per unit mechanical power on machine MVA rating
	 * as a function of turbine flow.
	 */
	public PU pmss10;
	/**
	 * Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2
	 * for lookup table representing per unit mechanical power on machine MVA rating
	 * as a function of turbine flow.
	 */
	public PU pmss2;
	/**
	 * Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3
	 * for lookup table representing per unit mechanical power on machine MVA rating
	 * as a function of turbine flow.
	 */
	public PU pmss3;
	/**
	 * Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4
	 * for lookup table representing per unit mechanical power on machine MVA rating
	 * as a function of turbine flow.
	 */
	public PU pmss4;
	/**
	 * Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5
	 * for lookup table representing per unit mechanical power on machine MVA rating
	 * as a function of turbine flow.
	 */
	public PU pmss5;
	/**
	 * Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6
	 * for lookup table representing per unit mechanical power on machine MVA rating
	 * as a function of turbine flow.
	 */
	public PU pmss6;
	/**
	 * Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7
	 * for lookup table representing per unit mechanical power on machine MVA rating
	 * as a function of turbine flow.
	 */
	public PU pmss7;
	/**
	 * Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8
	 * for lookup table representing per unit mechanical power on machine MVA rating
	 * as a function of turbine flow.
	 */
	public PU pmss8;
	/**
	 * Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9
	 * for lookup table representing per unit mechanical power on machine MVA rating
	 * as a function of turbine flow.
	 */
	public PU pmss9;
	/**
	 * Permanent droop for governor output feedback (R-Perm-Gate).
	 */
	public Float rpg;
	/**
	 * Permanent droop for electrical power feedback (R-Perm-Pe).
	 */
	public Float rpp;
	/**
	 * Derivative controller time constant to limit the derivative characteristic
	 * beyond a breakdown frequency to avoid amplification of high-frequency noise
	 * (Td).
	 */
	public Seconds td;
	/**
	 * Distributive Valve time lag time constant (Tdv).
	 */
	public Seconds tdv;
	/**
	 * Value to allow the Distribution valve controller to advance beyond the gate
	 * movement rate limit (Tg).
	 */
	public Seconds tg;
	/**
	 * Pilot Valve time lag time constant (Tp).
	 */
	public Seconds tp;
	/**
	 * Electrical power droop time constant (Tpe).
	 */
	public Seconds tpe;
	/**
	 * Water inertia time constant (Tw) (>0).
	 */
	public Seconds tw;

	public GovHydroWEH(){

	}
}//end GovHydroWEH