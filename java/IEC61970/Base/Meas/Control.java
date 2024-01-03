package IEC61970.Base.Meas;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.UnitSymbol;

/**
 * Control is used for supervisory/device control. It represents control outputs
 * that are used to change the state in a process, e.g. close or open breaker, a
 * set point value or a raise lower command.
 * @created 02-Jan-2024 11:16:21 PM
 */
public class Control extends IOPoint {

	/**
	 * Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint,
	 * TieLineFlow etc. The ControlType.name shall be unique among all specified types
	 * and describe the type.
	 */
	public String controlType;
	/**
	 * Indicates that a client is currently sending control commands that has not
	 * completed.
	 */
	public Boolean operationInProgress;
	/**
	 * The last time a control output was sent.
	 */
	public DateTime timeStamp;
	/**
	 * The unit multiplier of the controlled quantity.
	 */
	public UnitMultiplier unitMultiplier;
	/**
	 * The unit of measure of the controlled quantity.
	 */
	public UnitSymbol unitSymbol;

	public Control(){

	}
}//end Control