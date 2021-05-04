................................................Pub........................................

    #!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from second_pkg.msg import Firstone 


class my_node (Node):
    def __init__(self):
        super().__init__("Node_name")
        self.obj=self.create_publisher(Firstone, "my_topic", 10)
        self.create_timer(1/1, self.call_timer)

    def call_timer(self): 
            msg=Firstone()
            msg.message="my name is khaled ,5"
            msg.number=5
            self.obj.publish(msg)
        

    


def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__=="__main__":
    main()
    .............................................sub......................................
    
     #!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from example_interfaces.msg import Int64
from second_pkg.msg import Firstone 
from second_pkg.srv import Firstsr



class my_node(Node):
    def __init__(self):
        self.counter=0
        super().__init__("numebr_counter")
        self.create_subscription(Firstone,"my_topic",self.timer_call,10)
        self.get_logger().info("subscriber is started")
        
        self.create_timer(1/1,self.timer_call_)
        self.obj_pub=self.create_publisher(Int64,"my_number",10)


        self.create_service(Firstsr,"First_server",self.srv_call)
        

    def timer_call(self,msg):
        num=msg.message
        self.counter+=msg.number
        self.get_logger().info(msg.message+str(self.counter))


    def srv_call(self,rq,rsp):
        self.counter=0
        num1=rq.first
        num2=rq.second
        rsp.avg=int(num1+num2)
        return rsp

    def timer_call_(self):
        msg_int=Int64()
        my_data= self.counter
        msg_int.data=my_data
        self.obj_pub.publish(msg_int)

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()            
    

..................................................Client...........................

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from second_pkg.srv import Firstsr



class my_server(Node):
    def __init__(self):
        super().__init__("Client_OOP_node")
        self.service_client(True)

    def service_client(self,a):
        client=self.create_client(Firstsr,"First_server")
        while client.wait_for_service(0.25)==False:
            self.get_logger().warn("wating for server")

        request=Firstsr.Request()
        request.first=0
        request.second=0

        futur_obj=client.call_async(request)
        
        


       


def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
