package IEC61970.Base.AuxiliaryEquipment;

import IEC61970.Base.Domain.Float;

/**
 * The construction kind of the potential transformer.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
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