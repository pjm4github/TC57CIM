package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.String;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * A registered resource that represents a distributed energy resource, such as a
 * micro-generator, fuel cell, photo-voltaic energy source, etc.
 * @author mwald
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class RegisteredDistributedResource extends RegisteredResource {

	/**
	 * The type of resource. Examples include: fuel cell, flywheel, photovoltaic,
	 * micro-turbine, CHP (combined heat power), V2G (vehicle to grid), DES
	 * (distributed energy storage), and others.
	 */
	public String distributedResourceType;

	public RegisteredDistributedResource(){

	}
}//end RegisteredDistributedResource