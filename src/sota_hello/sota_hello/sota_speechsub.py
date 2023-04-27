"""imports"""
import rclpy
import os
from rclpy.node import Node

from std_msgs.msg import String
from dotenv import load_dotenv
from .robot_modules.robottools import RobotTools

load_dotenv()


class SotaSubscriber(Node):
    """SotaSubscriber class"""

    def __init__(self, ip, port):
        super().__init__("sota_subscriber")
        self.robot_tools = RobotTools(ip, port)
        self.subscription = self.create_subscription(
            String, "speech", self.listener_callback, 10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        """callback function"""
        self.get_logger().info(f"I heard: {msg.data}")
        self.robot_tools.say_text(msg.data)


def main(args=None):
    """main function"""
    rclpy.init(args=args)
    sota_subscriber = SotaSubscriber(
        ip=os.environ.get("ROBOT_IP"), port=int(os.environ.get("ROBOT_PORT"))
    )
    rclpy.spin(sota_subscriber)
    sota_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
