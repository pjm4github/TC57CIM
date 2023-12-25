package TC57CIM.IEC61970.Base.Core;

import TC57CIM.IEC61970.Base.Domain.Frequency;

/**
 * The class describe a base frequency for a power system network. In case of
 * multiple power networks with different frequencies, e.g. 50 or 60 Hertz each
 * network will have it's own base frequency class. Hence it is assumed that power
 * system objects having different base frequencies appear in separate documents
 * where each document has a single base frequency instance.
 * @author SELAOST1
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class BaseFrequency extends IdentifiedObject {

	/**
	 * The base frequency.
	 */
	public Frequency frequency;

	public BaseFrequency(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}