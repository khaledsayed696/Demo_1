#!/usr/bin/env python3

import rclpy
import numpy as np
import math
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import time
img1=None
x1=x2=0
y1=y2=0
# Instantiate CvBridge
bridge = CvBridge()

class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(Image,"/intel_realsense_d435_depth/image_raw",self.img_cb, rclpy.qos.qos_profile_sensor_data)
        
        self.get_logger().info("subscriber is started")
        self.counter=1

        
    def img_cb(self,message):
        global img1 ,x1,x2,y1,y2
        cv2_img = bridge.imgmsg_to_cv2(message, "bgr8")
        #cv2_img=cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    


        if self.counter==1:
            img1=np.copy(cv2_img)
            self.counter+=1

        if self.counter==2:
            img2=np.copy(cv2_img)
            
            orb = cv2.ORB_create()
            t0 = time.time()
            keypoints_1, descriptors_1 = orb.detectAndCompute(img1, None)
            keypoints_2, descriptors_2 = orb.detectAndCompute(img2, None)

            if descriptors_1 is not None:
                if descriptors_2 is not None:
                    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

                    matches = bf.match(descriptors_1, descriptors_2)

                    matches = sorted(matches, key = lambda x:x.distance)

                    img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches, img2, flags=2)

                    
                    list_kp1 = [keypoints_1[mat.queryIdx].pt for mat in matches] 
                    list_kp2 = [keypoints_2[mat.trainIdx].pt for mat in matches]
        

                    for i in range (len(list_kp1)):
                        x1+=(list_kp1[i][0]-list_kp2[i][0])
                        y1+=((list_kp1[i][1]-list_kp2[i][1]))
                    x1/=len(list_kp1)
                    y1/=len(list_kp1)
                

                    stx_point=int(img3.shape[1]/2)
                    sty_point=int(img3.shape[0]/2)
                    endx_point=stx_point+int(x1)
                    endy_point=sty_point+int(y1)

                    img3=cv2.arrowedLine(img3, (stx_point,sty_point), (endx_point,endy_point),(255, 0, 0), 4) 
            
                    cv2.imshow("cv2_img", img3)
                    cv2.waitKey(1)
                    
                    img1=np.copy(img2)

                   

          
def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
