from IEC61970.Base.Domain.Date import Date


class GenericDataSetVersion:
    """
    Author: SELAOST1
    Version: 1.0
    Created: 22-Dec-2023 4:59:45 PM
    """
    def __init__(self):
        self.major_version = "2016"  # The universal CIM version name describing a consistent set of packages
        self.minor_version = "01"  # Describe minor updates and error corrections
        self.published = Date()  # The date when the complete CIM canonical model is published
