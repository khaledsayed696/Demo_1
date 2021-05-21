#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from sensor_msgs.msg import NavSatFix
from example_interfaces.msg import String
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi
import numpy as np

import csv


class my_node(Node):
    def __init__(self):
        self.i=1
        self.cou=0
        
        super().__init__("Node_name")

        self.create_timer(1/1, self.timer_call)

        self.obj=self.create_publisher(Imu, "zed2_imu", 30)
        
        self.get_logger().info("Node is started")

    def timer_call(self):
        with open('/home/ubuntu/Demo_1/ITI_LSV_ROS2/ITI_LSV_ROS2/Labs/LAB1_Sensors/imu_data.csv', 'r') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in list(reader)[self.cou:self.cou+1]:
                self.a=float(row[0])
                self.b=float(row[1])
                self.c=float(row[2])
                self.d=float(row[3])
                self.e=float(row[4])
                self.f=float(row[5])
                self.g=float(row[6])
                
        self.cou+=self.i
        

        self.imu_msg=Imu()
        self.imu_msg.linear_acceleration.x = self.a
        self.imu_msg.linear_acceleration.y=self.b
        self.imu_msg.linear_acceleration.z = self.c
        self.imu_msg.angular_velocity.x=self.d
        self.imu_msg.angular_velocity.y = self.e
        self.imu_msg.angular_velocity.z=self.f
        self.imu_msg.orientation.x = self.g
        self.obj.publish(self.imu_msg)
        

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node )

    rclpy.shutdown()


if __name__=="__main__":
    main()            
