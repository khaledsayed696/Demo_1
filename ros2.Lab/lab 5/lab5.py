
import rclpy 
from rclpy.node import Node
from example_interfaces.msg import String

class my_node(Node):
    def __init__(self):
        self.counter=0
        self.flag=True
        super().__init__("Node_name")

        self.create_timer(1/1 ,self.timer_call)
        self.obj_pub=self.create_publisher(String,"my_topic",10)
        
        self.get_logger().info("Node is started")

    def timer_call(self):
        msg=String()     
        if(self.flag == True):
            msg.data="Hi" 
            self.flag=False
            self.obj_pub.publish(msg)  

        elif(self.flag == False):
            msg.data="Hello" 
            self.flag=True
            self.obj_pub.publish(msg)  
            



def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node )

    rclpy.shutdown()


if __name__=="__main__":
    main()            
    
    
    ............................................................sub......................................................................
    
    import rclpy 
from rclpy.node import Node
from example_interfaces.msg import String

class my_node(Node):
    def __init__(self):
        super().__init__("numebr_counter")
        self.counter=0

        self.create_subscription(String,"my_topic",self.timer_call,10)
        self.get_logger().info("subscriber is started")

    def timer_call(self,msg):
        self.get_logger().info(msg.data)  

   

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node )

    rclpy.shutdown()


if __name__=="__main__":
    main()            
