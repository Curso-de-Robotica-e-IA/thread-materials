from dataclasses import dataclass
from utils.constants import MoveType


@dataclass
class RobotJointCommand():
    type:MoveType = MoveType.JOINT
    joint1:float = 0
    joint2:float = 0
    joint3:float = 0
    joint4:float = 0
    joint5:float = 0
    joint6:float = 0

    def __init__(self, j1, j2, j3, j4, j5, j6):
        self.joint1 = j1
        self.joint2 = j2
        self.joint3 = j3
        self.joint4 = j4
        self.joint5 = j5
        self.joint6 = j6
