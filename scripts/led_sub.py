#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

def led0_callback(msg):
    if msg.data:
        with open("/dev/myled0", "w") as f:
                f.write("0\n")

    else:
	with open("/dev/myled0", "w") as f:
		f.write("1\n")


if __name__ == "__main__":
	rospy.init_node("led_pub")
	sub0 = rospy.Subscriber("led0", Bool, led0_callback, queue_size=10)
	rospy.spin()
