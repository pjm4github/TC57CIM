# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023



class Time:
    """
    Time as "hh:mm:ss.sss", which conforms with ISO 8601. UTC time zone is
    specified as "hh:mm:ss.sssZ". A local timezone relative UTC is specified
    as "hh:mm:ss.sssh h:mm". The second component (shown here as "ss.sss") could
    have any number of digits in its fractional part to allow any kind of
    precision beyond seconds.
    @author kdemaree
    @version 1.0
    @created 15-Dec-2023 4:38:30 PM
    """

    def __init__(self) -> None:
        # Constructor
        self.value = 0.0

