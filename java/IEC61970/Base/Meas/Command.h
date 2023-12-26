///////////////////////////////////////////////////////////
//  Command.h
//  Implementation of the Class Command
//  Created on:      25-Dec-2023 8:31:55 PM
///////////////////////////////////////////////////////////

#if !defined(EA_41A32710_96B9_42d8_8C28_2FAE0A658448__INCLUDED_)
#define EA_41A32710_96B9_42d8_8C28_2FAE0A658448__INCLUDED_

#include "Integer.h"
#include "ValueAliasSet.py"
#include "Control.py"

/**
 * A Command is a discrete control used for supervisory control.
 */
class Command : public Control
{

public:
	Command();
	/**
	 * Normal value for Control.value e.g. used for percentage scaling.
	 */
	Integer normalValue;
	/**
	 * The value representing the actuator output.
	 */
	Integer value;
	/**
	 * The ValueAliasSet used for translation of a Control value to a name.
	 */
	ValueAliasSet *ValueAliasSet;

};
#endif // !defined(EA_41A32710_96B9_42d8_8C28_2FAE0A658448__INCLUDED_)
