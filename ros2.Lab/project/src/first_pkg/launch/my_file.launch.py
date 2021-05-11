from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ob=LaunchDescription()

    pub_node=Node(
        package="first_pkg",
        executable="node_pub"

    )

    sub_node=Node(
        package="first_pkg",
        executable="node_sub"

    )

    ob.add_action(pub_node)
    ob.add_action(sub_node)

    return ob
