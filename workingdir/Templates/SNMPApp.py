#!/usr/bin/env python

from pysnmp.entity.rfc3413.oneliner import cmdgen

def snmp_get(ip):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBindNbrTable = cmdGen.nextCmd(cmdgen.CommunityData(comm), cmdgen.UpTransportTarget((ip, 161)), \
                                                                                                                    '1.3.6.1.2.1.14.10.1.3')
    errorIndication, errorStatus, errorIndex, varBindNbrTable = cmdGen.nextCmd(cmdgen.CommunityData(comm), cmdgen.UpTransportTarget((ip, 161)), \
                                                                                                                    '1.3.6.1.4.1.9.2.1.3')
    errorIndication, errorStatus, errorIndex, varBindNbrTable = cmdGen.nextCmd(cmdgen.CommunityData(comm), cmdgen.UpTransportTarget((ip, 161)), \
                                                                                                                    '1.3.6.1.2.1.14.1.1')
