#!/usr/bin/env python

with open("../DATA/tyger.txt", "r") as tyger_in:  # <1>
    for line in tyger_in:  # <2>
        line = line.rstrip()
        print(line)  # <3>

