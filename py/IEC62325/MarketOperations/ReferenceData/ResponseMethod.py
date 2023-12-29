# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.ReferenceData.RegisteredDistributedResource import RegisteredDistributedResource


class ResponseMethod(IdentifiedObject):
    """
    Specifies a category of energy usage that the demand response applies for; e.g.
    energy from lighting, HVAC, other.
    @author mwald
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        super().__init__()

        # The active power value for the demand adjustment type. This supports requests
        # to be made to a resource for some amount of active power provided by a
        # particular response method, as specified by the method attribute (e.g. lighting,
        # HVAC, wall mounted air conditioners, etc.).
        self.active_power = 0.0

        # The unit of measure of active power, e.g. kiloWatts (kW), megaWatts (mW), etc.
        self.active_power_uom = ""

        # The response method (e.g. lighting, HVAC, wall mounted air conditioners, etc.).
        self.method = ""

        # This value provides for scaling of a response method's active power. For
        # example, a response method of air conditioning could utilize a small amount of
        # active power from each air conditioning unit (e.g. 0.1 kiloWatt), but the site
        # multiplier could be used to produce a the total active power adjustment by
        # multiplying the response method active power by this value (e.g. a building
        # with 100 window air conditioning units, so 100 * 0.1 kW = 10 kW).
        self.site_multiplier = 0

        self.registered_resource = RegisteredDistributedResource()
