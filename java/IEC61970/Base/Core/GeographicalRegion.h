///////////////////////////////////////////////////////////
//  GeographicalRegion.h
//  Implementation of the Class GeographicalRegion
//  Created on:      25-Dec-2023 8:31:58 PM
///////////////////////////////////////////////////////////

#if !defined(EA_DDC4040E_07DF_4932_B62D_00E52BB8F163__INCLUDED_)
#define EA_DDC4040E_07DF_4932_B62D_00E52BB8F163__INCLUDED_

#include "SubGeographicalRegion.h"
#include "IdentifiedObject.py"

/**
 * A geographical region of a power system network model.
 */
class GeographicalRegion : public IdentifiedObject
{

public:
	GeographicalRegion();
	/**
	 * All sub-geograhpical regions within this geographical region.
	 */
	SubGeographicalRegion *Regions;

};
#endif // !defined(EA_DDC4040E_07DF_4932_B62D_00E52BB8F163__INCLUDED_)
