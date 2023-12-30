from IEC61970.Base.Domain.Date import Date


class IEC62325CIMVersion:
    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date = Date("2017-09-28")

    # Form is IEC62325CIMXXvYY where XX is the major CIM package version and the YY is the minor version.
    # For example IEC62325CIM10v03.
    version = "IEC62325CIM03v17"
