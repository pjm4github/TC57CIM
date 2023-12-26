package IEC61968.Metering;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A single path for the collection or reporting of register values over a period
 * of time. For example, a register which measures forward energy can have two
 * channels, one providing bulk quantity readings and the other providing interval
 * readings of a fixed interval size.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class Channel extends IdentifiedObject {

	/**
	 * If true, the data is being calculated by an enterprise system rather than
	 * metered directly.
	 */
	public Boolean isVirtual;

	public Channel(){

	}
}//end Channel