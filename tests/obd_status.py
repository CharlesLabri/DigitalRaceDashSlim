from obd import OBDStatus

# no connection is made
print(OBDStatus.NOT_CONNECTED) # "Not Connected"

# successful communication with the ELM327 adapter
print(OBDStatus.ELM_CONNECTED) # "ELM Connected"

# successful communication with the ELM327 adapter,
# OBD port connected to the car, ignition off
# (not available with argument "check_voltage=False")
print(OBDStatus.OBD_CONNECTED) # "OBD Connected"

# successful communication with the ELM327 and the
# vehicle; ignition on
print(OBDStatus.CAR_CONNECTED) # "Car Connected"