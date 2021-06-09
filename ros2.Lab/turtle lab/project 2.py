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
       
        self.P_lin=0.1
        self.Ki=0.001
        self.Kd=0.05

        self.now_theta=0
        self.desired_x=9.0
        self.desired_y=9.0

        self.xold=0
        self.theta_desired=0
        self.now_x=0
        self.now_y=0
        self.xCum_Error=0
        self.thold=0
        self.tCum_Error=0
        

        #self.service_client(True)

        self.create_subscription(Pose,"turtle1/pose",self.update_pose,10)        
        self.obj=self.create_publisher(Twist, "turtle1/cmd_vel", 1)


    def update_pose(self,data):
         
        self.now_x = data.x
        self.now_y = data.y
        #self.theta_now=data.theta
        self.msg=Twist()
        print(self.now_x)
        print(self.now_y)
        

        self.linear_dist=abs(sqrt(((self.desired_x-self.now_x)**2)+((self.desired_y-self.now_y)**2)))
        
        self.xdot=  self.linear_dist  - self.xold
        self.xCum_Error+=self.linear_dist        
        self.msg.linear.x=(self.linear_dist*self.P_lin)+(self.xCum_Error*self.Ki)+(self.xdot*self.Kd)
        self.xold=self.linear_dist
        self.theta_dist=atan2((self.desired_y-self.now_y),(self.desired_x-self.now_x))
        self.theta_dot= self.theta_dist-self.thold
        self.tCum_Error+=  self.theta_dist
        self.thold=self.theta_dist
        self.msg.angular.z=(self.theta_dist*self.P_lin)+(self.tCum_Error*self.Ki)+(self.theta_dot*self.Kd)

        if(self.linear_dist<=1):
            self.msg.linear.x=0.0
            self.msg.angular.z=0.0
        self.obj.publish(self.msg)

        
        #self.msg.angular.z=self.theta_desired-self.now_theta
        
        
        #self.msg.linear.x=self.linear_dist*self.P_lin

    '''
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
        '''      

def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
