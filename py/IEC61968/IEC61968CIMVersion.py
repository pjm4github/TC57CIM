from IEC61970.Base.Domain.Date import Date


class IEC61968CIMVersion:
    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date = Date("2017-06-11")

    # Form is IEC61968CIMXXvYY where XX is the major CIM package version and the YY is the minor version.
    # For example IEC61968CIM10v17.
    version = "IEC61968CIM13v11"

