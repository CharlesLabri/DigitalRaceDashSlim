import obd

ports = obd.scan_serial()       # return list of valid USB or RF ports
print(ports)                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']