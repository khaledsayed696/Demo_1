import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
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
import math



class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.dif_yaw=0
        self.curv=0
        self.create_subscription(Path,"local_plan",self.timer_call_sub,rclpy.qos.qos_profile_sensor_data)
        self.create_timer(1/1 ,self.timer_call)
        self.obj_pub=self.create_publisher(String,"my_topic",10)

        self.get_logger().info("subscriber is started")
        

    def timer_call_sub(self,msg):
        self.plan_size = len(msg.poses)
        print(self.plan_size)

        if( self.plan_size > 10):
            self.point_1_x= msg.poses[0].pose.position.x
            self.point_1_y= msg.poses[0].pose.position.y
            self.point_2_x= msg.poses[3].pose.position.x
            self.point_2_y= msg.poses[5].pose.position.y
            self.point_3_x= msg.poses[10].pose.position.x   
            self.point_3_y= msg.poses[10].pose.position.y
            self.point_4_x= msg.poses[0].pose.orientation.x
            self.point_5_y= msg.poses[5].pose.orientation.y
            self.point_6_z= msg.poses[10].pose.orientation.z

        _,_,self.yaw_rad = self.euler_from_quaternion( msg.poses[3].pose.orientation)
        _,_,self.yaw_rad2 = self.euler_from_quaternion( msg.poses[8].pose.orientation)

        self.dif_yaw=self.yaw_rad2-self.yaw_rad
        print(self.dif_yaw)



        self.curv= self.menger_curvature( self.point_1_x,self.point_1_y, self.point_2_x, self.point_2_y, self.point_3_x, self.point_3_y)
        
        if (self.dif_yaw > 0 ):
            self.get_logger().info("The robot is turning to the right with a curv" + str(self.curv)  ) 
        else:
            self.get_logger().info("The robot is turning to the left with curv" + str(self.curv)) 

        self.get_logger().info( str(self.point_1_x) + str(self.point_1_y)) 
        self.get_logger().info( str(self.point_2_x)  + str(self.point_2_y))  
        self.get_logger().info( str(self.point_3_x)  + str(self.point_3_y))

        self.get_logger().info( str( self.yaw_rad))  
  
         

    def timer_call(self):
        
        msg=String()
        if (self.dif_yaw < 0):
            msg.data="The robot is turning to the right with a curv" + str(self.curv) 
            self.obj_pub.publish(msg)  
        else:
            msg.data="The robot is turning to the left with curv" + str(self.curv) 
            self.obj_pub.publish(msg)   
        

    def menger_curvature(self, point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        triangle_area = 0.5 * abs( (point_1_x*point_2_y) + (point_2_x*point_3_y) + (point_3_x*point_1_y) - (point_2_x*point_1_y) - (point_3_x*point_2_y) - (point_1_x*point_3_y))#Shoelace formula 
            
        curvature = (4*triangle_area) / (math.sqrt(pow(point_1_x - point_2_x,2)+pow(point_1_y - point_2_y,2)) * math.sqrt(pow(point_2_x - point_3_x,2)+pow(point_2_y - point_3_y,2)) * math.sqrt(pow(point_3_x - point_1_x,2)+pow(point_3_y - point_1_y,2)))#Menger curvature 
        return curvature


    
    def euler_from_quaternion(self, quaternion):
        """
    Converts quaternion (w in last place) to euler roll, pitch, yaw
    quaternion = [x, y, z, w]
    Bellow should be replaced when porting for ROS 2 Python tf_conversions is done.
    """
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
