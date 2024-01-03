package IEC61970.Base.Generation.Production;

import IEC61970.Base.Core.Curve;

/**
 * Relationship between unit efficiency in percent and unit output active power
 * for a given net head in meters. The relationship between efficiency, discharge,
 * head, and power output is expressed as follows:   E =KP/HQ
 * Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)
 * (K=constant)
 * For example, a curve instance for a given net head could relate efficiency (Y-
 * axis) versus active power output (X-axis) or versus discharge on the X-axis.
 * @created 02-Jan-2024 10:55:02 PM
 */
public class HydroGeneratingEfficiencyCurve extends Curve {

	public HydroGeneratingEfficiencyCurve(){

	}
}//end HydroGeneratingEfficiencyCurve