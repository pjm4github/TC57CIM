package IEC61968.LoadControl;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Wires.Switch;
import IEC61968.Metering.EndDeviceFunction;

/**
 * A function that will disconnect and reconnect the customer's load under defined
 * conditions.
 * @created 02-Jan-2024 10:00:32 PM
 */
public class ConnectDisconnectFunction extends EndDeviceFunction {

	/**
	 * Running cumulative count of connect or disconnect events, for the lifetime of
	 * this function or until the value is cleared.
	 */
	public Integer eventCount;
	/**
	 * True if this function is in the connected state.
	 */
	public Boolean isConnected;
	/**
	 * If set true, the switch may disconnect the service at the end of a specified
	 * time delay after the disconnect signal has been given. If set false, the switch
	 * may disconnect the service immediately after the disconnect signal has been
	 * given. This is typically the case for over current circuit-breakers which are
	 * classified as either instantaneous or slow acting.
	 */
	public Boolean isDelayedDiscon;
	/**
	 * If set true and if disconnection can be operated locally, the operation happens
	 * automatically. Otherwise it happens manually.
	 */
	public Boolean isLocalAutoDisconOp;
	/**
	 * If set true and if reconnection can be operated locally, then the operation
	 * happens automatically. Otherwise, it happens manually.
	 */
	public Boolean isLocalAutoReconOp;
	/**
	 * If set true and if disconnection can be operated remotely, then the operation
	 * happens automatically. If set false and if disconnection can be operated
	 * remotely, then the operation happens manually.
	 */
	public Boolean isRemoteAutoDisconOp;
	/**
	 * If set true and if reconnection can be operated remotely, then the operation
	 * happens automatically. If set false and if reconnection can be operated
	 * remotely, then the operation happens manually.
	 */
	public Boolean isRemoteAutoReconOp;
	/**
	 * Information on remote connect disconnect switch.
	 */
	public RemoteConnectDisconnectInfo rcdInfo;
	public Switch Switches;

	public ConnectDisconnectFunction(){

	}
}//end ConnectDisconnectFunction