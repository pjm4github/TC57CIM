# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Generation.Production.SteamSendoutSchedule import SteamSendoutSchedule
from IEC61970.Base.Generation.Production.ThermalGeneratingUnit import ThermalGeneratingUnit


class CogenerationPlant(PowerSystemResource):
    """
    A set of thermal generating units for the production of electrical energy and
    process steam (usually from the output of the steam turbines). The steam
    sendout is typically used for industrial purposes or for municipal heating and
    cooling.
    @created 02-Jan-2024 10:51:55 PM
    """

    def __init__(self):
        super().__init__()
        # The high pressure steam sendout.
        self.cogen_hp_sendout_rating = 0.0
        # The high pressure steam rating.
        self.cogen_hp_steam_rating = 0.0
        # The low pressure steam sendout.
        self.cogen_lp_sendout_rating = 0.0
        # The low pressure steam rating.
        self.cogen_lp_steam_rating = 0.0
        # The rated output active power of the cogeneration plant.
        self.rated_p = ActivePower()
        # A thermal generating unit may be a member of a cogeneration plant.
        self.thermal_generating_units = ThermalGeneratingUnit()
        # A cogeneration plant has a steam sendout schedule.
        self.steam_sendout_schedule = SteamSendoutSchedule()

# end CogenerationPlant
