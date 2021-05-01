................................................Pub........................................
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class my_node (Node):
    def __init__(self):
        super().__init__("Node_name")
        
        self.create_timer(1/1,self.timer_call)
        self.obj_pub=self.create_publisher(Int64,"number",10)

        self.get_logger().info("Node is started")

    def timer_call(self):
        msg_int=Int64()
        my_data= 5
        msg_int.data=my_data
        self.obj_pub.publish(msg_int)



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
from example_interfaces.srv import AddTwoInts
from example_interfaces.srv import SetBool


class my_node(Node):
    def __init__(self):
        self.counter=0
        super().__init__("numebr_counter")
        self.create_subscription(Int64,"number",self.timer_call,10)
        self.get_logger().info("subscriber is started")
        
        self.create_timer(1/1,self.timer_call_)
        self.obj_pub=self.create_publisher(Int64,"my_number",10)


        self.create_service(SetBool,"First_server",self.srv_call)
        

    def timer_call(self,msg):
        self.counter+=msg.data
        self.get_logger().info(str(self.counter-5)) 


    def srv_call(self,rq,rsp):
        req_a=rq.data
        if  rq.data ==True:
            self.counter=0
            rsp.success=True
            rsp.message= "Call done"
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
from example_interfaces.srv import AddTwoInts
from example_interfaces.srv import SetBool


class my_server(Node):
    def __init__(self):
        super().__init__("Client_OOP_node")
        self.service_client(True)

    def service_client(self,a):
        client=self.create_client(SetBool,"First_server")
        while client.wait_for_service(0.25)==False:
            self.get_logger().warn("wating for server")

        request=SetBool.Request()
        request.data=a
        futur_obj=client.call_async(request)
        
        


       


def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
