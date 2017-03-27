import threading
import time

def myfunction():
	print "Start a thread"
	time.sleep(3)
	print "End a thread"


for i in range(5):
	myfunction()

