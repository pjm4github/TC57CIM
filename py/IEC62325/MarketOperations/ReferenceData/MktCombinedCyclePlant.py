# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Local import
from IEC61970.Base.Generation.Production.CombinedCyclePlant import CombinedCyclePlant

# Subclass of Production: CombinedCyclePlant from IEC61970 package.
# A set of combustion turbines and steam turbines where the exhaust heat from the
# combustion turbines is recovered to make steam for the steam turbines,
# resulting in greater overall plant efficiency.
# @author mspivbe2
# @version 1.0
# @created 25-Dec-2023 9:21:22 PM
class MktCombinedCyclePlant(CombinedCyclePlant):
    def __init__(self):
        super().__init__()
