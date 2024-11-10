import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32MultiArray
from transitions import Machine
import numpy as np

class BRSD_sm(object):
    def __init__(self, node):
        self.node = node
        self.ready = False
        self.rand = False
        self.theta = 0
        self.dist = 0
        self.bump_flag = False
        self.user_flag = True
        self.x_cord = 0
        self.y_cord = 0

    def calc_theta(self):
        self.dist = np.sqrt(self.x_cord**2 + self.y_cord**2)
        if(self.y_cord != 0):
            self.theta = np.rad2deg(np.arctan(self.x_cord / self.y_cord))
        else:
            self.theta = 0
    
    #---------------------------
    #       Transitions
    #---------------------------

    # automatic pass transition
    def state_pass(self, even_data):
        return True


    # idle 1 transitions
    def i1_to_f1(self, even_data):
        return (self.theta > -5 and self.theta < 5 and self.dist > 0)

    def i1_to_l1(self, even_data):
        return (self.theta < -5 and self.dist > 0)

    def i1_to_r1(self, even_data):
        return (self.theta > 5 and self.dist > 0)


    # forward 1 transitions
    def f1_to_l1(self, even_data):
        return (self.theta < -5 and self.dist > 0)      

    def f1_to_r1(self, even_data):
        return (self.theta > 5 and self.dist > 0)  

    def f1_to_f2(self, even_data):
        return (self.theta >= -5 and self.theta <= 5 and self.dist > 0)


    # left 1 transitions
    def l1_to_l2(self, even_data):
        return (self.theta < -20 and self.dist > 0)

    def l1_to_f1(self, even_data):
        return (self.theta >= -5 and self.dist > 0)


    # left 2 transitions
    def l2_to_l1(self, even_data):
        return (self.theta > -20 and self.dist > 0)
    

    # right 1 transitions
    def r1_to_r2(self, even_data):
        return (self.theta > 20 and self.dist > 0)

    def r1_to_f1(self, even_data):
        return (self.theta <= 5 and self.dist > 0)
    

    # right 2 transitions
    def r2_to_r1(self, even_data):
        return (self.theta < 20 and self.dist > 0)
    
    # stop, backwards transitions can be handled by existing checks above
    # here are transitions INTO the stop states
    def state_to_s1(self, even_data):
        return self.bump_flag == True
    
    def state_to_s2(self, even_data):
        return self.user_flag == False
    

    #---------------------------
    #       Callbacks
    #---------------------------

    def callback_i1(self, even_data):
        self.node.publish_data(0.0, 0.0)
        self.node.get_logger().info('i1 CALLBACK')

    def callback_f1(self, even_data):
        self.node.publish_data(0.6, 0.0)
        self.node.get_logger().info('f1 CALLBACK')

    def callback_f2(self, even_data):
        self.node.publish_data(1.2, 0.0)
        self.node.get_logger().info('f2 CALLBACK')

    def callback_l1(self, even_data):
        self.node.publish_data(0.6, -15.0)
        self.node.get_logger().info('l1 CALLBACK')

    def callback_l2(self, even_data):
        self.node.publish_data(0.6, -30.0)
        self.node.get_logger().info('l2 CALLBACK')

    def callback_r1(self, even_data):
        self.node.publish_data(0.6, 15.0)
        self.node.get_logger().info('r1 CALLBACK')

    def callback_r2(self, even_data):
        self.node.publish_data(0.6, 30.0)
        self.node.get_logger().info('r2 CALLBACK')

    def callback_s1(self, even_data):
        self.node.publish_data(0.0, 0.0)
        self.node.get_logger().info('s1 CALLBACK')

    def callback_s2(self, even_data):
        self.node.publish_data(0.0, 0.0)
        self.node.get_logger().info('s2 CALLBACK')

    def callback_b1(self, even_data):
        self.node.publish_data(-0.3, 0.0)
        self.node.get_logger().info('b1 CALLBACK')                

# define machine states
states = ['i1', 'f1', 'f2', 'l1', 'l2', 'r1', 'r2', 's1', 's2', 'b1']

