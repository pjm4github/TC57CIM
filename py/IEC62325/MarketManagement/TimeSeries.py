# ///////////////////////////////////////////////////////////
# //  TimeSeries.h
# //  Implementation of the Class TimeSeries
# //  Created on:      26-Dec-2023 8:08:10 PM
# ///////////////////////////////////////////////////////////
#
# #if !defined(EA_4589CED0_A0EA_45ac_B312_13137BD0AD35__INCLUDED_)
# #define EA_4589CED0_A0EA_45ac_B312_13137BD0AD35__INCLUDED_
#

#
# /**
#  * A set of regular time-ordered measurements or values of quantitative nature of
#  * an individual or collective phenomenon taken at successive, in most cases
#  * equidistant, periods / points of time.
#  */
# class TimeSeries : public IdentifiedObject
# {
#
# public:
# 	TimeSeries();
# 	/**
# 	 * The identification of the nature of the time series.
# 	 */
# 	String businessType;
# 	/**
# 	 * An indicator stating that the TimeSeries, identified by the mRID, is cancelled
# 	 * as well as all the values sent in a previous version of the TimeSeries in a
# 	 * previous document.
# 	 */
# 	String cancelledTS;
# 	/**
# 	 * The coded representation of the type of curve being described.
# 	 */
# 	String curveType;
# 	/**
# 	 * Identification of the object that is the common denominator used to aggregate a
# 	 * time series.
# 	 */
# 	String objectAggregation;
# 	/**
# 	 * The type of the product such as Power, energy, reactive power, transport
# 	 * capacity that is the subject of the time series.
# 	 */
# 	String product;
# 	/**
# 	 * Version of the time series.
# 	 */
# 	String version;
# 	Reason *Reason;
# 	MarketEvaluationPoint *MarketEvaluationPoint;
# 	MarketDocument *MarketDocument;
# 	Period *Period;
# 	FlowDirection *FlowDirection;
# 	Domain *Domain;
# 	DateAndOrTime *DateAndOrTime;
# 	EnvironmentalMonitoringStation *EnvironmentalMonitoringStation;
# 	MarketParticipant *MarketParticipant;
#
# };
# #endif // !defined(EA_4589CED0_A0EA_45ac_B312_13137BD0AD35__INCLUDED_)
#
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketManagement.Reason import Reason
from IEC62325.MarketManagement.MarketDocument import MarketDocument

from IEC62325.MarketManagement.Period import Period
from IEC62325.MarketManagement.FlowDirection import FlowDirection
from IEC62325.MarketManagement.Domain import Domain
from IEC62325.MarketManagement.DateAndOrTime import DateAndOrTime
from IEC62325.MarketCommon.EnvironmentalMonitoringStation import EnvironmentalMonitoringStation
from IEC62325.MarketCommon.MarketParticipant import MarketParticipant



class TimeSeries(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.business_type = ""  # The identification of the nature of the time series.
        self.cancelled_ts = ""  # An indicator stating that the TimeSeries, identified by the mRID, is cancelled as well as all the values sent in a previous version of the TimeSeries in a previous document.
        self.curve_type = ""  # The coded representation of the type of curve being described.
        self.object_aggregation = ""  # Identification of the object that is the common denominator used to aggregate a time series.
        self.product = ""  # The type of the product such as Power, energy, reactive power, transport capacity that is the subject of the time series.
        self.version = ""  # Version of the time series.
        self.reason = Reason()  # Reason
        self.market_evaluation_point = MarketEvaluationPoint()  # MarketEvaluationPoint
        self.market_document = MarketDocument()  # MarketDocument
        self.period = Period()  # Period
        self.flow_direction = FlowDirection()  # FlowDirection
        self.domain = Domain()  # Domain
        self.date_and_or_time = DateAndOrTime()  # DateAndOrTime
        self.environmental_monitoring_station = EnvironmentalMonitoringStation()  # EnvironmentalMonitoringStation
        self.market_participant = MarketParticipant()  # MarketParticipant
