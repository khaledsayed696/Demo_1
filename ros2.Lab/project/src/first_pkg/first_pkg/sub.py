#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from second_pkg.srv import Firstsr
import random
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt




class my_server(Node):
    def __init__(self):
        super().__init__("Client_OOP_node")
        self.desierd_x=0
        self.desired_y=0
        self.now_x=6
        self.now_y=8
        self.P_lin=6
        self.now_theta=3

        self.create_subscription(Pose,"pose",self.update_pose,10)

        self.service_client(True)

        self.create_timer(1/1 ,self.timer_call)
        self.obj=self.create_publisher(Twist, "cmd_vel", 10)

    def timer_call(self):
        self.linear_dist=abs(sqrt(((self.desierd_x-self.now_x)**2)+((self.desired_y-self.now_y)**2)))
        self.lin_vel=self.linear_dist*self.P_lin
        self.theta_desired=atan2((self.desired_y-self.now_y),(self.desierd_x-self.now_x))
        self.theta_error=self.theta_desired-self.now_theta
        
    def update_pose(self, data):
         
        self.desired_x = data.x
        self.desierd_y = data.y

        


    def service_client(self,a):
        client=self.create_client(Firstsr,"First_server")
        while client.wait_for_service(0.25)==False:
           
            self.get_logger().warn("wating for server")
        random.randint(0, 10)

        request=Firstsr.Request()
        request.x=float(random.randint(0, 10))
        request.y=float(random.randint(0, 10))
        request.z=float(random.randint(0, 10))
        futur_obj=client.call_async(request)
        futur_obj.add_done_callback(self.future_call)

    def future_call(self,future_msg):
        self.get_logger().info(float(future_msg.result().avg))


    

        


       


def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()