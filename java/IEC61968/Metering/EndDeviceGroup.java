package IEC61968.Metering;

import IEC61968.Common.Status;
import IEC61970.Base.Domain.String;
import IEC61968.Common.Version;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.DER.DERGroupDispatch;
import IEC61968.DER.DispatchablePowerCapability;
import IEC61968.DER.DERMonitorableParameter;

/**
 * Abstraction for management of group communications within a two-way AMR system
 * or the data for a group of related end devices. Commands can be issued to all
 * of the end devices that belong to the group using a defined group address and
 * the underlying AMR communication infrastructure. A DERGroup and a
 * PANDeviceGroup is an EndDeviceGroup.
 * @created 03-Jan-2024 1:10:15 PM
 */
public class EndDeviceGroup extends IdentifiedObject {

	public Status status;
	/**
	 * Type of this group.
	 */
	public String type;
	public Version version;
	/**
	 * All end devices this end device group refers to.
	 */
	public EndDevice EndDevices;
	/**
	 * All end device controls sending commands to this end device group.
	 */
	public EndDeviceControl EndDeviceControls;
	public DERGroupDispatch DERGroupDispatch;
	public DispatchablePowerCapability DispatchablePowerCapability;
	public DERMonitorableParameter DERMonitorableParameter;

	public EndDeviceGroup(){

	}
}//end EndDeviceGroup