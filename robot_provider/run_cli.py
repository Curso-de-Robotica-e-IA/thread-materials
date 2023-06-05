from robot_ctrl import RobotCtrl
from packages.robot_cartesian_command import RobotCartesianCommand
from packages.robot_joint_command import RobotJointCommand


# in this module has an example using cli for interact with robot

def main():
    robot_controller = RobotCtrl()
    while True:
        tecla = input('Enter a command for using the robot arm: ')
        if tecla == 'c':
            robot_controller.connect()
        elif tecla == 'd':
            robot_controller.disconnect()
        elif tecla == 'mj':
            robot_controller.move([RobotJointCommand(0, 40, 0, 0, 0, 0), RobotJointCommand(0, -40, 0, 0, 0, 0),
                                   RobotJointCommand(30, 40, 0, 0, 0, 0)])
        elif tecla == 'mc':
            robot_controller.move([RobotCartesianCommand(0.2, 0.1, 0.3, 0.0, 0.5, 0.0)])
        elif tecla == 'mz':
            robot_controller.move([RobotJointCommand(0, 0, 0, 0, 0, 0)])
        elif tecla == 's':
            robot_controller.stop()
        elif tecla == 'p':
            robot_controller.pause()
        elif tecla == 'r':
            robot_controller.resume()
        elif tecla == 'g':
            robot_controller.get_status()
        elif tecla == 'q':
            break
