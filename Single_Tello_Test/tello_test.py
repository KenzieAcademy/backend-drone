#!/usr/bin/env python
"""
Executes a series of Tello commands from a flight script
"""

from tello import Tello
import sys
from datetime import datetime
import time

start_time = str(datetime.now())

file_name = sys.argv[1]

with open(file_name, "r") as f:
    commands = f.readlines()

with Tello() as tello:
    for command in commands:
        command = command.strip()
        if command.startswith('#'):
            continue
        if command:
            if command.find('delay') != -1:
                sec = float(command.partition('delay')[2])
                print 'delay %s ...' % sec
                time.sleep(sec)
            else:
                tello.send_command(command)

print("Completed.")
# log = tello.get_log()

# with open('log/' + start_time + '.txt', 'w') as out:
#     for stat in log:
#         stat.print_stats()
#         str = stat.return_stats()
#         out.write(str)
