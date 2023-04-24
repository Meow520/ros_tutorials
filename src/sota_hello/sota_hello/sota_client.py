import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class SotaClient(Node):
    def __init__(self):
        super().__init__("sota_client")
        self.cli = self.create_client(String, "service")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not available, waiting again...")
        self.req = String()

    def send_request(self):
        self.req.data = "Hello, Sota"
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)
    sota_client = SotaClient()
    response = sota_client.send_request()
    sota_client.get_logger().info('Response: "%s"' % response.data)
    sota_client.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
