#!/usr/bin/env python 

import rospy
from std_msgs.msg import Bool

if __name__ == "__main__":
	rospy.init_node("led_pub")
	pub0 = rospy.Publisher("led0", Bool, queue_size=10)
	rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            i = input()
            i = int(i)
           

            if i % 2  == 1:
        	pub0.publish(True)
            else:
                pub0.publish(False)

        rate.sleep()
