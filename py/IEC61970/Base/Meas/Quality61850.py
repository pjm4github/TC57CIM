# quality_61850.py
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.Validity import Validity
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.SCADA.Source import Source


class Quality61850:
    def __init__(self):
        # Measurement value may be incorrect due to a reference being out of calibration.
        self.bad_reference = False

        # Value has been replaced by State Estimator. estimator_replaced is not an
        # IEC61850 quality bit but has been put in this class for convenience.
        self.estimator_replaced = False

        # This identifier indicates that a supervision function has detected an internal
        # or external failure, e.g. communication failure.
        self.failure = False

        # Measurement value is old and possibly invalid, as it has not been successfully
        # updated during a specified time interval.
        self.old_data = False

        # Measurement value is blocked and hence unavailable for transmission.
        self.operator_blocked = False

        # To prevent some overload of the communication it is sensible to detect and
        # suppress oscillating (fast changing) binary inputs. If a signal changes in a
        # defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0)
        # then oscillation is detected and the detail quality identifier "oscillatory" is
        # set. If it is detected a configured numbers of transient changes could be
        # passed by. In this time the validity status "questionable" is set. If after
        # this defined numbers of changes the signal is still in the oscillating state
        # the value shall be set either to the opposite state of the previous stable
        # value or to a defined default value. In this case the validity status
        # "questionable" is reset and "invalid" is set as long as the signal is
        # oscillating. If it is configured such that no transient changes should be
        # passed by then the validity status "invalid" is set immediately in addition to
        # the detail quality identifier "oscillatory" (used for status information only).
        self.oscillatory = False

        # Measurement value is beyond a predefined range of value.
        self.out_of_range = False

        # Measurement value is beyond the capability of being represented properly. For
        # example, a counter value overflows from maximum count back to a value of zero.
        self.overflow = False

        # Source gives information related to the origin of a value. The value may be
        # acquired from the process, defaulted or substituted.
        self.source = Source()

        # A correlation function has detected that the value is not consistent with other
        # values. Typically set by a network State Estimator.
        self.suspect = False

        # Measurement value is transmitted for test purposes.
        self.test = False

        # Validity of the measurement value.
        self.validity = Validity()

