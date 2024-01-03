package IEC61970.Base.Generation.GenerationTrainingSimulation;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Float;

/**
 * Steam turbine.
 * @created 02-Jan-2024 11:06:43 PM
 */
public class SteamTurbine extends PrimeMover {

	/**
	 * Crossover time constant.
	 */
	public Seconds crossoverTC;
	/**
	 * First reheater time constant.
	 */
	public Seconds reheater1TC;
	/**
	 * Second reheater time constant.
	 */
	public Seconds reheater2TC;
	/**
	 * Fraction of power from shaft 1 high pressure turbine output.
	 */
	public Float shaft1PowerHP;
	/**
	 * Fraction of power from shaft 1 intermediate pressure turbine output.
	 */
	public Float shaft1PowerIP;
	/**
	 * Fraction of power from shaft 1 first low pressure turbine output.
	 */
	public Float shaft1PowerLP1;
	/**
	 * Fraction of power from shaft 1 second low pressure turbine output.
	 */
	public Float shaft1PowerLP2;
	/**
	 * Fraction of power from shaft 2 high pressure turbine output.
	 */
	public Float shaft2PowerHP;
	/**
	 * Fraction of power from shaft 2 intermediate pressure turbine output.
	 */
	public Float shaft2PowerIP;
	/**
	 * Fraction of power from shaft 2 first low pressure turbine output.
	 */
	public Float shaft2PowerLP1;
	/**
	 * Fraction of power from shaft 2 second low pressure turbine output.
	 */
	public Float shaft2PowerLP2;
	/**
	 * Steam chest time constant.
	 */
	public Seconds steamChestTC;

	public SteamTurbine(){

	}
}//end SteamTurbine