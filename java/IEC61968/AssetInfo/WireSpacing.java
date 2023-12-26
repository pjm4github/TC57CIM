package IEC61968.AssetInfo;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Length;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.Assets.Structure;
import IEC61968.Assets.DuctBank;

/**
 * Wire spacing data that associates multiple wire positions with the line segment,
 * and allows to calculate line segment impedances. Number of phases can be
 * derived from the number of associated wire positions whose phase is not neutral.
 * 
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:26 PM
 */
public class WireSpacing extends IdentifiedObject {

	/**
	 * If true, this spacing data describes a cable.
	 */
	public Boolean isCable;
	/**
	 * Number of wire sub-conductors in the symmetrical bundle (typically between 1
	 * and 4).
	 */
	public Integer phaseWireCount;
	/**
	 * Distance between wire sub-conductors in a symmetrical bundle.
	 */
	public Length phaseWireSpacing;
	/**
	 * Usage of the associated wires.
	 */
	public WireUsageKind usage;
	/**
	 * All positions of single wires (phase or neutral) making the conductor.
	 */
	public WirePosition WirePositions;
	public Structure Structures;
	public DuctBank DuctBank;

	public WireSpacing(){

	}
}//end WireSpacing