package IEC61970.Base.Domain;


/**
 * Reservoir water level referred to a given datum such as mean sea level.
 * @created 30-Dec-2023 4:19:38 PM
 */
public class WaterLevel {

	public UnitMultiplier multiplier;
	public static final UnitSymbol unit = m;
	public Float value;

	public WaterLevel(){

	}
}//end WaterLevel