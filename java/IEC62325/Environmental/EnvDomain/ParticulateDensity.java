package IEC62325.Environmental.EnvDomain;

import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.UnitSymbol;
import IEC61970.Base.Domain.Float;

/**
 * Particulate density as kg/m<sup>3</sup>.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class ParticulateDensity {

	public static final UnitMultiplier multiplier = none;
	public static final UnitSymbol unit = kgPerm3;
	public Float value;

	public ParticulateDensity(){

	}
}//end ParticulateDensity