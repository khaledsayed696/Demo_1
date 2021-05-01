#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class my_server(Node):
    def __init__(self):
        super().__init__("Client_OOP_node")
        self.service_client(17.0,4.0,3.0)



    def service_client(self,a,b,z):
        client=self.create_client(Spawn,"spawn")
        while client.wait_for_service(0.25)==False:
            self.get_logger().warn("wating for server")

        request=Spawn.Request()
        request.x=a
        request.y=b
        request._theta=z
        futur_obj=client.call_async(request)
        
        


       


def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
