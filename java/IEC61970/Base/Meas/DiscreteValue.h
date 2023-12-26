///////////////////////////////////////////////////////////
//  DiscreteValue.h
//  Implementation of the Class DiscreteValue
//  Created on:      25-Dec-2023 8:31:56 PM
///////////////////////////////////////////////////////////

#if !defined(EA_6564763C_387D_4c7b_A4BE_313B2F58E5C2__INCLUDED_)
#define EA_6564763C_387D_4c7b_A4BE_313B2F58E5C2__INCLUDED_

#include "Integer.h"
#include "Command.h"
#include "MeasurementValue.h"

/**
 * DiscreteValue represents a discrete MeasurementValue.
 */
class DiscreteValue : public MeasurementValue
{

public:
	DiscreteValue();
	/**
	 * The value to supervise.
	 */
	Integer value;
	/**
	 * The Control variable associated with the MeasurementValue.
	 */
	Command *Command;

};
#endif // !defined(EA_6564763C_387D_4c7b_A4BE_313B2F58E5C2__INCLUDED_)
