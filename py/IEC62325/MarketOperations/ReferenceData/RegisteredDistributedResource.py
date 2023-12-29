# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource


class RegisteredDistributedResource(RegisteredResource):

    def __init__(self):
        super().__init__()
        # The type of resource. Examples include: fuel cell, flywheel, photovoltaic,
        # micro-turbine, CHP (combined heat power), V2G (vehicle to grid), DES
        # (distributed energy storage), and others.
        self.distributed_resource_type = ""
