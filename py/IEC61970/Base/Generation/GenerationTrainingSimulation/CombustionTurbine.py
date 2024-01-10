from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.Temperature import Temperature
from IEC61970.Base.Generation.GenerationTrainingSimulation.CCTempActivePowerCurve import CTTempActivePowerCurve
from IEC61970.Base.Generation.GenerationTrainingSimulation.PrimeMover import PrimeMover
from IEC61970.Base.Generation.Production.AirCompressor import AirCompressor


class CombustionTurbine(PrimeMover):
    """
    A prime mover that is typically fueled by gas or light oil.
    Created: 02-Jan-2024 11:05:05 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.ambient_temp = Temperature()  # Default ambient temperature for modeling applications
        self.aux_power_versus_frequency = PU()  # Off-nominal frequency effect on turbine auxiliaries
        self.aux_power_versus_voltage = PU()  # Off-nominal voltage effect on turbine auxiliaries
        self.capability_versus_frequency = PU()  # Off-nominal frequency effect on turbine capability
        self.heat_recovery_flag = True  # True if associated with a heat recovery boiler
        self.power_variation_by_temp = PU()  # Per unit change in power versus unit change in ambient temperature
        self.reference_temp = Temperature()  # Reference temperature for turbine output
        self.time_constant = Seconds()  # Time constant for the turbine
        self.air_compressor = AirCompressor()  # Associated CAES air compressor
        self.ct_temp_active_power_curve = CTTempActivePowerCurve()  # Active power versus ambient temperature relationship
        # Assuming PrimeMover, Temperature, PU, Boolean, Seconds, AirCompressor, and CTTempActivePowerCurve are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented
