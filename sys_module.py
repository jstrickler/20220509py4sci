import sys
import math
import re

print("sys.argv: {}".format(sys.argv))
print("sys.prefix: {}".format(sys.prefix))
print("sys.executable: {}".format(sys.executable))
print()
print("sys.version: {}".format(sys.version))
print("sys.version_info: {}".format(sys.version_info))
print("sys.version_info.major: {}\n".format(sys.version_info.major))

for path in sys.path:
    print(path)
print()

print("sys.platform: {}\n".format(sys.platform))

print("sys.modules['re']: {}".format(sys.modules['re']))
print("sys.modules['math']: {}\n".format(sys.modules['math']))

print("We are doomed!", file=sys.stderr)

