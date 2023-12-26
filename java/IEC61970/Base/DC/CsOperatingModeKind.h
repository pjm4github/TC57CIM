///////////////////////////////////////////////////////////
//  CsOperatingModeKind.h
//  Implementation of the Class CsOperatingModeKind
//  Created on:      25-Dec-2023 8:31:55 PM
//  Original author: selaost1
///////////////////////////////////////////////////////////

#if !defined(EA_BFC44D04_F000_4c49_BB04_2B4797B1BB10__INCLUDED_)
#define EA_BFC44D04_F000_4c49_BB04_2B4797B1BB10__INCLUDED_

/**
 * Operating mode for HVDC line operating as Current Source Converter.
 */
enum CsOperatingModeKind
{
	/**
	 * Operating as inverter
	 */
	inverter,
	/**
	 * Operating as rectifier.
	 */
	rectifier
};
#endif // !defined(EA_BFC44D04_F000_4c49_BB04_2B4797B1BB10__INCLUDED_)
