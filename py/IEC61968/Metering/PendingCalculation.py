from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.ReadingType import ReadingType


class PendingCalculation:
    def __init__(self):
        self.multiply_before_add = False  # Whether scalars should be applied before adding the 'offset'.
        self.offset = 0  # (if applicable) Offset to be added as well as multiplication using scalars.
        self.scalar_denominator = 0  # (if scalar is rational number) When 'IntervalReading.value' is multiplied by 'scalarNumerator' and divided by this value, it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'.
        self.scalar_float = 1.0  # (if scalar is floating number) When multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, according to the 'ReadingType.unit'.
        self.scalar_numerator = 0  # (if scalar is integer or rational number) When the scalar is a simple integer, and this attribute is presented alone and multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. It is never used in conjunction with 'scalarFloat', only with 'scalarDenominator'.
        self.ReadingType = ReadingType()  # Reading type resulting from this pending conversion.
