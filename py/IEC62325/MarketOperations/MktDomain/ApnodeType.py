from enum import Enum


class ApnodeType(Enum):
	"""
	Aggregate Node Types for example:
	AG -  Aggregated Generation
	CPZ -  Custom Price Zone
	DPZ -  Default Price Zone
	LAP - Load Aggregation Point
	TH -  Trading  Hub
	SYS - System Zone
	CA - Control Area
	
	GA - generic aggregation
	EHV - 500 kV
	GH - generic hub
	ZN - zone
	INT - Interface
	BUS - Bus
	@created 28-Dec-2023 3:05:37 PM
	"""

	# Aggregated Generation
	AG = 1

	# Custom Price Zone
	CPZ = 2

	# Default Price Zone
	DPZ = 3

	# Trading  Hub
	TH = 4

	# System Zone
	SYS = 5

	# Control Area
	CA = 6

	# Designated Congestion Area
	DCA = 7

	# generic aggregation
	GA = 8

	# generic hub
	GH = 9

	# 500 kV - Extra High Voltage aggregate price nodes
	EHV = 10

	# Zone
	ZN = 11

	# Interface
	INT = 12

	# Bus
	BUS = 13
