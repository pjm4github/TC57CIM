###########################################################
# WeatherStation.py
# Implementation of the Class WeatherStation
# Created on:      18-Dec-2023 3:17:41 PM
# Original author: akamath
###########################################################
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.PowerSystemResource import PowerSystemResource

class WeatherStation(PowerSystemResource):
    def __init__(self):
        super().__init__()
