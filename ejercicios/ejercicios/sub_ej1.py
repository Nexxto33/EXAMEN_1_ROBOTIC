import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MotorSubscriber(Node):
    def __init__(self):
        super().__init__('sub_ej1')
        self.subscription = self.create_subscription(String, 'sensor_data', self.listener_callback, 10)

    def listener_callback(self, msg):
        sensor_state = msg.data
        mi, md, estado = self.get_motor_state(sensor_state)
        self.get_logger().info(f"Sensores: {sensor_state} | Motores: {mi}{md} | Estado: {estado}")

    def get_motor_state(self, sensor_state):
        table = {
            "000": ("1", "1", "Adelante"),
            "001": ("0", "1", "Derecha"),
            "010": ("0", "0", "Alto"),
            "011": ("0", "1", "Derecha"),
            "100": ("1", "0", "Izquierda"),
            "101": ("1", "1", "Adelante"),
            "110": ("1", "0", "Izquierda"),
            "111": ("0", "0", "Alto"),
        }
        return table.get(sensor_state, ("0", "0", "Desconocido"))

def main(args=None):
    rclpy.init(args=args)
    node = MotorSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
