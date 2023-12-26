package IEC61970.Dynamics.StandardInterconnections;

import IEC61970.Base.Core.Terminal;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Supports connection to a terminal associated with a remote bus from which an
 * input signal of a specific type is coming.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class RemoteInputSignal extends IdentifiedObject {

	/**
	 * Type of input signal.
	 */
	public RemoteSignalKind remoteSignalType;
	/**
	 * Remote terminal with which this input signal is associated.
	 */
	public Terminal Terminal;

	public RemoteInputSignal(){

	}
}//end RemoteInputSignal