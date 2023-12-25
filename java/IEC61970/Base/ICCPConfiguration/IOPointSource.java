package TC57CIM.IEC61970.Base.ICCPConfiguration;

import TC57CIM.IEC61970.Base.Meas.IOPoint;
import TC57CIM.IEC61970.Base.Meas.MeasurementValueSource;

/**
 * Indicates the point source for an IO Point.
 * @author herb
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class IOPointSource extends MeasurementValueSource {

	public IOPoint IOPoint;

	public IOPointSource(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}