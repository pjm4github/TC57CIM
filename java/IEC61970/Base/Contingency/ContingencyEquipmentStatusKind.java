package TC57CIM.IEC61970.Base.Contingency;


/**
 * Indicates the state which the contingency equipment is to be in when the
 * contingency is applied.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public enum ContingencyEquipmentStatusKind {
	/**
	 * The equipment is to be put into service.
	 */
	inService,
	/**
	 * The equipment is to be taken out of service.
	 */
	outOfService
}