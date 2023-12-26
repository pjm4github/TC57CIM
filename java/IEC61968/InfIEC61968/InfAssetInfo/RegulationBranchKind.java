package IEC61968.InfIEC61968.InfAssetInfo;


/**
 * Kind of regulation branch for shunt impedance.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public enum RegulationBranchKind {
	line,
	transformer,
	switch,
	breaker,
	recloser,
	fuse,
	sectionner,
	other
}