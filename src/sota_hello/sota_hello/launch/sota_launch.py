from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        Node(
            package="sota_hello",
            executable="talker",
            output="screen",
            parameters=[{"message": LaunchConfiguration("speech_text")}],
        ),
        Node(
            package="sota_hello",
            executable="talker",
            output="screen",
            parameters=[{"message": LaunchConfiguration("speech_text")}],
        ),
    )
