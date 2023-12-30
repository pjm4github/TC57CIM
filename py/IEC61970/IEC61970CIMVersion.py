from IEC61970.Base.Domain.Date import Date


class IEC61970CIMVersion:
    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date = Date("2017-07-26")

    # Form is IEC61970CIMXXvYY where XX is the major CIM package version and the YY is the minor version.
    # For example IEC61970CIM13v18.
    version = "IEC61970CIM17v23"
