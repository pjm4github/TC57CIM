///////////////////////////////////////////////////////////
//  ValueToAlias.h
//  Implementation of the Class ValueToAlias
//  Created on:      25-Dec-2023 8:32:04 PM
///////////////////////////////////////////////////////////

#if !defined(EA_10E06216_8FD8_445a_8E38_031FF5EBFC55__INCLUDED_)
#define EA_10E06216_8FD8_445a_8E38_031FF5EBFC55__INCLUDED_

#include "Integer.h"
#include "IdentifiedObject.py"

/**
 * Describes the translation of one particular value into a name, e.g. 1 as "Open".
 */
class ValueToAlias : public IdentifiedObject
{

public:
	ValueToAlias();
	/**
	 * The value that is mapped.
	 */
	Integer value;

};
#endif // !defined(EA_10E06216_8FD8_445a_8E38_031FF5EBFC55__INCLUDED_)
