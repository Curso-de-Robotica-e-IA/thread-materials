from enum import Enum, auto

class RobotStatus(Enum):
    START = auto()
    STOP = auto()
    PAUSE = auto()

class RobotType(Enum):
    KINOVA = auto()
    NIRYO = auto()

