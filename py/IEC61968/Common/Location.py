# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local imports
from IEC61968.Common.ConfigurationEvent import ConfigurationEvent
from IEC61968.Common.CoordinateSystem import CoordinateSystem
from IEC61968.Common.Crew import Crew
from IEC61968.Common.ElectronicAddress import ElectronicAddress
from IEC61968.Common.PositionPoint import PositionPoint
from IEC61968.Common.Status import Status
from IEC61968.Common.StreetAddress import StreetAddress
from IEC61968.Common.TelephoneNumber import TelephoneNumber
from IEC61970.Base.Meas.Measurement import Measurement
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61968.Operations.SwitchingOrder import SwitchingOrder


class Location(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.direction = ""
        self.electronic_address = ElectronicAddress()
        self.geo_info_reference = ""
        self.main_address = StreetAddress()
        self.phone1 = TelephoneNumber()
        self.phone2 = TelephoneNumber()
        self.secondary_address = StreetAddress()
        self.status = Status()
        self.type = ""
        self.measurements = Measurement()
        self.coordinate_system = CoordinateSystem()
        self.power_system_resources = PowerSystemResource()
        self.configuration_events = ConfigurationEvent()
        self.crew = Crew()
        self.switching_order = SwitchingOrder()
        self.position_points = PositionPoint()
