#!/usr/bin/env python3

import rclpy
import numpy as np
import math
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.x=0
        self.min_value=0
        self.create_subscription(LaserScan,"scan",self.scan_cb, rclpy.qos.qos_profile_sensor_data)

        self.create_subscription(Twist,"key_cmd_vel",self.timer_call_sub,10)
        self.create_timer(1/1, self.timer_call)
        self.obj=self.create_publisher(Twist, "cmd_vel", 10)

        
        self.get_logger().info("subscriber is started")


        
    def scan_cb(self,message):
        laser_data = message.ranges[0:20]
        print("len", len(laser_data))
        max_value = max(laser_data)
        self.min_value = min(laser_data)
        #laser_data.count(max_value)
        self.x=laser_data.index(self.min_value)
        print("min", self.min_value, laser_data.count(self.min_value), laser_data.index(self.min_value))
        indices = [idx for idx,val in enumerate(laser_data) if val < 1.0]
        print(indices)

        max_index = np.where(np.isinf(laser_data),-np.Inf,laser_data).argmax()
        print("max", max_index, laser_data[max_index],max_value)


    def timer_call(self ): 
        
        if(  self.min_value < 2.5):
            self.msg=Twist()
            self.msg.linear.x = 0.0
            self.obj.publish(self.msg)

    def timer_call_sub(self,msg):

        self.obj.publish(msg )
    
          
def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()


