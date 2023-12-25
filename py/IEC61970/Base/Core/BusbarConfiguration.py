from enum import Enum


class BusbarConfiguration(Enum):
	"""
	Busbar layout for bay.
	"""
	# * Single bus.
	SINGLE_BUS = 1
	# * Double bus.
	DOUBLE_BUS = 2
	# * Main bus with transfer bus.
	MAIN_WITH_TRANSFER = 3
	# * Ring bus.
	RING_BUS = 4
