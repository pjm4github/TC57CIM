///////////////////////////////////////////////////////////
//  RemoteConnectDisconnectInfo.h
//  Implementation of the Class RemoteConnectDisconnectInfo
//  Created on:      25-Dec-2023 8:45:24 PM
//  Original author: T. Kostic
///////////////////////////////////////////////////////////

#if !defined(EA_4AF6AABE_5C9C_4e9e_8693_71667A07F837__INCLUDED_)
#define EA_4AF6AABE_5C9C_4e9e_8693_71667A07F837__INCLUDED_

#include "Seconds.py"
#include "Voltage.h"
#include "RealEnergy.py"
#include "DateTime.py"
#include "Boolean.h"
#include "ActivePower.h"

/**
 * Details of remote connect and disconnect function.
 */
class RemoteConnectDisconnectInfo
{

public:
	RemoteConnectDisconnectInfo();
	/**
	 * Setting of the timeout elapsed time.
	 */
	Seconds armedTimeout;
	/**
	 * Voltage limit on customer side of RCD switch above which the connect should not
	 * be made.
	 */
	Voltage customerVoltageLimit;
	/**
	 * Limit of energy before disconnect.
	 */
	RealEnergy energyLimit;
	/**
	 * Start date and time to accumulate energy for energy usage limiting.
	 */
	DateTime energyUsageStartDateTime;
	/**
	 * Warning energy limit, used to trigger event code that energy usage is nearing
	 * limit.
	 */
	RealEnergy energyUsageWarning;
	/**
	 * True if the RCD switch has to be armed before a connect action can be initiated.
	 */
	Boolean isArmConnect;
	/**
	 * True if the RCD switch has to be armed before a disconnect action can be
	 * initiated.
	 */
	Boolean isArmDisconnect;
	/**
	 * True if the energy usage is limited and the customer will be disconnected if
	 * they go over the limit.
	 */
	Boolean isEnergyLimiting;
	/**
	 * True if load limit has to be checked to issue an immediate disconnect (after a
	 * connect) if load is over the limit.
	 */
	Boolean needsPowerLimitCheck;
	/**
	 * True if voltage limit has to be checked to prevent connect if voltage is over
	 * the limit.
	 */
	Boolean needsVoltageLimitCheck;
	/**
	 * Load limit above which the connect should either not take place or should cause
	 * an immediate disconnect.
	 */
	ActivePower powerLimit;
	/**
	 * True if pushbutton has to be used for connect.
	 */
	Boolean usePushbutton;

};
#endif // !defined(EA_4AF6AABE_5C9C_4e9e_8693_71667A07F837__INCLUDED_)
