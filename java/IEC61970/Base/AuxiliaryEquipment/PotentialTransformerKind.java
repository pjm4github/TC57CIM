package TC57CIM.IEC61970.Base.AuxiliaryEquipment;

import TC57CIM.IEC61970.Base.Domain.Float;

/**
 * The construction kind of the potential transformer.
 * @author kdemaree
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public enum PotentialTransformerKind {
	/**
	 * The potential transformer is using induction coils to create secondary voltage.
	 */
	inductive,
	/**
	 * The potential transformer is using capacitive coupling to create secondary
	 * voltage.
	 */
	capacitiveCoupling
}