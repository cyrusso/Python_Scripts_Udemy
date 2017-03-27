#!/usr/bin/env python
import telnetlib
import time

def open_telnet_conn(ip):
    try:
        username = 'teopy'
        password = 'python'

        cmd_file = raw_input("Enter command fine name and extension: ")


        port = 23

        connection_timeout = 5

        reading_timeout = 5

        connection = telnetlib.Telnet(ip, port, connection_timeout)

        router_output = connection.read_until("Username:", reading_timeout)

        connection.write(username + "\n")

        router_output = connection.read_until("Password", reading_timeout)

        connection.write(password + "\n")
        time.sleep(1)

        connection.write("terminal lenght 0\n")
        time.sleep(1)

        connection.write("\n")
        connection.write("configure terminal\n")
        time.sleep(1)

        selected_cmd_file = open(cmd_file, 'r')

        selected_cmd_file.seek(0)

        for each_line in selected_cmd_file.readlines():
            connection.write(each_line + "\n")
            time.sleep(1)

        selected_cmd_file.close()
        router_output = connection.read_very_eager()
        print router_output

        connection.close()
    except IOError:
        print "Input parameter error"

open_telnet_conn("192.168.2.101")
