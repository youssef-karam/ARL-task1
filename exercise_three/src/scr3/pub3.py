#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publisher():
	
	pub	 =rospy.Publisher('raw_data',String,queue_size=10)
	
	rate	 =rospy.Rate(1)
	
	msg_to_publish=String()
	
	while not rospy.is_shutdown():
		name=input("please enter the name:\n")
		age=input("Please enter age:\n")
		height=input("please enter the height:\n")
		string_to_publish="name: %s ,age: %s ,height: %s" % (name,age,height)
		
		msg_to_publish.data = string_to_publish
		pub.publish(msg_to_publish)
		
		rospy.loginfo(string_to_publish)
		
		rate.sleep()
		
		
if __name__ == "__main__":
	rospy.init_node('user_info_driver')
	publisher()
