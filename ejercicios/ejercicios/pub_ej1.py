import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('pub_ej1')
        self.publisher_ = self.create_publisher(String, 'sensor_data', 10)
        self.timer = self.create_timer(3.0, self.publish_sensor_data)

    def publish_sensor_data(self):
        si = random.randint(0, 1)
        sc = random.randint(0, 1)
        sd = random.randint(0, 1)
        sensor_state = f"{si}{sc}{sd}"
        self.publisher_.publish(String(data=sensor_state))
        self.get_logger().info(f"Publicando sensores: {sensor_state}")

def main(args=None):
    rclpy.init(args=args)
    node = SensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
