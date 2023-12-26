///////////////////////////////////////////////////////////
//  WirePosition.h
//  Implementation of the Class WirePosition
//  Created on:      25-Dec-2023 8:45:26 PM
///////////////////////////////////////////////////////////

#if !defined(EA_CC2E91A3_1D78_4091_9D46_456F4500A833__INCLUDED_)
#define EA_CC2E91A3_1D78_4091_9D46_456F4500A833__INCLUDED_

#include "java\IEC61970\IEC61970\Base\Domain\Displacement.java"
#include "IdentifiedObject.py"
#include "IEC61968\AssetInfo\WirePhaseInfo.java"

/**
 * Identification, spacing and configuration of the wires of a conductor with
 * respect to a structure.
 */
class WirePosition : public IdentifiedObject
{

public:
	WirePosition();
	/**
	 * Signed horizontal distance from the wire at this position to a common reference
	 * point.
	 */
	Displacement xCoord;
	/**
	 * Signed vertical distance from the wire at this position: above ground (positive
	 * value) or burial depth below ground (negative value).
	 */
	Displacement yCoord;
	WirePhaseInfo *WirePhaseInfo;

};
#endif // !defined(EA_CC2E91A3_1D78_4091_9D46_456F4500A833__INCLUDED_)
