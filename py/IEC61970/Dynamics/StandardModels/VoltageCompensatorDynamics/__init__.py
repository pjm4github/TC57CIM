__description__ = """
Synchronous machine terminal voltage transducer and current compensator models adjust the terminal voltage feedback to the excitation system by adding a quantity that is proportional to the terminal current of the generator.  It is linked to a specific generator (synchronous machine).

Several types of compensation are available on most excitation systems. Synchronous machine active and reactive current compensation are the most common. Either reactive droop compensation and/or line-drop compensation may be used, simulating an impedance drop and effectively regulating at some point other than the terminals of the machine. The impedance or range of adjustment and type of compensation should be specified for different types. 

Care must be taken to ensure that a consistent pu system is utilized for the compensator parameters and the synchronous machine current base.

For further information see IEEE Standard 421.5-2005, Section 4.

"""