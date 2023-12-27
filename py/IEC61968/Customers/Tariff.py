# Tariff.py
from IEC61968.Common.Document import Document
from IEC61970.Base.Domain.Date import Date


class Tariff(Document):
    def __init__(self):
        super().__init__()
        self.end_date = Date()
        self.start_date = Date()
        self.tariff_profiles = TariffProfile()
