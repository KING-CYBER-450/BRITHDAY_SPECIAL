import os, sys

try:

    __import__("gift").ck()

except Exception as e:

    exit(str(e))
