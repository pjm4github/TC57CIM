# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# procedure_kind.py

from enum import Enum

class ProcedureKind(Enum):
    # Inspection procedure.
    INSPECTION = 1

    # Diagnosis procedure.
    DIAGNOSIS = 2

    # Maintenance procedure.
    MAINTENANCE = 3
    
    # Test procedure.
    TEST = 4
    
    # Other procedure.
    OTHER = 5
