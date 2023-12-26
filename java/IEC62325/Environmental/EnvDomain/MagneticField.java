package IEC62325.Environmental.EnvDomain;

import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.UnitSymbol;
import IEC61970.Base.Domain.Float;

/**
 * Magnetic field in nanotesla.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class MagneticField {

	public static final UnitMultiplier multiplier = n;
	public static final UnitSymbol unit = T;
	public Float value;

	public MagneticField(){

	}
}//end MagneticField