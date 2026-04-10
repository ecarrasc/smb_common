from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    default_rviz_config = os.path.join(
        get_package_share_directory('smb_common'),
        'rviz',
        'smb_basic.rviz'
    )

    # Declare the launch argument
    use_sim_time = LaunchConfiguration('use_sim_time')
    rviz_config = LaunchConfiguration('rviz_config')

    return LaunchDescription([
        # Declare the launch argument
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',  # Changed to true for simulation
            description='Use simulation time'
        ),

        DeclareLaunchArgument(
            'rviz_config',
            default_value=default_rviz_config,
            description='Path to RViz config file'
        ),
        
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config],
            parameters=[{
                'use_sim_time': use_sim_time
            }]
        )
    ]) 