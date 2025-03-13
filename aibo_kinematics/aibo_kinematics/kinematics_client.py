import rclpy
from rclpy.node import Node
from aibo_kinematics.srv import Kinematics

class KinematicsClient(Node):
    def __init__(self):
        super().__init__('kinematics_client')
        self.client = self.create_client(Kinematics, 'calculate_kinematics')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Esperando al servidor de cinemática...")

        self.request_angles()

    def request_angles(self):
        configurations = [
            (0, 0, 0, 0),
            (20, 45, 10, 0),
            (10, -30, 25, 0)
        ]

        results = []

        for config in configurations:
            request = Kinematics.Request()
            request.theta1, request.theta2, request.theta3, request.theta4 = config

            future = self.client.call_async(request)
            rclpy.spin_until_future_complete(self, future)
            
            response = future.result()
            results.append((config, (response.x, response.y, response.z, response.roll, response.pitch, response.yaw)))
            self.get_logger().info(f"Entrada: {config} => Salida: {response.x:.2f}, {response.y:.2f}, {response.z:.2f}, {response.roll:.2f}, {response.pitch:.2f}, {response.yaw:.2f}")

        self.get_logger().info(f"Resultados almacenados: {results}")

def main():
    rclpy.init()
    node = KinematicsClient()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
