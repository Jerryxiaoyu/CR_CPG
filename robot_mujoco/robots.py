"""
Module for wrappers of robot specific classes
"""

from abc import ABCMeta, abstractmethod, abstractproperty

class Robot:
    """
    Abstract class for robot specific functions
    """

    # This class cannot be instantiated but must be inherited by a class that provides implementation of the methods
    # and values for the properties
    __metaclass__ = ABCMeta

    def __init__(self):
        """
        The constructor of the abstract class
        """
        pass

    @abstractmethod
    def sync_sleep_time(self):
        """
        Time to sleep to allow the joints to reach their targets
        """
        pass

    @abstractmethod
    def robot_handle(self):
        """
        Stores the handle to the robot
        This handle is used to invoke methods on the robot
        """
        pass

    @abstractmethod
    def interpolation(self):
        """
        Flag to indicate if intermediate joint angles should be interpolated
        """
        pass

    @abstractmethod
    def fraction_max_speed(self):
        """
        Fraction of the maximum motor speed to use
        """
        pass

    @abstractmethod
    def wait(self):
        """
        Flag to indicate whether the control should wait for each angle to reach its target
        """
        pass

    @abstractmethod
    def set_angles(self, joint_angles, duration=None, joint_velocities=None):
        """
        Sets the joints to the specified angles

        :type joint_angles: dict
        :param joint_angles: Dictionary of joint_names: angles (in radians)
        :type duration: float
        :param duration: Time to reach the angular targets (in seconds)
        :type joint_velocities: dict
        :param joint_velocities: dict of joint angles and velocities
        :return: None
        """
        pass

    @abstractmethod
    def get_angles(self, joint_names):
        """
        Gets the angles of the specified joints and returns a dict of joint_names: angles (in radians)

        :type joint_names: list(str)
        :param joint_names: List of joint names
        :rtype: dict
        """
        pass
 
