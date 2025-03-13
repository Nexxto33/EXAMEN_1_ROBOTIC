# filter_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class FilterNode(Node):
    def __init__(self):
        super().__init__('filter_node')
        self.subscription1 = self.create_subscription(Float32, '/sensor1', self.sensor1_callback, 10)
        self.subscription2 = self.create_subscription(Float32, '/sensor2', self.sensor2_callback, 10)
        self.subscription3 = self.create_subscription(Float32, '/sensor3', self.sensor3_callback, 10)
        self.publisher_ = self.create_publisher(Float32, '/filtered_sensor', 10)
        self.sensor1_data = 0.0
        self.sensor2_data = 0.0
        self.sensor3_data = 0.0
        self.timer = self.create_timer(1.0, self.publish_filtered_data)
        
    def sensor1_callback(self, msg):
        self.sensor1_data = msg.data
        
    def sensor2_callback(self, msg):
        self.sensor2_data = msg.data
        
    def sensor3_callback(self, msg):
        self.sensor3_data = msg.data
        
    def publish_filtered_data(self):
        average = (self.sensor1_data + self.sensor2_data + self.sensor3_data) / 3.0
        msg = Float32()
        msg.data = average
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing filtered data: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = FilterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

