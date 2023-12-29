# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC61970.Base.Domain.DateTime import DateTime


class TransmissionCapacity:
    def __init__(self):
        self.capacity_benefit_margin = 0.0  # Capacity Benefit Margin (CBM) is used by Markets to calculate the transmission interface limits. This number could be manually or procedurally determined. The CBM is defined per transmission interface (branch group).
        self.operational_transmission_capacity = 0.0  # The Operational Transmission Capacity (OTC) is the transmission capacity under the operating condition during a specific time period, incorporating the effects of derates and current settings of operation controls. The OTCs for all transmission interface (branch group) are always provided regardless of outage or switching conditions.
        self.otc15min_emergency = 0.0  # The Operational Transmission Capacity (OTC) 15 minute Emergency Limit
        self.otc_emergency = 0.0  # The Operational Transmission Capacity (OTC) Emergency Limit.
        self.pod = ""  # point of delivery
        self.por = ""  # point of receipt
        self.start_operating_date = DateTime()  # Operating date & hour when the entitlement applies
        self.total_transmission_capacity = 0.0  # Total Transmission Capacity