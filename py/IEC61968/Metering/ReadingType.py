from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.AccumulationKind import AccumulationKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.AggregateKind import AggregateKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.RationalNumber import RationalNumber
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.CommodityKind import CommodityKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.FlowDirectionKind import FlowDirectionKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.ReadingInterharmonic import ReadingInterharmonic
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.MacroPeriodKind import MacroPeriodKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.MeasurementKind import MeasurementKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.MeasuringPeriodKind import MeasuringPeriodKind

from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.Channel import Channel
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.PhaseCode import PhaseCode
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Currency import Currency
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class ReadingType(IdentifiedObject):
    """
    Detailed description for a type of a reading value. Values in attributes allow
    for the creation of recommended codes to be used for identifying reading value
    types as follows: <macroPeriod>.<aggregate>.<measuringPeriod>.<accumulation>.
    <flowDirection>.<commodity>.<measurementKind>.<interharmonic.numerator>.
    <interharmonic.denominator>.<argument.numerator>.<argument.denominator>.<tou>.
    <cpp>.<consumptionTier>.<phases>.<multiplier>.<unit>.<currency>.
    """

    def __init__(self):
        super().__init__()
        self.accumulation = AccumulationKind()  # Accumulation behaviour of a reading over time, usually 'measuringPeriod', to be used with individual endpoints (as opposed to 'macroPeriod' and 'aggregate' that are used to describe aggregations of data from individual endpoints).
        self.aggregate = AggregateKind()  # Salient attribute of the reading data aggregated from individual endpoints. This is mainly used to define a mathematical operation carried out over 'macroPeriod', but may also be used to describe an attribute of the data when the 'macroPeriod' is not defined.
        self.argument = RationalNumber()  # Argument used to introduce numbers into the unit of measure description where they are needed (e.g., 4 where the measure needs an argument such as CEMI(n=4)). Most arguments used in practice however will be integers (i.e., 'denominator'=1). Value 0 in 'numerator' and 'denominator' means not applicable.
        self.commodity = CommodityKind()  # Commodity being measured.
        self.consumption_tier = 0  # In case of common flat-rate pricing for power, in which all purchases are at a given rate, 'consumptionTier'=0. Otherwise, the value indicates the consumption tier, which can be used in conjunction with TOU or CPP pricing.
        self.cpp = 0  # Critical peak period (CPP) bucket the reading value is attributed to. Value 0 means not applicable.
        self.currency = Currency()  # Metering-specific currency.
        self.flow_direction = FlowDirectionKind.forward  # Flow direction for a reading where the direction of flow of the commodity is important (for electricity measurements this includes current, energy, power, and demand).
        self.interharmonic = ReadingInterharmonic()  # Indication of a "harmonic" or "interharmonic" basis for the measurement. Value 0 in 'numerator' and 'denominator' means not applicable.
        self.macro_period = MacroPeriodKind.SPECIFIED_PERIOD  # Time period of interest that reflects how the reading is viewed or captured over a long period of time.
        self.measurement_kind = MeasurementKind.none  # Identifies "what" is being measured, as refinement of 'commodity'. When combined with 'unit', it provides detail to the unit of measure.
        self.measuring_period = MeasuringPeriodKind.none  # Time attribute inherent or fundamental to the reading value (as opposed to 'macroPeriod' that supplies an "adjective" to describe aspects of a time period with regard to the measurement).
        self.multiplier = UnitMultiplier.none  # Metering-specific multiplier.
        self.phases = PhaseCode()  # Metering-specific phase code.
        self.tou = 0  # Time of use (TOU) bucket the reading value is attributed to. Value 0 means not applicable.
        self.unit = UnitSymbol.none  # Metering-specific unit.
        self.channel = Channel()  # Channel reporting/collecting register values with this type information.