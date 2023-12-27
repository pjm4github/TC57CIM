# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.Money import Money

class Due:
    def __init__(self):
        self.arrears = Money()
        self.charges = Money()
        self.current = Money()
        self.interest = Money()
        self.principle = Money()
