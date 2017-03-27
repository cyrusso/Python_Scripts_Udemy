#!/usr/bin/pytyon3

import ftplib
import sys

filename = sys.argv[1]
connect = ftplib.FTP("www.ualr.edu")
connect.login("facstaff\mmmcmillan", "meredith26")
file1 = open(filename,"rb")
connect.storbinary("STOR " + filename, file1)
connect.quit()

