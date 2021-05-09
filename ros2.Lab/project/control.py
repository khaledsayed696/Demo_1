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
        self.now_x=0
        self.now_y=0
        self.P_lin=5
        self.now_theta=0

        self.service_client(True)

        self.create_subscription(Pose,"turtle1/pose",self.update_pose,10)

        self.obj=self.create_publisher(Twist, "turtle1/cmd_vel", 10)

    

    def update_pose(self, data):
         
        self.desired_x = data.x
        self.desired_y = data.y
        self.theta_desired=data.theta

        self.msg=Twist()
        self.linear_dist=abs(sqrt(((self.desired_x-self.now_x)**2)+((self.desired_y-self.now_y)**2)))
        self.msg.linear.x=self.linear_dist*self.P_lin
        self.theta_desired=atan2((self.desired_y-self.now_y),(self.desired_x-self.now_x))
        self.msg.angular.z=self.theta_desired-self.now_theta

        self.obj.publish(self.msg)
        


    def service_client(self,a):
        client=self.create_client(Firstsr,"First_server")
        while client.wait_for_service(0.25)==False:
           
            self.get_logger().warn("wating for server")
        random.randint(0, 10)

        request=Firstsr.Request()
        request.x=float(random.randint(0, 10))
        request.y=float(random.randint(0, 10))
        request.z=float(random.randint(0, 10))

        self.now_x=request.x
        self.now_y=request.y
        self.now_theta=request.z  

        futur_obj=client.call_async(request)
              
        
    

        


       


def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
