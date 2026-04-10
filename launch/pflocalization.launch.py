from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    pkg_share = get_package_share_directory('smb_common')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_share, 'launch', 'gazebo.launch.py')
        )
    )

    sim_se = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_share, 'launch', 'smb_sim_se.launch.py')
        ),
        launch_arguments={
            'rviz_config': os.path.join(pkg_share, 'rviz', 'smb_localization.rviz')
        }.items()
    )

    map_file_path = os.path.join(
        pkg_share,
        'data',
        'map_room_01.yaml'
    )

    # Define the map_server lifecycle node
    map_server_cmd = Node(
        package='nav2_map_server',
        executable='map_server',
        output='screen',
        parameters=[{'yaml_filename': map_file_path}]
    )

    amcl_cmd = Node(
        package='nav2_amcl',
        executable='amcl',
        output='screen'
    )

    # Define the lifecycle manager to handle activation
    # It manages the 'map_server' node and sets autostart to True
    lifecycle_manager_cmd = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager',
        output='screen',
        parameters=[
            {'use_sim_time': True},
            {'autostart': True},
            {'node_names': ['map_server', 'amcl']}
        ]
    )

    return LaunchDescription([
        gazebo,
        sim_se,
        map_server_cmd,
        amcl_cmd,
        lifecycle_manager_cmd
    ])