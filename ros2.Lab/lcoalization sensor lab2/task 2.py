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

class my_node(Node):
    def __init__(self):
        self.i=1
        self.cou=0
        self.frame_id= 'frame_id'
        
        super().__init__("Node_name")

        self.create_timer(1/1, self.timer_call)

        self.obj=self.create_publisher(NavSatFix,"fix", 5)

        self.get_logger().info("Node is started")

    def timer_call(self ):
        with open('/home/ubuntu/Demo_1/ITI_LSV_ROS2/ITI_LSV_ROS2/Labs/LAB2_Sensors/GGA_GST.csv', 'r') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in list(reader)[self.cou+1:self.cou+2]:
                self.latitude=float(row[2])
                self.longitude=float(row[4])
                self.altitude=float(row[9])
                self.hdop=float(row[8])
                self.lat_std_dev=float(row[21])
                self.lon_std_dev=float(row[22])
                self.alt_std_dev=float(row[23])


        self.cou+=self.i
        
        self.current_fix = NavSatFix()
        self.current_fix.header.frame_id = self.frame_id
        self.current_fix.latitude = self.latitude
        self.current_fix.longitude = self.longitude
        self.current_fix.altitude = self.altitude
        self.current_fix.position_covariance[0] = (self.hdop * self.lon_std_dev) ** 2
        self.current_fix.position_covariance[4] = (self.hdop * self.lat_std_dev) ** 2
        self.current_fix.position_covariance[8] = (2 * self.hdop * self.alt_std_dev) ** 2
        self.obj.publish(self.current_fix)
        
   

            



def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node )

    rclpy.shutdown()


if __name__=="__main__":
    main()            
