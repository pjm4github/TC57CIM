package IEC61968.InfIEC61968.InfTypeAsset;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.ReactivePower;
import IEC61970.Base.Domain.Resistance;
import IEC61970.Base.Domain.Reactance;
import IEC61968.Assets.CatalogAssetType;

/**
 * Generic generation equipment that may be used for various purposes such as work
 * planning. It defines both the Real and Reactive power properties (modelled at
 * the PSR level as a GeneratingUnit + SynchronousMachine).
 * @created 02-Jan-2024 9:53:35 PM
 */
public class GeneratorTypeAsset extends CatalogAssetType {

	/**
	 * Maximum real power limit.
	 */
	public ActivePower maxP;
	/**
	 * Maximum reactive power limit.
	 */
	public ReactivePower maxQ;
	/**
	 * Minimum real power generated.
	 */
	public ActivePower minP;
	/**
	 * Minimum reactive power generated.
	 */
	public ReactivePower minQ;
	/**
	 * Direct-axis subtransient resistance.
	 */
	public Resistance rDirectSubtrans;
	/**
	 * Direct-axis synchronous resistance.
	 */
	public Resistance rDirectSync;
	/**
	 * Direct-axis transient resistance.
	 */
	public Resistance rDirectTrans;
	/**
	 * Quadrature-axis subtransient resistance.
	 */
	public Resistance rQuadSubtrans;
	/**
	 * Quadrature-axis synchronous resistance.
	 */
	public Resistance rQuadSync;
	/**
	 * Quadrature-axis transient resistance.
	 */
	public Resistance rQuadTrans;
	/**
	 * Direct-axis subtransient reactance.
	 */
	public Reactance xDirectSubtrans;
	/**
	 * Direct-axis synchronous reactance.
	 */
	public Reactance xDirectSync;
	/**
	 * Direct-axis transient reactance.
	 */
	public Reactance xDirectTrans;
	/**
	 * Quadrature-axis subtransient reactance.
	 */
	public Reactance xQuadSubtrans;
	/**
	 * Quadrature-axis synchronous reactance.
	 */
	public Reactance xQuadSync;
	/**
	 * Quadrature-axis transient reactance.
	 */
	public Reactance xQuadTrans;

	public GeneratorTypeAsset(){

	}
}//end GeneratorTypeAsset