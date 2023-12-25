from CIM_STD_PYTHON.TC57CIM.IEC61968.LoadControl.RemoteConnectDisconnectInfo import RemoteConnectDisconnectInfo
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceFunction import EndDeviceFunction
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.Switch import Switch

class ConnectDisconnectFunction(EndDeviceFunction):
    # 	/**
    # 	 * Running cumulative count of connect or disconnect events, for the lifetime of
    # 	 * this function or until the value is cleared.
    # 	 */
    def __init__(self):
        super().__init__()
        self.event_count = 0
        # 	/**
        # 	 * True if this function is in the connected state.
        # 	 */
        self.is_connected = False
        # 	/**
        # 	 * If set true, the switch may disconnect the service at the end of a specified
        # 	 * time delay after the disconnect signal has been given. If set false, the switch
        # 	 * may disconnect the service immediately after the disconnect signal has been
        # 	 * given. This is typically the case for over current circuit-breakers which are
        # 	 * classified as either instantaneous or slow acting.
        # 	 */
        self.is_delayed_discon = False
        # 	/**
        # 	 * If set true and if disconnection can be operated locally, the operation happens
        # 	 * automatically. Otherwise it happens manually.
        # 	 */
        self.is_local_auto_disconOp = False
        # 	/**
        # 	 * If set true and if reconnection can be operated locally, then the operation
        # 	 * happens automatically. Otherwise, it happens manually.
        # 	 */
        self.is_local_auto_recon_op = False
        # 	/**
        # 	 * If set true and if disconnection can be operated remotely, then the operation
        # 	 * happens automatically. If set false and if disconnection can be operated
        # 	 * remotely, then the operation happens manually.
        # 	 */
        self.is_remote_auto_discon_op = False
        # 	/**
        # 	 * If set true and if reconnection can be operated remotely, then the operation
        # 	 * happens automatically. If set false and if reconnection can be operated
        # 	 * remotely, then the operation happens manually.
        # 	 */
        self.is_remote_auto_recon_op = False
        # 	/**
        # 	 * Information on remote connect disconnect switch.
        # 	 */
        self.rcdInfo = RemoteConnectDisconnectInfo()
        self.Switches = Switch()
