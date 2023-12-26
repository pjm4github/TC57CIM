///////////////////////////////////////////////////////////
//  AssetFunction.h
//  Implementation of the Class AssetFunction
//  Created on:      25-Dec-2023 8:45:19 PM
///////////////////////////////////////////////////////////

#if !defined(EA_6015C078_F27F_4fc4_9948_552D09E283A6__INCLUDED_)
#define EA_6015C078_F27F_4fc4_9948_552D09E283A6__INCLUDED_

#include "String.h"
#include "IdentifiedObject.py"

/**
 * Function performed by an asset.
 */
class AssetFunction : public IdentifiedObject
{

public:
	AssetFunction();
	/**
	 * Configuration specified for this function.
	 */
	String configID;
	/**
	 * Firmware version.
	 */
	String firmwareID;
	/**
	 * Hardware version.
	 */
	String hardwareID;
	/**
	 * Password needed to access this function.
	 */
	String password;
	/**
	 * Name of program.
	 */
	String programID;

};
#endif // !defined(EA_6015C078_F27F_4fc4_9948_552D09E283A6__INCLUDED_)
