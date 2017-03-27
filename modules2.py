#!/usr/bin/python3

from tempconv import ftoc
from tempconv import ctof
temp = 212
convTemp = ftoc(temp)
print("The converted temp is " + str(convTemp))
temp = 0
convTemp = ctof(temp)
print("The covertted temp is " + str(convTemp))

