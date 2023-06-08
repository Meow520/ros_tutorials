"""imports"""
from dotenv import load_dotenv
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import speech_recognition as sr

load_dotenv()


class SotaPublisher(Node):
    """SotaPublisher class"""

    def __init__(self):
        super().__init__("sota_publisher")
        self.publisher_ = self.create_publisher(String, "conversation", 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.done = False

    def timer_callback(self):
        """timer callback function"""
        publish_msg = String()
        publish_msg.data = self.speech_recognition()
        self.publisher_.publish(publish_msg)

    def publish(self, text: str):
        """publish function"""
        self.publisher_.publish(text)

    def speech_recognition(self) -> String:
        "speechrecognition function"
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # r.adjust_for_ambient_noise(source)  # ノイズ対策（オプション, might not use to faster response）
            while True:
                # print('何か話してください...')

                audio = r.listen(source)

                try:
                    user_input = r.recognize_google(audio, language="en-GB")
                    print("USER: " + user_input)
                    return user_input

                except sr.UnknownValueError:
                    # print('Google Speech Recognition could not understand audio')
                    continue
                except sr.RequestError as e:
                    # print('Could not request results from Google Speech Recognition service; {0}'.format(e))
                    continue


def main(args=None):
    """main function"""
    rclpy.init(args=args)
    sota_publisher = SotaPublisher()
    rclpy.spin(sota_publisher)
    sota_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
