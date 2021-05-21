#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from sensor_msgs.msg import NavSatFix
from example_interfaces.msg import String
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi
import numpy as np


class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.qz=0
        self.create_subscription(Imu,"imu",self.timer_call,rclpy.qos.qos_profile_sensor_data)
        
        self.get_logger().info("subscriber is started")

    def timer_call(self,imu_msg):

        self.roll=imu_msg.orientation.x
        self.pich=imu_msg.orientation.y
        self.yaw=imu_msg.orientation.z
        self.quaternion=self.quaternion_from_euler(self.roll,self.pich,self.yaw)
        self.x,self.y,self.z=self.euler_from_quaternion(self.quaternion)

        if(self.z> -2 and self.z< 2):
            self.get_logger().info("The robot is nearly heading north .. Heading is:" + str(imu_msg.orientation.z))

        if(abs(imu_msg.linear_acceleration.x) >0.3):
            self.get_logger().info("Warning !! .. linear acceleration x exceeded the limit . Current acceleration is " + str(imu_msg.linear_acceleration.x)+ ) 
        if(abs(imu_msg.angular_velocity.z) >0.3): 
            self.get_logger().info("Warning !! .. angular velocity z exceeded the limit . Current Angular velocity is" + str(imu_msg.angular_velocity.z ) )




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



