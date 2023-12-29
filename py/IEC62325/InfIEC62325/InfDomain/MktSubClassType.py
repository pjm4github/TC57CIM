# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum

class MktSubClassType(Enum):
    forecasted_udc_direct_access_load = 1
    day_ahead_rmr = 2
    ten_min_expost_market_info = 3
    day_ahead_interim_market_info = 4
    day_ahead_final_market_info = 5
    ttc_atc_forecast_information = 6
    ttc_atc_hourly_forecast = 7
    branch_group_derates = 8
    hour_ahead_market_info = 9
    hourly_expost_market_info = 10
    public_bid_data = 11
    day_ahead_forecast_information = 12
