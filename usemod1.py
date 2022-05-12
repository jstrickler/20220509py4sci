import sys
# from pkg.pkg import module
# from john/math import geometry.py
from john.math import geometry

a = geometry.circle_area(75)
print("a: {}".format(a))

b = geometry.rectangle_area(18, 6)
print("b: {}".format(b))

# module search sequence
# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin locations (install folder)
for path in sys.path:
    print(path)
