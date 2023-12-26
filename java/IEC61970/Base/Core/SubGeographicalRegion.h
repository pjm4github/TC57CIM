///////////////////////////////////////////////////////////
//  SubGeographicalRegion.h
//  Implementation of the Class SubGeographicalRegion
//  Created on:      25-Dec-2023 8:32:03 PM
///////////////////////////////////////////////////////////

#if !defined(EA_4A2D3E8E_2DF9_478d_A763_3E24155D4B9D__INCLUDED_)
#define EA_4A2D3E8E_2DF9_478d_A763_3E24155D4B9D__INCLUDED_

#include "Line.h"
#include "Substation.h"
#include "IdentifiedObject.py"

/**
 * A subset of a geographical region of a power system network model.
 */
class SubGeographicalRegion : public IdentifiedObject
{

public:
	SubGeographicalRegion();
	/**
	 * The lines within the sub-geographical region.
	 */
	Line *Lines;
	/**
	 * The substations in this sub-geographical region.
	 */
	Substation *Substations;

};
#endif // !defined(EA_4A2D3E8E_2DF9_478d_A763_3E24155D4B9D__INCLUDED_)
