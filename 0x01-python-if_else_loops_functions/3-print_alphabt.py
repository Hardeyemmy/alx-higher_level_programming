#!/usr/bin/python3
for v in range(ord('a'), ord('z') + 1):
    if v != ord('e') and v != ord('q'):
        print("{:c}".format(v), end="")
