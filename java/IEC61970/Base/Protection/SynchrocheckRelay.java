package IEC61970.Base.Protection;

import IEC61970.Base.Domain.AngleRadians;
import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.Voltage;

/**
 * A device that operates when two AC circuits are within the desired limits of
 * frequency, phase angle, and voltage, to permit or to cause the paralleling of
 * these two circuits. Used to prevent the paralleling of non-synchronous
 * topological islands.
 * @created 25-Dec-2023 8:32:03 PM
 */
public class SynchrocheckRelay extends ProtectionEquipment {

	/**
	 * The maximum allowable voltage vector phase angle difference across the open
	 * device.
	 */
	public AngleRadians maxAngleDiff;
	/**
	 * The maximum allowable frequency difference across the open device.
	 */
	public Frequency maxFreqDiff;
	/**
	 * The maximum allowable difference voltage across the open device.
	 */
	public Voltage maxVoltDiff;

	public SynchrocheckRelay(){

	}
}//end SynchrocheckRelay