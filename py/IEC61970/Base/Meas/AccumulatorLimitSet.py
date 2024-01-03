# package IEC61970.Base.Meas;
#
#
# /**
#  * An AccumulatorLimitSet specifies a set of Limits that are associated with an
#  * Accumulator measurement.
#  * @created 03-Jan-2024 4:15:43 PM
#  */
# public class AccumulatorLimitSet extends LimitSet {
#
# 	/**
# 	 * The limit values used for supervision of Measurements.
# 	 */
# 	public AccumulatorLimit Limits;
#
# 	public AccumulatorLimitSet(){
#
# 	}
# }//end AccumulatorLimitSet
from IEC61970.Base.Meas.LimitSet import LimitSet
from IEC61970.Base.Meas.AccumulatorLimit import AccumulatorLimit


class AccumulatorLimitSet(LimitSet):
    def __init__(self):
        super().__init__()
        self.limits = AccumulatorLimit()  # The limit values used for supervision of Measurements