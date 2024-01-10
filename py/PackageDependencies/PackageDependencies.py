from IEC61970.Base.Domain.Date import Date


class PackageDependenciesCIMVersion:
    """
    The version of dependencies description among top level subpackages of the
    combined CIM model. This is not the same as the combined packages version.
    Author: kdd
    Version: 1.0
    Created: 02-Jan-2024 9:48:24 PM
    """
    date = Date("2017-02-14")  # Date of last change to the main package dependencies
    version = "8"  # The version of the main subpackages of the combined CIM model
