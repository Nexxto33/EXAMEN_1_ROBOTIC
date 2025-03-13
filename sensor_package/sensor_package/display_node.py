# display_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class DisplayNode(Node):
    def __init__(self):
        super().__init__('display_node')
        self.subscription = self.create_subscription(Float32, '/filtered_sensor', self.filtered_sensor_callback, 10)
        
    def filtered_sensor_callback(self, msg):
        self.get_logger().info(f'Filtered Sensor Average: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = DisplayNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

