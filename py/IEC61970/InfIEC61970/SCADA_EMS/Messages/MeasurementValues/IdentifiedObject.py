class IdentifiedObject:
    """
    Author: selaost1
    Version: 1.0
    Created: 25-Dec-2023 8:31:59 PM
    """
    def __init__(self):
        # Master resource identifier issued by a model authority. The mRID is unique
        # within an exchange context. Global uniqueness is easily achieved by using a
        # UUID,  as specified in RFC 4122, for the mRID. The use of UUID is strongly
        # recommended.
        # For CIMXML data files in RDF syntax conforming to IEC 61970-552 Edition 1, the
        # mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object
        # elements.

        self.mrid = ""  # Master resource identifier, unique within an exchange context
