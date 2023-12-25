"""
The domain package define primitive datatypes that are used by classes in other packages.
Stereotypes are used to describe the datatypes. The following stereotypes are defined:
<<enumeration>> A list of permissible constant values.
<<Primitive>> The most basic data types used to compose all other data types.
<<CIMDatatype>> A datatype that contains a value attribute, an optional unit of measure and a unit multiplier.
The unit and multiplier may be specified as a static variable initialized to the allowed value.
<<Compound>> A composite of Primitive, enumeration, CIMDatatype or othe Compound classes, as long as the
Compound classes do not recurse.

"""