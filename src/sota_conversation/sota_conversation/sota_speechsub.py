"""imports"""
import os
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from dotenv import load_dotenv
from .robot_modules.robottools import RobotTools
import openai

load_dotenv()


class SotaSubscriber(Node):
    """SotaSubscriber class"""

    def __init__(self, ip, port, api_key):
        super().__init__("sota_subscriber")
        self.robot_tools = RobotTools(ip, port)
        self.__api_key = api_key
        self.subscription = self.create_subscription(
            String, "conversation", self.listener_callback, 10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        """callback function"""
        self.get_logger().info(f"USER: {msg.data}")
        message = self.create_response(msg.data)
        duration = self.robot_tools.say_text(message)
        servo_list = self.robot_tools.make_beat_motion(duration)
        self.robot_tools.play_motion(servo_list)

    def create_response(self, text: str) -> str:
        openai.api_key = self.__api_key
        params = [
            {"role": "system", "content": "You are chating with the user in english."}
        ]
        params.append({"role": "user", "content": text})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=params)
        message = response.choices[0].message.content
        params.append({"role": "assistant", "content": message})
        self.get_logger().info(f"ROBOT:{message}")
        return message


def main(args=None):
    """main function"""
    rclpy.init(args=args)
    sota_subscriber = SotaSubscriber(
        ip=os.environ.get("ROBOT_IP"),
        port=int(os.environ.get("ROBOT_PORT")),
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    rclpy.spin(sota_subscriber)
    sota_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
