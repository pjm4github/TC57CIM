# EndDevice.py
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.AssetContainer import AssetContainer
from CIM_STD_PYTHON.TC57CIM.IEC61968.DER.DispatchablePowerCapability import DispatchablePowerCapability
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceFunction import EndDeviceFunction
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceInfo import EndDeviceInfo
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Minutes import Minutes


class EndDevice(AssetContainer):
    """
    Asset container that performs one or more end device functions. One type of end
    device is a meter which can perform metering, load management,
    connect/disconnect, accounting functions, etc. Some end devices, such as ones
    monitoring and controlling air conditioners, refrigerators, pool pumps may be
    connected to a meter. All end devices may have communication capability defined
    by the associated communication function(s). An end device may be owned by a
    consumer, a service provider, utility or otherwise.
    There may be a related end device function that identifies a sensor or control
    point within a metering application or communications systems (e.g., water, gas,
    electricity).
    Some devices may use an optical port that conforms to the ANSI C12.18 standard
    for communications.
    """

    def __init__(self):
        super().__init__()
        self.amr_system = ""  # Automated meter reading (AMR) or other communication system responsible for communications to this end device.
        self.install_code = ""  # Installation code.
        self.is_pan = False  # If true, this is a premises area network (PAN) device.
        self.is_smart_inverter = False
        self.is_virtual = False  # If true, there is no physical device. As an example, a virtual meter can be defined to aggregate the consumption for two or more physical meters. Otherwise, this is a physical hardware device.
        self.time_zone_offset = Minutes()  # Time zone offset relative to GMT for the location of this end device.
        self.end_device_info = EndDeviceInfo()  # End device data.
        self.end_device_functions = EndDeviceFunction()  # All end device functions this end device performs.
        self.dispatchable_power_capability = DispatchablePowerCapability()