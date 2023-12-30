from datetime import date


# Date as "yyyy-mm-dd", which conforms with ISO 8601. UTC time zone is specified as "yyyy-mm-ddZ".
# A local timezone relative UTC is specified as "yyyy-mm-dd(+/-)hh:mm".

class Date(date):
    def __init__(self, value=None, **kwargs):
        super().__init__(**kwargs)
        self.value = value  # "yyyy-mm-dd"