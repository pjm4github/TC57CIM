# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 12:50:20 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea


class AreaReserveSpec:
    """
    The control area's reserve specification.
    @created 27-Dec-2023 12:43:12 PM
    """

    def __init__(self) -> None:
        pass
        # Description of the object or instance.
        self.description: str = ""
        # Lower regulating margin requirement in MW, the amount of generation that can be
        # dropped by control in 10 minutes
        self.lower_reg_margin_reqt: ActivePower = ActivePower()
        # Operating reserve requirement in MW, where operating reserve is the generating
        # capability that is fully available within 30 minutes. Operating reserve is
        # composed of primary reserve (t less than 10 min) and secondary reserve (10 less
        # than t less than 30 min).
        self.op_reserve_reqt: ActivePower = ActivePower()
        # Primary reserve requirement in MW, where primary reserve is generating
        # capability that is fully available within 10 minutes. Primary reserve is
        # composed of spinning reserve and quick-start reserve.
        self.primary_reserve_reqt: ActivePower = ActivePower()
        # Raise regulating margin requirement in MW, the amount of generation that can be
        # picked up by control in 10 minutes
        self.raise_reg_margin_reqt: ActivePower = ActivePower()
        # Spinning reserve requirement in MW, spinning reserve is generating capability
        # that is presently synchronized to the network and is fully available within 10
        # minutes
        self.spinning_reserve_reqt: ActivePower = ActivePower()
        self.sub_control_area: SubControlArea = SubControlArea()
