import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mhpromit7473/Workspaces/ros2_py_ws/install/my_py_pkg'
