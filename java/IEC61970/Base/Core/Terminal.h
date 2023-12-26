///////////////////////////////////////////////////////////
//  Terminal.h
//  Implementation of the Class Terminal
//  Created on:      25-Dec-2023 8:32:04 PM
///////////////////////////////////////////////////////////

#if !defined(EA_BCC75025_9EC5_473a_B44E_701A6112AEBB__INCLUDED_)
#define EA_BCC75025_9EC5_473a_B44E_701A6112AEBB__INCLUDED_

#include "PhaseCode.py"
#include "ConnectivityNode.py"
#include "ConductingEquipment.py"
#include "java\IEC61970\IEC61970\Base\Wires\RegulatingControl.java"
#include "java\IEC61970\IEC61970\Base\Core\ACDCTerminal.java"

/**
 * An AC electrical connection point to a piece of conducting equipment. Terminals
 * are connected at physical connection points called connectivity nodes.
 */
class Terminal : public ACDCTerminal
{

public:
	Terminal();
	/**
	 * Represents the normal network phasing condition.
	 * If the attribute is missing three phases (ABC or ABCN) shall be assumed.
	 */
	PhaseCode phases;
	/**
	 * The connectivity node to which this terminal connects with zero impedance.
	 */
	ConnectivityNode *ConnectivityNode;
	/**
	 * The conducting equipment of the terminal.  Conducting equipment have  terminals
	 * that may be connected to other conducting equipment terminals via connectivity
	 * nodes or topological nodes.
	 */
	ConductingEquipment *ConductingEquipment;
	/**
	 * The controls regulating this terminal.
	 */
	RegulatingControl *RegulatingControl;

};
#endif // !defined(EA_BCC75025_9EC5_473a_B44E_701A6112AEBB__INCLUDED_)
