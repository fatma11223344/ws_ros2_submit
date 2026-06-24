import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class StudentTalker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, '/robocup_chatter', 10)
        self.counter = 0
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info('Talker node started')

    def timer_callback(self):
        self.counter += 1
        msg = String()
        msg.data = f'Counter: {self.counter}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = StudentTalker()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
