"""imports"""
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class SotaPublisher(Node):
    """SotaPublisher class"""

    def __init__(self):
        super().__init__("sota_publisher")
        self.publisher_ = self.create_publisher(String, "speech", 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        publish_msg = String()
        publish_msg.data = input()
        self.publisher_.publish(publish_msg)

    def publish(self, text: str):
        """publish function"""
        self.publisher_.publish(text)


def main(args=None):
    """main function"""
    rclpy.init(args=args)
    sota_publisher = SotaPublisher()
    rclpy.spin(sota_publisher)
    sota_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
