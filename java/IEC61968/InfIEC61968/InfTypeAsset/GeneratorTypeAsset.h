///////////////////////////////////////////////////////////
//  GeneratorTypeAsset.h
//  Implementation of the Class GeneratorTypeAsset
//  Created on:      25-Dec-2023 8:45:22 PM
///////////////////////////////////////////////////////////

#if !defined(EA_E871C68A_EEBB_4136_A2E6_7C757EDCB81C__INCLUDED_)
#define EA_E871C68A_EEBB_4136_A2E6_7C757EDCB81C__INCLUDED_

#include "ActivePower.h"
#include "ReactivePower.py"
#include "Resistance.py"
#include "Reactance.py"
#include "CatalogAssetType.h"

/**
 * Generic generation equipment that may be used for various purposes such as work
 * planning. It defines both the Real and Reactive power properties (modelled at
 * the PSR level as a GeneratingUnit + SynchronousMachine).
 */
class GeneratorTypeAsset : public CatalogAssetType
{

public:
	GeneratorTypeAsset();
	/**
	 * Maximum real power limit.
	 */
	ActivePower maxP;
	/**
	 * Maximum reactive power limit.
	 */
	ReactivePower maxQ;
	/**
	 * Minimum real power generated.
	 */
	ActivePower minP;
	/**
	 * Minimum reactive power generated.
	 */
	ReactivePower minQ;
	/**
	 * Direct-axis subtransient resistance.
	 */
	Resistance rDirectSubtrans;
	/**
	 * Direct-axis synchronous resistance.
	 */
	Resistance rDirectSync;
	/**
	 * Direct-axis transient resistance.
	 */
	Resistance rDirectTrans;
	/**
	 * Quadrature-axis subtransient resistance.
	 */
	Resistance rQuadSubtrans;
	/**
	 * Quadrature-axis synchronous resistance.
	 */
	Resistance rQuadSync;
	/**
	 * Quadrature-axis transient resistance.
	 */
	Resistance rQuadTrans;
	/**
	 * Direct-axis subtransient reactance.
	 */
	Reactance xDirectSubtrans;
	/**
	 * Direct-axis synchronous reactance.
	 */
	Reactance xDirectSync;
	/**
	 * Direct-axis transient reactance.
	 */
	Reactance xDirectTrans;
	/**
	 * Quadrature-axis subtransient reactance.
	 */
	Reactance xQuadSubtrans;
	/**
	 * Quadrature-axis synchronous reactance.
	 */
	Reactance xQuadSync;
	/**
	 * Quadrature-axis transient reactance.
	 */
	Reactance xQuadTrans;

};
#endif // !defined(EA_E871C68A_EEBB_4136_A2E6_7C757EDCB81C__INCLUDED_)
