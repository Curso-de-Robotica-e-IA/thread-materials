from dataclasses import dataclass
from utils.constants import MoveType


@dataclass
class RobotJointCommand:
    """
    This class is a data class that represents a robot joint command.
    """
    type: MoveType = MoveType.JOINT
    joint_1: float = 0
    joint_2: float = 0
    joint_3: float = 0
    joint_4: float = 0
    joint_5: float = 0
    joint_6: float = 0

    def __init__(self, j1, j2, j3, j4, j5, j6):
        self.joint_1 = j1
        self.joint_2 = j2
        self.joint_3 = j3
        self.joint_4 = j4
        self.joint_5 = j5
        self.joint_6 = j6
