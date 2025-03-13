import rclpy
from rclpy.node import Node
from aibo_kinematics.srv import Kinematics
import numpy as np

class KinematicsServer(Node):
    def __init__(self):
        super().__init__('kinematics_server')
        self.srv = self.create_service(Kinematics, 'calculate_kinematics', self.calculate_kinematics_callback)
        self.get_logger().info("Servidor de cinemática directa listo.")

    def calculate_kinematics_callback(self, request, response):
        # Convertir ángulos a radianes
        theta1 = np.radians(request.theta1)
        theta2 = np.radians(request.theta2)
        theta3 = np.radians(request.theta3)
        theta4 = np.radians(request.theta4)

        # Longitudes constantes en mm
        L1 = 69.5
        L2 = 71.5

        # Cinemática directa usando matrices homogéneas
        x = L1 * np.cos(theta2) + L2 * np.cos(theta2 + theta3)
        y = 0  # Suponemos que el movimiento está en el plano XZ
        z = L1 * np.sin(theta2) + L2 * np.sin(theta2 + theta3)

        # Orientación (simplificada)
        roll = np.degrees(theta1)
        pitch = np.degrees(theta2 + theta3)
        yaw = np.degrees(theta4)

        response.x = x
        response.y = y
        response.z = z
        response.roll = roll
        response.pitch = pitch
        response.yaw = yaw

        self.get_logger().info(f"Recibido: θ1={request.theta1}, θ2={request.theta2}, θ3={request.theta3}, θ4={request.theta4}")
        self.get_logger().info(f"Respuesta: x={x:.2f}, y={y:.2f}, z={z:.2f}, roll={roll:.2f}, pitch={pitch:.2f}, yaw={yaw:.2f}")

        return response

def main():
    rclpy.init()
    node = KinematicsServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
