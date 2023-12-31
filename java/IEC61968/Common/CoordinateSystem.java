package IEC61968.Common;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Coordinate reference system.
 * @created 25-Dec-2023 8:45:20 PM
 */
public class CoordinateSystem extends IdentifiedObject {

	/**
	 * A Uniform Resource Name (URN) for the coordinate reference system (crs) used to
	 * define 'Location.PositionPoints'.
	 * An example would be the European Petroleum Survey Group (EPSG) code for a
	 * coordinate reference system, defined in URN under the Open Geospatial
	 * Consortium (OGC) namespace as: urn:ogc:def:uom:EPSG::XXXX, where XXXX is an
	 * EPSG code (a full list of codes can be found at the EPSG Registry web site http:
	 * //www.epsg-registry.org/). To define the coordinate system as being WGS84
	 * (latitude, longitude) using an EPSG OGC, this attribute would be urn:ogc:def:
	 * uom:EPSG::4236.
	 * A profile should limit this code to a set of allowed URNs agreed to by all
	 * sending and receiving parties.
	 */
	public String crsUrn;

	public CoordinateSystem(){

	}
}//end CoordinateSystem