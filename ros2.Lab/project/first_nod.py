#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from second_pkg.srv import Firstsr
from second_pkg.msg import Firstone



class my_server(Node):
    def __init__(self):
        super().__init__("Client_OOP_node")
      
        self.create_service(Firstsr,"First_server",self.service_client)
        


    def service_client(self,req,rsp):

        client=self.create_client(Spawn,"spawn")
        while client.wait_for_service(0.25)==False:
            self.get_logger().warn("wating for server")

        request=Spawn.Request()
        request.x=req.x
        request.y=req.y
        request._theta=req.z
        futur_obj=client.call_async(request)

        rsp.a=req.x
        rsp.b=req.y
        rsp.c=req.z   
        return rsp


       


def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
