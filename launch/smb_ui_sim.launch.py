from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    rviz_config_path = os.path.join(
        get_package_share_directory('smb_ui'),
        'rviz',
        'smb_sim.rviz'
    )

    # Declare the launch argument
    use_sim_time = LaunchConfiguration('use_sim_time')

    return LaunchDescription([
        # Declare the launch argument
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',  # Changed to true for simulation
            description='Use simulation time'
        ),
        
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path],
            parameters=[{
                'use_sim_time': use_sim_time
            }]
        )
    ]) 