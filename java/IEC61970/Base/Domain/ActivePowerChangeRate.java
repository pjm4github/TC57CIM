package IEC61970.Base.Domain;


/**
 * Rate of change of active power per time.
 * @created 30-Dec-2023 4:19:37 PM
 */
public class ActivePowerChangeRate {

	public UnitMultiplier multiplier;
	public static final UnitSymbol unit = WPers;
	public Float value;

	public ActivePowerChangeRate(){

	}
}//end ActivePowerChangeRate