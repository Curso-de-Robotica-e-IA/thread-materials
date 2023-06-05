from utils.constants import RobotStatus
from robot_provider.robot_provider import RobotProvider
from robot_provider.robot_execution_context import RobotContext, ActionCommand, ExecutionStatus


class RobotCtrl:

    def __init__(self):
        self.status: RobotStatus = RobotStatus.STOP
        self.__robotProvider = RobotProvider('gen3')
        self.__robotStatus = RobotContext.get_execution_status()

    def move(self, command: list):
        RobotContext.reset_action_command()
        RobotContext.enqueue_command(command)
        if not RobotContext.is_connected():
            self.connect()

        if RobotContext.get_execution_status() != ExecutionStatus.RUNNING:
            self.__robotProvider.run_commands()

    def stop(self):
        RobotContext.set_action_command(ActionCommand.STOP)

    def get_status(self):
        return RobotContext.get_execution_status()

    def pause(self):
        RobotContext.set_action_command(ActionCommand.PAUSE)

    def resume(self):
        RobotContext.reset_action_command()
        if RobotContext.get_execution_status() != ExecutionStatus.RUNNING:
            self.__robotProvider.run_commands()

    def connect(self):
        self.__robotProvider.connect_robot()

    def disconnect(self):
        self.__robotProvider.disconnect_robot()

    def update_status(self):
        """
        Triggers an update flag to update robot status at interface
        """
        self.__robotStatus = RobotContext.get_execution_status()
