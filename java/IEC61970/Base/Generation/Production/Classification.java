package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.UnitSymbol;
import IEC61970.Base.Domain.Integer;

/**
 * Classification of level.  Specify as 1..n, with 1 being the most detailed,
 * highest priority, etc as described on the attribue using this data type.
 * @created 02-Jan-2024 10:51:39 PM
 */
public class Classification {

	public static final UnitMultiplier multiplier = none;
	public static final UnitSymbol unit = none;
	public Integer value;

	public Classification(){

	}
}//end Classification