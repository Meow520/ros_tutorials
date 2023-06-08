"""imports"""
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class SotaClient(Node):
    """SotaClient class"""

    def __init__(self):
        super().__init__("sota_client")
        self.cli = self.create_client(String, "service")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not available, waiting again...")
        self.req = String()
        self.future = self.cli.call_async(self.req)

    def send_request(self):
        """send request"""
        self.req.data = "Hello, Sota"
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    """main function"""
    rclpy.init(args=args)
    sota_client = SotaClient()
    response = sota_client.send_request()
    sota_client.get_logger().info(f"Response: {response.data}")
    sota_client.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