# define transition conditions
transitions = [
    # idle 1 transitions
    {'trigger': 'check', 'source': 'i1', 'dest': 's1', 'conditions': 'state_to_s1'},
    {'trigger': 'check', 'source': 'i1', 'dest': 's2', 'conditions': 'state_to_s2'},
    {'trigger': 'check', 'source': 'i1', 'dest': 'f1', 'conditions': 'i1_to_f1'},
    {'trigger': 'check', 'source': 'i1', 'dest': 'l1', 'conditions': 'i1_to_l1'},
    {'trigger': 'check', 'source': 'i1', 'dest': 'r1', 'conditions': 'i1_to_r1'},
    
    # forward 1 transitions
    {'trigger': 'check', 'source': 'f1', 'dest': 's1', 'conditions': 'state_to_s1'},
    {'trigger': 'check', 'source': 'f1', 'dest': 's2', 'conditions': 'state_to_s2'},
    {'trigger': 'check', 'source': 'f1', 'dest': 'l1', 'conditions': 'f1_to_l1'},
    {'trigger': 'check', 'source': 'f1', 'dest': 'r1', 'conditions': 'f1_to_r1'},
    {'trigger': 'check', 'source': 'f1', 'dest': 'f2', 'conditions': 'f1_to_f2'},   

    # forward 2 transitions (can use same transitions as f1)
    {'trigger': 'check', 'source': 'f2', 'dest': 's1', 'conditions': 'state_to_s1'},
    {'trigger': 'check', 'source': 'f2', 'dest': 's2', 'conditions': 'state_to_s2'},
    {'trigger': 'check', 'source': 'f2', 'dest': 'l1', 'conditions': 'f1_to_l1'},
    {'trigger': 'check', 'source': 'f2', 'dest': 'r1', 'conditions': 'f1_to_r1'},
    # {'trigger': 'check', 'source': 'f2', 'dest': 'f1', 'conditions': 'f2_to_f1'}, 

    # left 1 transitions
    {'trigger': 'check', 'source': 'l1', 'dest': 's1', 'conditions': 'state_to_s1'},
    {'trigger': 'check', 'source': 'l1', 'dest': 's2', 'conditions': 'state_to_s2'},
    {'trigger': 'check', 'source': 'l1', 'dest': 'f1', 'conditions': 'l1_to_f1'},
    {'trigger': 'check', 'source': 'l1', 'dest': 'l2', 'conditions': 'l1_to_l2'},

    # left 2 transitions
    {'trigger': 'check', 'source': 'l2', 'dest': 's1', 'conditions': 'state_to_s1'},
    {'trigger': 'check', 'source': 'l2', 'dest': 's2', 'conditions': 'state_to_s2'},
    {'trigger': 'check', 'source': 'l2', 'dest': 'l1', 'conditions': 'l2_to_l1'},

    # right 1 transitions
    {'trigger': 'check', 'source': 'r1', 'dest': 's1', 'conditions': 'state_to_s1'},
    {'trigger': 'check', 'source': 'r1', 'dest': 's2', 'conditions': 'state_to_s2'},
    {'trigger': 'check', 'source': 'r1', 'dest': 'f1', 'conditions': 'r1_to_f1'},
    {'trigger': 'check', 'source': 'r1', 'dest': 'r2', 'conditions': 'r1_to_r2'},

    # right 2 transitions
    {'trigger': 'check', 'source': 'r2', 'dest': 's1', 'conditions': 'state_to_s1'},
    {'trigger': 'check', 'source': 'r2', 'dest': 's2', 'conditions': 'state_to_s2'},
    {'trigger': 'check', 'source': 'r2', 'dest': 'r1', 'conditions': 'r2_to_r1'},

    # stop 1 transitions  
    {'trigger': 'check', 'source': 's1', 'dest': 'b1', 'conditions': 'state_pass'},

    # stop 2 transitions
    {'trigger': 'check', 'source': 's2', 'dest': 'l1', 'conditions': 'f1_to_l1'},
    {'trigger': 'check', 'source': 's2', 'dest': 'r1', 'conditions': 'f1_to_r1'},
    {'trigger': 'check', 'source': 's2', 'dest': 'f1', 'conditions': 'i1_to_f1'},

    # backwards 1 transitions
    {'trigger': 'check', 'source': 'b1', 'dest': 's1', 'conditions': 'state_to_s1'},
    {'trigger': 'check', 'source': 'b1', 'dest': 's2', 'conditions': 'state_to_s2'},    
    {'trigger': 'check', 'source': 'b1', 'dest': 'l1', 'conditions': 'f1_to_l1'},
    {'trigger': 'check', 'source': 'b1', 'dest': 'r1', 'conditions': 'f1_to_r1'},
    {'trigger': 'check', 'source': 'b1', 'dest': 'f1', 'conditions': 'i1_to_f1'}]

class BRSD_machine(object):
    def __init__(self, node):
        # initialize machine
        self.model = BRSD_sm(node)
        self.machine = Machine(model=self.model, states=states, transitions=transitions, initial='i1', send_event=True)

        # initialize callbakcs
        self.machine.on_enter_i1('callback_i1')
        self.machine.on_enter_f1('callback_f1')
        self.machine.on_enter_f2('callback_f2')
        self.machine.on_enter_l1('callback_l1')
        self.machine.on_enter_l2('callback_l2')
        self.machine.on_enter_r1('callback_r1')
        self.machine.on_enter_r2('callback_r2')
        self.machine.on_enter_s1('callback_s1')
        self.machine.on_enter_s2('callback_s2')
        self.machine.on_enter_b1('callback_b1')

class BrsdFsmNode(Node):
    def __init__(self):
        super().__init__('brsd_fsm_node')

        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            depth=10
        )

        self.vel_publisher = self.create_publisher(
            Twist, 
            'micro_ros_arduino_node', 
            10
        )

        self.point_subscriber = self.create_subscription(
            Int32MultiArray,
            'navigation_path',
            self.update_target_point,
            qos_profile
        )

        self.timer = self.create_timer(0.1, self.timer_callback)

        self.brsd = BRSD_machine(self)

    def timer_callback(self):
        self.brsd.model.calc_theta()
        self.brsd.model.check()

    def update_target_point(self, msg):
        self.brsd.model.x_cord = msg.data[0]
        self.brsd.model.y_cord = msg.data[1]

    def publish_data(self, x_vel, z_ang):
        msg = Twist()
        msg.linear.x = x_vel
        msg.angular.z = z_ang

        self.vel_publisher.publish(msg)
        self.get_logger().info(f"Publishing Twist: Linear x - {msg.linear.x}, Angular z - {msg.angular.z}")

def main(args=None):
    rclpy.init(args=args)
    node = BrsdFsmNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()