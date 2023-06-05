"""
This module contains all enums used in the system.
"""
from enum import Enum, auto


class RobotStatus(Enum):
    START = auto()
    STOP = auto()
    PAUSE = auto()


class RobotType(Enum):
    KINOVA = auto()
    NIRYO = auto()


class ExecutionStatus(Enum):
    RUNNING = auto()
    IDLE = auto()
    PAUSED = auto()
    STOPPED = auto()
    ERROR = auto()


class ActionCommand(Enum):
    PAUSE = auto()
    STOP = auto()
    FLUSH_ERROR = auto()


class MoveType(Enum):
    JOINT = auto()
    CARTESIAN = auto()
