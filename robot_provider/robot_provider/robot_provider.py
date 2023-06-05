from robot_execution_context import RobotContext
from utils.constants import ExecutionStatus, ActionCommand, MoveType
from rria_api.robot_facade import *  # TODO: substituir pelo pyniryo
import sys
from concurrent.futures import ThreadPoolExecutor
from threading import Lock


class RobotProvider():
    def __init__(self, robot_name):
        # TODO: substituir pelo pyniryo 
        self.__robot = RobotObject('192.168.2.10', robot_name)

        self.__thread_pool = ThreadPoolExecutor(max_workers=1)
        self.__robot_mutex = Lock()

    def robot(self):
        with self.__robot_mutex:
            element = self.__robot
            return element

    def connect_robot(self):
        if RobotContext.get_execution_status() != ExecutionStatus.RUNNING:
            task = self.__thread_pool.submit(self.__connect_robot)
        else:
            print('robot running commands, stop to change connect')

    def __connect_robot(self):
        try:
            print('try connect')
            connected = self.robot().connect_robot()
            print(connected)
            RobotContext.set_connected(connected)
        except Exception as e:
            print(e)
            RobotContext.set_connected(False)

        sys.exit()

    def disconnect_robot(self):
        if RobotContext.get_execution_status() != ExecutionStatus.RUNNING:
            task = self.__thread_pool.submit(self.__disconnect_robot)
        else:
            print('robot running commands, stop to change connect')

    def __disconnect_robot(self):
        try:
            print('try disconnect')
            self.robot().disconnect_robot()
            RobotContext.set_connected(False)
        except Exception as e:
            print(e)

        sys.exit()

    def emergency_stop(self):
        pass

    def safety_restart(self):
        pass

    def flush_robot_error(self):
        pass

    def run_commands(self):
        task = self.__thread_pool.submit(self.__run_commands)

    def __run_commands(self):
        if not RobotContext.is_connected():
            print('robot connection not started')
            RobotContext.set_execution_status(ExecutionStatus.IDLE)
            return

        RobotContext.set_execution_status(ExecutionStatus.RUNNING)

        while True:
            actionCommand = RobotContext.get_reset_action_command()
            if actionCommand is not None:
                if actionCommand == ActionCommand.PAUSE:
                    RobotContext.set_execution_status(ExecutionStatus.PAUSED)
                    break
                elif actionCommand == ActionCommand.STOP:
                    RobotContext.set_execution_status(ExecutionStatus.STOPPED)
                    self.__robot.move_joints(0, 0, 0, 0, 0, 0)  # to home
                    RobotContext.clean_commands()
                    break
                elif actionCommand == ActionCommand.FLUSH_ERROR:
                    pass
                else:
                    print('action not supported on execution loop', actionCommand)

            command = RobotContext.dequeue_command()

            if command is None:
                RobotContext.set_execution_status(ExecutionStatus.IDLE)
                break
            else:
                RobotContext.set_execution_status(ExecutionStatus.RUNNING)
                print(command)
                if command.type == MoveType.JOINT:
                    print(command)
                    self.__robot.move_joints(command.joint1, command.joint2, command.joint3, command.joint4,
                                             command.joint5, command.joint6)
                elif command.type == MoveType.CARTESIAN:
                    print(command)
                    self.__robot.move_cartesian(command.x, command.y, command.z, command.rx, command.ry, command.rz)

        sys.exit()
