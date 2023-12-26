///////////////////////////////////////////////////////////
//  IOPointSource.h
//  Implementation of the Class IOPointSource
//  Created on:      25-Dec-2023 8:31:59 PM
//  Original author: herb
///////////////////////////////////////////////////////////

#if !defined(EA_E907B672_A575_4c70_A296_0623DCD121FB__INCLUDED_)
#define EA_E907B672_A575_4c70_A296_0623DCD121FB__INCLUDED_

#include "IOPoint.py"
#include "MeasurementValueSource.py"

/**
 * Indicates the point source for an IO Point.
 */
class IOPointSource : public MeasurementValueSource
{

public:
	IOPointSource();
	IOPoint *IOPoint;

};
#endif // !defined(EA_E907B672_A575_4c70_A296_0623DCD121FB__INCLUDED_)
