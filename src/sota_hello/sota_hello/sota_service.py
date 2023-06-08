"""imports"""
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class SotaService(Node):
    """SotaService class"""

    def __init__(self):
        super().__init__("sota_service")
        self.srv = self.create_service(String, "service", self.srv_callback)

    def srv_callback(self, request, response):
        """callback function"""
        response.data = "Hello, Sota"
        return response


def main(args=None):
    """main function"""
    rclpy.init(args=args)
    sota_service = SotaService()
    rclpy.spin(sota_service)
    sota_service.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
