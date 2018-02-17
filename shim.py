import os
import time

# steering_position(4)][brake_position(4)][accelerator_position(4)][gear_position(4)][autonomy_status(1)][ignition_status(1)][kill_status(1)][checksum(4)]\n

# checksum is steering_position + brake_position + accelerator_position + gear_position as uint16_t

# ####################################################################3333

# All constante here in 'arduino' units.

gear_dict = {'P': 123, 'R': 234, 'N': 345, 'D': 456}
full_accel = 3450
full_brake = 450
mid_steering = 1000
rng_steering = 1000

# Time until disbling autonomy irrespective of incoming value, in seconds.

time_till_panic = 1.0

# read text file -- -1.0-1.0 on steering; 0.0-1.0 on accel & brake.

mtime = os.stat('in.txt').st_mtime

with open('in.txt') as fp:
    steering = float(fp.readline())

    accel = float(fp.readline())
    brake = float(fp.readline())

    gear = str.strip(fp.readline())

    autonomy = int(fp.readline())
    ignition = int(fp.readline())
    kill = int(fp.readline())

now = time.time()

if (now - mtime > time_till_panic):
    autonomy = 0

# convert to arduino format

arduino_steering = int((steering * rng_steering) + mid_steering)

arduino_accel = int(accel * full_accel)
arduino_brake = int(brake * full_brake)

arduino_gear = gear_dict[gear]

arduino_autonomy = autonomy
arduino_ignition = ignition
arduino_kill = kill

# convert to digits and calculate checksum

arduino_steering_4 = int(arduino_steering % 10)
arduino_steering_3 = int((arduino_steering % 100 - arduino_steering % 10) / 10)
arduino_steering_2 = int((arduino_steering % 1000 - arduino_steering % 100) / 100)
arduino_steering_1 = int((arduino_steering % 10000 - arduino_steering % 1000) / 1000)

arduino_accel_4 = int(arduino_accel % 10)
arduino_accel_3 = int((arduino_accel % 100 - arduino_accel % 10) / 10)
arduino_accel_2 = int((arduino_accel % 1000 - arduino_accel % 100) / 100)
arduino_accel_1 = int((arduino_accel % 10000 - arduino_accel % 1000) / 1000)

arduino_brake_4 = int(arduino_brake % 10)
arduino_brake_3 = int((arduino_brake % 100 - arduino_brake % 10) / 10)
arduino_brake_2 = int((arduino_brake % 1000 - arduino_brake % 100) / 100)
arduino_brake_1 = int((arduino_brake % 10000 - arduino_brake % 1000) / 1000)

arduino_gear_4 = int(arduino_gear % 10)
arduino_gear_3 = int((arduino_gear % 100 - arduino_gear % 10) / 10)
arduino_gear_2 = int((arduino_gear % 1000 - arduino_gear % 100) / 100)
arduino_gear_1 = int((arduino_gear % 10000 - arduino_gear % 1000) / 1000)

arduino_checksum = (arduino_steering_4 + arduino_steering_3 + arduino_steering_2 + arduino_steering_1 +
                    arduino_accel_4 + arduino_accel_3 + arduino_accel_2 + arduino_accel_1 +
                    arduino_brake_4 + arduino_brake_3 + arduino_brake_2 + arduino_brake_1 +
                    arduino_gear_4 + arduino_gear_3 + arduino_gear_2 + arduino_gear_1)

arduino_checksum_4 = int(arduino_checksum % 10)
arduino_checksum_3 = int((arduino_checksum % 100 - arduino_checksum % 10) / 10)
arduino_checksum_2 = int((arduino_checksum % 1000 - arduino_checksum % 100) / 100)
arduino_checksum_1 = int((arduino_checksum % 10000 - arduino_checksum % 1000) / 1000)

# debug printing

print('Steering')
print(steering)
print(arduino_steering)
print(str(arduino_steering_1) + ' ' + str(arduino_steering_2) + ' ' + str(arduino_steering_3) + ' ' + str(arduino_steering_4))
print('Accel')
print(accel)
print(arduino_accel)
print(str(arduino_accel_1) + ' ' + str(arduino_accel_2) + ' ' + str(arduino_accel_3) + ' ' + str(arduino_accel_4))
print('Brake')
print(brake)
print(arduino_brake)
print(str(arduino_brake_1) + ' ' + str(arduino_brake_2) + ' ' + str(arduino_brake_3) + ' ' + str(arduino_brake_4))
print('Gear')
print(gear)
print(arduino_gear)
print(str(arduino_gear_1) + ' ' + str(arduino_gear_2) + ' ' + str(arduino_gear_3) + ' ' + str(arduino_gear_4))
print('Checksum')
print(arduino_checksum)
print(str(arduino_checksum_1) + ' ' + str(arduino_checksum_2) + ' ' + str(arduino_checksum_3) + ' ' + str(arduino_checksum_4))
print('Autonomy')
print(arduino_autonomy)
print(str(arduino_autonomy))
print('Ignition')
print(arduino_ignition)
print(str(arduino_ignition))
print('Kill')
print(arduino_kill)
print(str(arduino_kill))

# send to arduino

print('Sending to arduino:')
print(str(arduino_steering_1) + str(arduino_steering_2) + str(arduino_steering_3) + str(arduino_steering_4) +
      str(arduino_accel_1) + str(arduino_accel_2) + str(arduino_accel_3) + str(arduino_accel_4) +
      str(arduino_brake_1) + str(arduino_brake_2) + str(arduino_brake_3) + str(arduino_brake_4) +
      str(arduino_gear_1) + str(arduino_gear_2) + str(arduino_gear_3) + str(arduino_gear_4) +
      str(arduino_autonomy) +
      str(arduino_ignition) +
      str(arduino_kill) +
      str(arduino_checksum_1) + str(arduino_checksum_2) + str(arduino_checksum_3) + str(arduino_checksum_4))

# read from arduino

print('Reading from arduino:')
print(str(arduino_steering_1) + str(arduino_steering_2) + str(arduino_steering_3) + str(arduino_steering_4) +
      str(arduino_accel_1) + str(arduino_accel_2) + str(arduino_accel_3) + str(arduino_accel_4) +
      str(arduino_brake_1) + str(arduino_brake_2) + str(arduino_brake_3) + str(arduino_brake_4) +
      str(arduino_gear_1) + str(arduino_gear_2) + str(arduino_gear_3) + str(arduino_gear_4) +
      str(arduino_autonomy) +
      str(arduino_ignition) +
      str(arduino_kill) +
      str(arduino_checksum_1) + str(arduino_checksum_2) + str(arduino_checksum_3) + str(arduino_checksum_4))

# convert to local format.

steering = (arduino_steering - mid_steering) / rng_steering

accel = arduino_accel / full_accel
brake = arduino_brake / full_brake

gear = ''
for key in gear_dict:
    if (arduino_gear == gear_dict[key]):
        gear = key

autonomy = arduino_autonomy
ignition = arduino_ignition
kill = arduino_kill

# write to text file.

with open('out.txt', 'w') as fp:
    fp.write(str(steering) + '\n')

    fp.write(str(accel) + '\n')
    fp.write(str(brake) + '\n')

    fp.write(str(gear) + '\n')

    fp.write(str(autonomy) + '\n')
    fp.write(str(ignition) + '\n')
    fp.write(str(kill) + '\n')
