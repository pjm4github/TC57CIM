package IEC61968.Assets;


/**
 * How the failure has been isolated.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public enum FailureIsolationMethodKind {
	breakerOperation,
	fuse,
	burnedInTheClear,
	manuallyIsolated,
	other
}