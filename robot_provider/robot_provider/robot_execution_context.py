from collections import deque
from enum import Enum, auto
from threading import Lock
from dataclasses import dataclass

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
@dataclass
class RobotJointCommand():
    type:MoveType = MoveType.JOINT
    joint1:float
    joint2:float
    joint3:float
    joint4:float
    joint5:float
    joint6:float

@dataclass
class RobotCartesianCommand():
    type:MoveType = MoveType.CARTESIAN
    x:float
    y:float
    z:float
    rx:float
    ry:float
    rz:float
    
class RobotExecutionContext():
    def __init__(self) -> None:
        self.__command_queue = deque()
        self.__execution_status = ExecutionStatus.IDLE
        self.__conected = False
        self.__action_command = None
        self.__mutex = Lock()
    
    def enqueue_command(self, command) -> None:
        with self.__mutex:
            self.__command_queue += command

    def dequeue_command(self):
        with self.__mutex:
            if len(self.__command_queue) > 0:
                element = self.__command_queue.popleft()
                return element
    
    def clean_commands(self):
        with self.__mutex:
            self.__command_queue.clear()

    def get_execution_status(self):
        with self.__mutex:
            element = self.__execution_status
            return element
    
    def set_execution_status(self, execution_status:ExecutionStatus):
        with self.__mutex:
            self.__execution_status = execution_status

    def get_reset_action_command(self):
        with self.__mutex:
            element = self.__action_command
            self.__action_command = None
            return element
    
    def get_action_command(self):
        with self.__mutex:
            element = self.__action_command
            return element
    
    def set_action_command(self, action_command:ActionCommand):
        with self.__mutex:
            self.__action_command = action_command

    def reset_action_command(self):
        with self.__mutex:
            self.__action_command = None

    def is_connected(self):
        with self.__mutex:
            element = self.__conected
            return element
        
        return False
    
    def set_connected(self, connected):
        with self.__mutex:
            self.__conected = connected


RobotContext = RobotExecutionContext()