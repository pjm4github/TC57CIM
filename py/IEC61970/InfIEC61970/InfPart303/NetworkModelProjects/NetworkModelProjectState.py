from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class NetworkModelProjectState(IdentifiedObject):
    """
    A network model project version state. States are agreed upon by the exchange
    community. Examples are "approved", "proposed", "withdrawn", "committed" etc.
    Author: 222206
    Version: 1.0
    Created: 25-Dec-2023 8:32:00 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
