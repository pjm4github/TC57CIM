///////////////////////////////////////////////////////////
//  WireInfo.h
//  Implementation of the Class WireInfo
//  Created on:      25-Dec-2023 8:45:26 PM
///////////////////////////////////////////////////////////

#if !defined(EA_61C909B7_E8C2_4f65_85DB_E31D73AA99B1__INCLUDED_)
#define EA_61C909B7_E8C2_4f65_85DB_E31D73AA99B1__INCLUDED_

#include "Length.py"
#include "Integer.h"
#include "Boolean.h"
#include "IEC61968\AssetInfo\WireInsulationKind.java"
#include "IEC61968\AssetInfo\WireMaterialKind.java"
#include "java\IEC61970\IEC61970\Base\Domain\ResistancePerLength.java"
#include "CurrentFlow.h"
#include "String.h"
#include "IEC61968\AssetInfo\WirePhaseInfo.java"
#include "IEC61968\Assets\AssetInfo.java"

/**
 * Wire data that can be specified per line segment phase, or for the line segment
 * as a whole in case its phases all have the same wire characteristics.
 */
class WireInfo : public AssetInfo
{

public:
	WireInfo();
	/**
	 * (if there is a different core material) Radius of the central core.
	 */
	Length coreRadius;
	/**
	 * (if used) Number of strands in the steel core.
	 */
	Integer coreStrandCount;
	/**
	 * Geometric mean radius. If we replace the conductor by a thin walled tube of
	 * radius GMR, then its reactance is identical to the reactance of the actual
	 * conductor.
	 */
	Length gmr;
	/**
	 * True if conductor is insulated.
	 */
	Boolean insulated;
	/**
	 * (if insulated conductor) Material used for insulation.
	 */
	WireInsulationKind insulationMaterial;
	/**
	 * (if insulated conductor) Thickness of the insulation.
	 */
	Length insulationThickness;
	/**
	 * Conductor material.
	 */
	WireMaterialKind material;
	/**
	 * AC resistance per unit length of the conductor at 25 øC.
	 */
	ResistancePerLength rAC25;
	/**
	 * AC resistance per unit length of the conductor at 50 øC.
	 */
	ResistancePerLength rAC50;
	/**
	 * AC resistance per unit length of the conductor at 75 øC.
	 */
	ResistancePerLength rAC75;
	/**
	 * Outside radius of the wire.
	 */
	Length radius;
	/**
	 * Current carrying capacity of the wire under stated thermal conditions.
	 */
	CurrentFlow ratedCurrent;
	/**
	 * DC resistance per unit length of the conductor at 20 øC.
	 */
	ResistancePerLength rDC20;
	/**
	 * Describes the wire gauge or cross section (e.g., 4/0, #2, 336.5).
	 */
	String sizeDescription;
	/**
	 * Number of strands in the conductor.
	 */
	Integer strandCount;
	WirePhaseInfo *WirePhaseInfo;

};
#endif // !defined(EA_61C909B7_E8C2_4f65_85DB_E31D73AA99B1__INCLUDED_)
