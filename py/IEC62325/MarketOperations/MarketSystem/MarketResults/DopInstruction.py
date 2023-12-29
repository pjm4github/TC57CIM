# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime


class DopInstruction:
    '''
    Provides the necessary information (on a resource basis) to capture the
    Dispatch Operating Point (DOP) results on a Dispatch interval. This
    information is only relevant to the RT interval market.
    '''

    def __init__(self) -> None:
        '''
        Dispatched Operating Point (MW)
        '''
        self.mw_dop: float = 0.0
        
        '''
        A value used to establish priority of the DOP when plotting.  This is only
        applicable when two DOPs exist for the same time, but with different MW values.
        E.g. when indicating a step in the curve.  Its used to determine if the curve
        steps up or down.
        '''
        self.plot_priority: str = ""
        
        '''
        Indication of DOP validity. 
        Shows the DOP is calculated from the latest run (YES). A NO indicator shows
        that the DOP is copied from a previous execution.
        Up to 2 intervals can be missed.
        '''
        self.run_indicator_dop: str = ""
        
        '''
        DOP time stamp
        '''
        self.timestamp_dop: DateTime = DateTime()
        self.update_timestamp: DateTime = DateTime()
        self.update_type: str = ""
        self.update_user: str = ""
