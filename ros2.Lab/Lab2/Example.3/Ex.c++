............................................Talker...........................................

#include <chrono>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
using namespace std;


int counter=0;
class Node1 :public rclcpp::Node
{
 public:    
    Node1():Node("string_publisher")
    {
      string_publisher_ = this->create_publisher<std_msgs::msg::String>("str_topic",10);
      timer_ = this->create_wall_timer(std::chrono::microseconds(1000000), 		std::bind(&Node1::timer_cb,this ) );
      
    }
private:
    void timer_cb()
    {
        counter+=1;
      std_msgs::msg::String string_msg = std_msgs::msg::String();
      string_msg.data = "my name is khaled : " + to_string(counter-1) ;  
      string_publisher_->publish(string_msg); 
      

    }
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr string_publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[])
{
    
    rclcpp::init(argc,argv);
    rclcpp::spin(std::make_shared<Node1>());
    rclcpp::shutdown();
    return 0;
}

.............................................Listener....................................
#include <chrono>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class Node2 :public rclcpp::Node
{
 public:    
    Node2():Node("string_subscriber")
    {
      string_subscriber_ = this->create_subscription<std_msgs::msg::String>("str_topic",10, std::bind(&Node2::timer_cb,this,std::placeholders::_1));
      string_publisher_ = this->create_publisher<std_msgs::msg::String>("number_counter",10);
      
      
    }
private:
    void timer_cb(const std_msgs::msg::String::SharedPtr msg)
    {
      RCLCPP_INFO(this->get_logger(),msg->data.c_str());
    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr string_subscriber_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr string_publisher_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc,argv);
    rclcpp::spin(std::make_shared<Node2>());
    rclcpp::shutdown();
    return 0;
}


