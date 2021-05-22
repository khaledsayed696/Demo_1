#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from sensor_msgs.msg import NavSatFix
from example_interfaces.msg import String
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi
import numpy as np
import csv



class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.x=0
        self.y=0
        self.z=0 
        self.cou=0
        self.i=1
        
               
        self.create_subscription(Odometry,"odom",self.timer_call,rclpy.qos.qos_profile_sensor_data)

        self.get_logger().info("subscriber is started")

    def timer_call(self,odom):

        with open('/home/ubuntu/Demo_1/ITI_LSV_ROS2/ITI_LSV_ROS2/Labs/LAB2_Sensors/pose.csv', 'r') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in list(reader)[self.cou+1:self.cou+2]:
                self.k[0]=(row[0] , row [1] , row [2])
                self.a=float(row[0])
                self.b=float(row[1])
                self.c=float(row[2])
        self.cou+=self.i
        
        self.x=odom.pose.pose.position.x
        self.y=odom.pose.pose.position.y
        self.z=odom.pose.pose.orientation.z 

        self.quaternion=self.quaternion_from_euler(self.x,self.y,self.z)
        self.roll,self.pitch,self.yaw=self.euler_from_quaternion(self.quaternion)

        self.deg=self.yaw*57.2957795

        if(self.x-0.5 >= self.a+0.5 and self.y-0.5>= self.b+0.5 and self.deg-5>=self.z+5): 
            self.get_logger().info("you reach the goal and your next point is" + str(self.k)  )

        




    def quaternion_from_euler(self, roll, pitch, yaw):
        qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
        qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
        qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
        qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)
        return Quaternion(x=qx, y=qy, z=qz, w=qw)

    def euler_from_quaternion(self, quaternion):
        x = quaternion.x
        y = quaternion.y
        z = quaternion.z
        w = quaternion.w

        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (w * y - z * x)
        pitch = np.arcsin(sinp)

        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)

        return roll, pitch, yaw 
    


def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__=="__main__":
    main()



