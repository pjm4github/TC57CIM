package IEC61970.Base.Generation.Production;

import IEC61970.Base.Core.Curve;

/**
 * Relationship between the generating unit's gross active power output on the X-
 * axis (measured at the terminals of the machine(s)) and the generating unit's
 * net active power output on the Y-axis (based on utility-defined measurements at
 * the power station). Station service loads, when modeled, should be treated as
 * non-conforming bus loads. There may be more than one curve, depending on the
 * auxiliary equipment that is in service.
 * @created 02-Jan-2024 10:54:15 PM
 */
public class GrossToNetActivePowerCurve extends Curve {

	public GrossToNetActivePowerCurve(){

	}
}//end GrossToNetActivePowerCurve