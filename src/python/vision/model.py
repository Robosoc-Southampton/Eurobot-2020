
from typing import List
from enum import Enum
from worldmodel.position import BoardPosition


class CupColour(Enum):
	GREEN = 0
	RED = 1


class CupModel:
	def __init__(self, colour: CupColour, position: BoardPosition):
		self.colour = colour
		self.position = position


class RobotModel:
	def __init__(self, id: int, position: BoardPosition):
		self.id = id
		self.position = position


class VisionModel:
	def __init__(self, cups: List[CupModel] = [], robots: List[RobotModel] = [], side: CupColour):
		self.cups = cups # list of cups detected
		self.robots = robots # list of robots detected
		self.side = side # side of the board we're playing on
