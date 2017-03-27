#!/usr/bin/python

newfile = open("newfile.txt","r")
for line in newfile.readlines():
	print line
newfile.close()
