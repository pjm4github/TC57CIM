package IEC61968.Metering;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Temperature;

/**
 * PAN control used to issue action/command to PAN devices during a demand
 * response/load control event.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class PanDemandResponse extends EndDeviceAction {

	/**
	 * Appliance being controlled.
	 */
	public ControlledAppliance appliance;
	/**
	 * Used to define a maximum energy usage limit as a percentage of the client
	 * implementations specific average energy usage. The load adjustment percentage
	 * is added to 100% creating a percentage limit applied to the client
	 * implementations specific average energy usage. A -10% load adjustment
	 * percentage will establish an energy usage limit equal to 90% of the client
	 * implementations specific average energy usage. Each load adjustment percentage
	 * is referenced to the client implementations specific average energy usage.
	 * There are no cumulative effects.
	 * The range of this field is -100% to +100% with a resolution of 1. A -100% value
	 * equals a total load shed. A +100% value will limit the energy usage to the
	 * client implementations specific average energy usage.
	 */
	public PerCent avgLoadAdjustment;
	/**
	 * Encoding of cancel control.
	 */
	public String cancelControlMode;
	/**
	 * Timestamp when a canceling of the event is scheduled to start.
	 */
	public DateTime cancelDateTime;
	/**
	 * If true, a canceling of the event should start immediately.
	 */
	public Boolean cancelNow;
	/**
	 * Requested offset to apply to the normal cooling setpoint at the time of the
	 * start of the event. It represents a temperature change that will be applied to
	 * the associated cooling set point. The temperature offsets will be calculated
	 * per the local temperature in the thermostat. The calculated temperature will be
	 * interpreted as the number of degrees to be added to the cooling set point.
	 * Sequential demand response events are not cumulative. The offset shall be
	 * applied to the normal setpoint.
	 */
	public Temperature coolingOffset;
	/**
	 * Requested cooling set point. Temperature set point is typically defined and
	 * calculated based on local temperature.
	 */
	public Temperature coolingSetpoint;
	/**
	 * Level of criticality for the action of this control. The action taken by load
	 * control devices for an event can be solely based on this value, or in
	 * combination with other load control event fields supported by the device.
	 */
	public String criticalityLevel;
	/**
	 * Maximum "on" state duty cycle as a percentage of time. For example, if the
	 * value is 80, the device would be in an "on" state for 80% of the time for the
	 * duration of the action.
	 */
	public PerCent dutyCycle;
	/**
	 * Provides a mechanism to direct load control actions to groups of PAN devices.
	 * It can be used in conjunction with the PAN device types.
	 */
	public String enrollmentGroup;
	/**
	 * Requested offset to apply to the normal heating setpoint at the time of the
	 * start of the event. It represents a temperature change that will be applied to
	 * the associated heating set point. The temperature offsets will be calculated
	 * per the local temperature in the thermostat. The calculated temperature will be
	 * interpreted as the number of degrees to be subtracted from the heating set
	 * point. Sequential demand response events are not cumulative. The offset shall
	 * be applied to the normal setpoint.
	 */
	public Temperature heatingOffset;
	/**
	 * Requested heating set point. Temperature set point is typically defined and
	 * calculated based on local temperature.
	 */
	public Temperature heatingSetpoint;

	public PanDemandResponse(){

	}
}//end PanDemandResponse