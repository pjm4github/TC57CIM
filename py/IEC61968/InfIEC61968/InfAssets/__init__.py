__description__ = """
The package is used to define asset-level models for objects. Assets may be comprised of other assets and may have 
relationships to other assets. Assets also have owners and values. Assets may also have a relationship to a 
PowerSystemResource in the Wires model.

TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we 
store the knowledge here to reuse later:
"Assets are the basic units which define a physical infrastructure. PowerSystemResources are logical objects meaningful
to operations which are constructed from one or more Assets, although PowerSystemResources are not required to
specifiy their component Assets.
The Asset package is comprosed of several packages. The key concepts of an Asset are as follows:
Assets can have names, through inheritance to the Naming package
Assets are physical entities which have a lifecycle
One or more assets can be associated to create a PowerSystemResource
Assets can be grouped (aggregated) with other Assets
Assets are typically either 'point' or 'linear' assets, which relate to physical geometry
Assets have a close relationship to Work as a consequence of their lifecycle
The following sections describe the packages in the Assets package.
The AssetBasics package defines the relationship between Asset and other classes, such as Organization, 
PowerSystemResource and Document.
Point assets are those assets whose physical location can be described in terms of a single coordinate, 
such as a pole or a switch.
Linear assets are those assets whose physical location is best described in terms of a line, plyline or polygon.
Asset work triggers are used to determine when inspection and/or maintenance are required for assets".


"""