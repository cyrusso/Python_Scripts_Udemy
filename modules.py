#!/usr/bin/python3

import tempconv
temp = 212
convTemp = tempconv.ftoc(temp)
print("The converted temp is " + str(convTemp))
temp = 0
convTemp = tempconv.ctof(temp)
print("The covertted temp is " + str(convTemp))

