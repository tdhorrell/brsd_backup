import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

class JetsonNode(Node):
    def __init__(self):
        super().__init__('jetson_node')

        #Variables to store data
        self.joystickDirection = 0

        # Publishing to ESP32
        self.publisher_ = self.create_publisher(
            Twist, 
            'micro_ros_arduino_node', 
            10
        )

        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            depth=10
        )

        # Subscribing to joystick node
        self.joystickSubscription = self.create_subscription(
            Int32,
            'joystick_command',
            self.updateJoystickVal,
            qos_profile
        )

        timerFreq = .1
        self.timer = self.create_timer(timerFreq, self.publish_data) # Send every .1 second

    def updateJoystickVal(self, msg):
        self.joystickDirection = msg.data
        self.get_logger().info(f"updating {msg.data}")
    
    def publish_data(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 30.0

        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing Twist: Linear x - {msg.linear.x}, Angular z - {msg.angular.z}")

def main(args=None):
    rclpy.init(args=args)
    node = JetsonNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()