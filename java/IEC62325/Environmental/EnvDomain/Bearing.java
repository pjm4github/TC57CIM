package IEC62325.Environmental.EnvDomain;

import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.UnitSymbol;
import IEC61970.Base.Domain.Float;

/**
 * The bearing in degrees (with 360 degrees being True North).  Measured in
 * degrees clockwise from True North.  0 degrees indicates no direction being
 * given.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class Bearing {

	public static final UnitMultiplier multiplier = none;
	public static final UnitSymbol unit = deg;
	public Float value;

	public Bearing(){

	}
}//end Bearing