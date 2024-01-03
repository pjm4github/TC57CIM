# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from IEC61968.Assets.Streetlight import Streetlight
from IEC61968.Assets.Structure import Structure
from IEC61968.InfIEC61968.InfAssets.PoleBaseKind import PoleBaseKind
from IEC61968.InfIEC61968.InfAssets.PoleTreatmentKind import PoleTreatmentKind
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Length import Length



class Pole(Structure):
    def __init__(self):
        super().__init__()
        self.base_kind = PoleBaseKind.DIRT  # Kind of base for this pole
        self.breast_block = True  # True if a block of material has been attached to base of pole in ground for stability
        self.classification = ""  # Pole class
        self.construction = ""  # The framing structure mounted on the pole
        self.diameter = Length()  # Diameter of the pole
        self.jpa_reference = ""  # Joint pole agreement reference number
        self.length = Length()  # Length of the pole
        self.preservative_kind = PolePreservativeKind()  # Kind of preservative for this pole
        self.species_type = ""  # Pole species
        self.treated_date_time = DateTime()  # Date and time pole was last treated with preservative
        self.treatment_kind = PoleTreatmentKind()  # Kind of treatment for this pole
        self.streetlights = Streetlight()  # All streetlights attached to this pole
