#!/usr/bin/env python
import os

os.system("hostname")  # <1>

hostname = os.popen("hostname").read()
print("hostname: {}".format(hostname))


with os.popen('netstat -an') as netstat_in:  # <2>
    for entry in netstat_in:  # <3>
        if 'ESTAB' in entry:  # <4>
            print(entry, end='')
print()

