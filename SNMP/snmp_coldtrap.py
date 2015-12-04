from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    sendNotification(SnmpEngine(),
                     CommunityData('debianEdet'),
                     UdpTransportTarget(('192.168.56.4', 162)),
                     ContextData(),
                     'trap',
                     NotificationType(
                         ObjectIdentity('SNMPv2-MIB', 'coldStart')
                     )
    )
)

if errorIndication:
    print(errorIndication)

