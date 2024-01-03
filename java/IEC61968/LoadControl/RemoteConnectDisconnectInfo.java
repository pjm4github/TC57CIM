package IEC61968.LoadControl;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.RealEnergy;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.ActivePower;

/**
 * Details of remote connect and disconnect function.
 * @author T. Kostic
 * @version 1.0
 * @created 02-Jan-2024 10:00:50 PM
 */
public class RemoteConnectDisconnectInfo {

	/**
	 * Setting of the timeout elapsed time.
	 */
	public Seconds armedTimeout;
	/**
	 * Voltage limit on customer side of RCD switch above which the connect should not
	 * be made.
	 */
	public Voltage customerVoltageLimit;
	/**
	 * Limit of energy before disconnect.
	 */
	public RealEnergy energyLimit;
	/**
	 * Start date and time to accumulate energy for energy usage limiting.
	 */
	public DateTime energyUsageStartDateTime;
	/**
	 * Warning energy limit, used to trigger event code that energy usage is nearing
	 * limit.
	 */
	public RealEnergy energyUsageWarning;
	/**
	 * True if the RCD switch has to be armed before a connect action can be initiated.
	 */
	public Boolean isArmConnect;
	/**
	 * True if the RCD switch has to be armed before a disconnect action can be
	 * initiated.
	 */
	public Boolean isArmDisconnect;
	/**
	 * True if the energy usage is limited and the customer will be disconnected if
	 * they go over the limit.
	 */
	public Boolean isEnergyLimiting;
	/**
	 * True if load limit has to be checked to issue an immediate disconnect (after a
	 * connect) if load is over the limit.
	 */
	public Boolean needsPowerLimitCheck;
	/**
	 * True if voltage limit has to be checked to prevent connect if voltage is over
	 * the limit.
	 */
	public Boolean needsVoltageLimitCheck;
	/**
	 * Load limit above which the connect should either not take place or should cause
	 * an immediate disconnect.
	 */
	public ActivePower powerLimit;
	/**
	 * True if pushbutton has to be used for connect.
	 */
	public Boolean usePushbutton;

	public RemoteConnectDisconnectInfo(){

	}
}//end RemoteConnectDisconnectInfo