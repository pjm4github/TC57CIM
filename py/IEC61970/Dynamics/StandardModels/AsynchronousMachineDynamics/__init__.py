__description__ = """
An asynchronous machine model represents a (induction) generator or motor with no external connection to the rotor windings, e.g., squirrel-cage induction machine. 

The interconnection with the electrical network equations may differ among simulation tools.  The program only needs to know the terminal to which this asynchronous machine is connected in order to establish the correct interconnection.  The interconnection with motor’s equipment could also differ due to input and output signals required by standard models.

The asynchronous machine model is used to model wind generators Type 1 and Type 2.  For these, normal practice is to include the rotor flux transients and neglect the stator flux transients.
"""