///////////////////////////////////////////////////////////
//  ConnectDisconnectFunction.h
//  Implementation of the Class ConnectDisconnectFunction
//  Created on:      25-Dec-2023 8:45:20 PM
///////////////////////////////////////////////////////////

#if !defined(EA_233B4CD7_3294_42c5_9E3C_B09F04B37843__INCLUDED_)
#define EA_233B4CD7_3294_42c5_9E3C_B09F04B37843__INCLUDED_

#include "Integer.h"
#include "Boolean.h"
#include "RemoteConnectDisconnectInfo.h"
#include "Switch.h"
#include "EndDeviceFunction.py"

/**
 * A function that will disconnect and reconnect the customer's load under defined
 * conditions.
 */
class ConnectDisconnectFunction : public EndDeviceFunction
{

public:
	ConnectDisconnectFunction();
	/**
	 * Running cumulative count of connect or disconnect events, for the lifetime of
	 * this function or until the value is cleared.
	 */
	Integer eventCount;
	/**
	 * True if this function is in the connected state.
	 */
	Boolean isConnected;
	/**
	 * If set true, the switch may disconnect the service at the end of a specified
	 * time delay after the disconnect signal has been given. If set false, the switch
	 * may disconnect the service immediately after the disconnect signal has been
	 * given. This is typically the case for over current circuit-breakers which are
	 * classified as either instantaneous or slow acting.
	 */
	Boolean isDelayedDiscon;
	/**
	 * If set true and if disconnection can be operated locally, the operation happens
	 * automatically. Otherwise it happens manually.
	 */
	Boolean isLocalAutoDisconOp;
	/**
	 * If set true and if reconnection can be operated locally, then the operation
	 * happens automatically. Otherwise, it happens manually.
	 */
	Boolean isLocalAutoReconOp;
	/**
	 * If set true and if disconnection can be operated remotely, then the operation
	 * happens automatically. If set false and if disconnection can be operated
	 * remotely, then the operation happens manually.
	 */
	Boolean isRemoteAutoDisconOp;
	/**
	 * If set true and if reconnection can be operated remotely, then the operation
	 * happens automatically. If set false and if reconnection can be operated
	 * remotely, then the operation happens manually.
	 */
	Boolean isRemoteAutoReconOp;
	/**
	 * Information on remote connect disconnect switch.
	 */
	RemoteConnectDisconnectInfo rcdInfo;
	Switch *Switches;

};
#endif // !defined(EA_233B4CD7_3294_42c5_9E3C_B09F04B37843__INCLUDED_)
