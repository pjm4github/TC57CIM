from IEC61970.Base.Contingency.ContingencyElement import ContingencyElement
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Contingency(IdentifiedObject):
    """
    * An event threatening system reliability, consisting of one or more contingency
    * elements.
    * @created 29-Dec-2023 1:45:04 PM
    """
    def __init__(self):
        # Set true if must study this contingency.
        super().__init__()
        self.must_study = False

        # A contingency can have any number of contingency elements.
        self.contingency_element = [ContingencyElement()]
