# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:15:59 2024
# public class MeasValueSet extends IdentifiedObject {
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Meas.MeasurementValue import MeasurementValue
from IEC61970.InfIEC61970.SCADA_EMS.Meas.MeasValueConfiguration import MeasValueConfiguration


class MeasValueSet(IdentifiedObject):
    """A set of Measurement Values."""
    
    def __init__(self):
        super().__init__()
        # public PerCent anaogValueDeadband;
        self.anaog_value_deadband = PerCent()  # initialize to default PerCent value
        # public Boolean reportDiscreteOnChange;
        self.report_discrete_on_change = False  # initialize to default Boolean value
        # public MeasValueConfiguration m_MeasValueConfiguration;
        self.m_meas_value_configuration = MeasValueConfiguration()  # initialize to default MeasValueConfiguration value
        # public MeasurementValue m_MeasurementValue;
        self.m_measurement_value = MeasurementValue()  # initialize to default MeasurementValue value
        # public MeasValueSet() {}
        # Constructor
