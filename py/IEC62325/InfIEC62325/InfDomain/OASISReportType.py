# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum

class OASISReportType(Enum):
    AS_DA_RESULT = 0
    AS_OP_RSRV = 1
    AS_REQ = 2
    AS_RTM_RESULT = 3
    BIDS_PUBLIC = 4
    CMMT_RA_MLC = 5
    CMMT_RMR = 6
    CRR_CLEARING = 7
    CRR_INVENTORY = 8
    ENE_EA = 9
    ENE_HASP = 10
    ENE_IFM = 11
    ENE_MPM = 12
    ENE_RTM = 13
    ENE_RUC = 14
    LOSS_DA_HASP = 15
    LOSS_RTM = 16
    PRC_AS = 17
    PRC_FUEL = 18
    PRC_HRLY_LMP = 19
    PRC_INTVL_LMP = 20
    PRC_CNSTR = 21
    SLD_FCST = 22
    SLD_FCST_PEAK = 23
    SLD_MKTS = 24
    TRNS_ATC = 25
    TRNS_OUTAGE = 26
    TRNS_USAGE = 27
