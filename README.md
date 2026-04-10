# smb_common

## Useful command for launching telop keyboard

ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args \
  -r /cmd_vel:=/key_vel \
  -p stamped:=true \
  -p frame_id:=base_link