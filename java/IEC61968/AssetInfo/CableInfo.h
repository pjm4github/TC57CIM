///////////////////////////////////////////////////////////
//  CableInfo.h
//  Implementation of the Class CableInfo
//  Created on:      25-Dec-2023 8:45:19 PM
///////////////////////////////////////////////////////////

#if !defined(EA_B777E9AA_C960_4315_A46B_C04348BCAAE9__INCLUDED_)
#define EA_B777E9AA_C960_4315_A46B_C04348BCAAE9__INCLUDED_

#include "IEC61968\AssetInfo\CableConstructionKind.java"
#include "Length.py"
#include "Boolean.h"
#include "Temperature.py"
#include "IEC61968\AssetInfo\CableOuterJacketKind.java"
#include "IEC61968\AssetInfo\CableShieldMaterialKind.java"
#include "WireInfo.h"

/**
 * Cable data.
 */
class CableInfo : public WireInfo
{

public:
	CableInfo();
	/**
	 * Kind of construction of this cable.
	 */
	CableConstructionKind constructionKind;
	/**
	 * Diameter over the core, including any semi-con screen; should be the insulating
	 * layer's inside diameter.
	 */
	Length diameterOverCore;
	/**
	 * Diameter over the insulating layer, excluding outer screen.
	 */
	Length diameterOverInsulation;
	/**
	 * Diameter over the outermost jacketing layer.
	 */
	Length diameterOverJacket;
	/**
	 * Diameter over the outer screen; should be the shield's inside diameter.
	 */
	Length diameterOverScreen;
	/**
	 * True if wire strands are extruded in a way to fill the voids in the cable.
	 */
	Boolean isStrandFill;
	/**
	 * Maximum nominal design operating temperature.
	 */
	Temperature nominalTemperature;
	/**
	 * Kind of outer jacket of this cable.
	 */
	CableOuterJacketKind outerJacketKind;
	/**
	 * True if sheath / shield is used as a neutral (i.e., bonded).
	 */
	Boolean sheathAsNeutral;
	/**
	 * Material of the shield.
	 */
	CableShieldMaterialKind shieldMaterial;

};
#endif // !defined(EA_B777E9AA_C960_4315_A46B_C04348BCAAE9__INCLUDED_)
