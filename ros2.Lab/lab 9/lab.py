#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.msg import Pose


import csv


class my_node(Node):
    def __init__(self):
        self.i=1
        self.cou=0
        
        super().__init__("Node_name")

        self.create_timer(1/1, self.timer_call)

        self.obj=self.create_publisher(Twist, "turtle1/cmd_vel", 10)

        self.create_subscription(Pose,"turtle1/pose",self.update_pose,10)


        
        self.get_logger().info("Node is started")

    def timer_call(self ):
        with open('/home/ubuntu/Demo_1/ITI_LSV_ROS2/Labs/LAB9_ROS2/turtle_commands.csv', 'r') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in list(reader)[self.cou+1:self.cou+2]:
                self.a=float(row[0])
                self.b=float(row[1])
        self.cou+=self.i
        
        self.msg=Twist()
        self.msg.linear.x = self.a
        self.msg.angular.z=self.b
        self.obj.publish(self.msg)
        


    def update_pose(self, data):
        self.desired_x = data.x
        self.desired_y = data.y
        self.theta_desired=data.theta
        if( self.desired_x >10 and self.desired_x<20): 
            self.service_client()
           
    


            
    
    def service_client(self):
        client=self.create_client(Empty,"reset")
        while client.wait_for_service(0.25)==False:
            self.get_logger().warn("wating for server")

        request=Empty.Request()
        futur_obj=client.call_async(request)

   

            



def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node )

    rclpy.shutdown()


if __name__=="__main__":
    main()            
