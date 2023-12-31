package IEC61970.Base.Core;

import IEC61970.Base.Domain.PerCent;

/**
 * Specifies the operations contract relationship between a power system resource
 * and a contract participant.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class OperatingShare {

	/**
	 * Percentage operational ownership between the pair (power system resource and
	 * operatging participant) associated with this share. The total percentage
	 * ownership for a power system resource should add to 100%.
	 */
	public PerCent percentage;
	/**
	 * The operating participant having this share with the associated power system
	 * resource.
	 */
	public OperatingParticipant OperatingParticipant;
	/**
	 * The power system resource to which the share applies.
	 */
	public PowerSystemResource PowerSystemResource;

	public OperatingShare(){

	}
}//end OperatingShare