package PackageDependencies;

import IEC61970.Base.Domain.Date;
import IEC61970.Base.Domain.String;

/**
 * The version of dependencies description among top level subpackages of the
 * combined CIM model.  This is not the same as the combined packages version.
 * @author kdd
 * @version 1.0
 * @created 02-Jan-2024 9:48:24 PM
 */
public class PackageDependenciesCIMVersion {

	/**
	 * Date of last change to the main package dependencies in format YYYY-MM-DD.
	 * This is updated when the version attribute is updated.
	 */
	public static final Date date = 2017-02-14;
	/**
	 * The version of the main subpackages of the combined CIM model.  The format is
	 * simply an integer.  The version (and date) initial values should be updated any
	 * time the dependencies in the model change and require an actual change to the
	 * diagrams within this package.
	 */
	public static final String version = 8;

	public PackageDependenciesCIMVersion(){

	}
}//end PackageDependenciesCIMVersion