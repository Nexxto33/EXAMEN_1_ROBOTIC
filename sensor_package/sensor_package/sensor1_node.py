import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class Sensor1Node(Node):
    def __init__(self):
        super().__init__('sensor1_node')
        self.publisher_ = self.create_publisher(Float32, '/sensor1', 10)
        self.timer = self.create_timer(1.0, self.publish_sensor_data)
        
    def publish_sensor_data(self):
        msg = Float32()
        msg.data = random.uniform(0.0, 10.0)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Sensor1Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
