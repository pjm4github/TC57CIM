# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 12:50:20 2023
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC62325.InfIEC62325.InfEnergyScheduling.TransmissionRightOfWay import TransmissionRightOfWay


class TransmissionCorridor(PowerSystemResource):
    """
    A corridor containing one or more rights of way
    @created 27-Dec-2023 12:45:03 PM
    """

    def __init__(self) -> None:
        # 	 * A transmission right-of-way is a member of a transmission corridor
        super().__init__()
        self.transmission_right_of_ways = [TransmissionRightOfWay]

