package IEC61968.Metering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Minutes;
import IEC61968.Assets.AssetContainer;
import IEC61968.DER.DispatchablePowerCapability;

/**
 * Asset container that performs one or more end device functions. One type of end
 * device is a meter which can perform metering, load management,
 * connect/disconnect, accounting functions, etc. Some end devices, such as ones
 * monitoring and controlling air conditioners, refrigerators, pool pumps may be
 * connected to a meter. All end devices may have communication capability defined
 * by the associated communication function(s). An end device may be owned by a
 * consumer, a service provider, utility or otherwise.
 * There may be a related end device function that identifies a sensor or control
 * point within a metering application or communications systems (e.g., water, gas,
 * electricity).
 * Some devices may use an optical port that conforms to the ANSI C12.18 standard
 * for communications.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class EndDevice extends AssetContainer {

	/**
	 * Automated meter reading (AMR) or other communication system responsible for
	 * communications to this end device.
	 */
	public String amrSystem;
	/**
	 * Installation code.
	 */
	public String installCode;
	/**
	 * If true, this is a premises area network (PAN) device.
	 */
	public Boolean isPan;
	public Boolean isSmartInverter;
	/**
	 * If true, there is no physical device. As an example, a virtual meter can be
	 * defined to aggregate the consumption for two or more physical meters. Otherwise,
	 * this is a physical hardware device.
	 */
	public Boolean isVirtual;
	/**
	 * Time zone offset relative to GMT for the location of this end device.
	 */
	public Minutes timeZoneOffset;
	/**
	 * End device data.
	 */
	public EndDeviceInfo EndDeviceInfo;
	/**
	 * All end device functions this end device performs.
	 */
	public EndDeviceFunction EndDeviceFunctions;
	public DispatchablePowerCapability DispatchablePowerCapability;

	public EndDevice(){

	}
}//end EndDevice