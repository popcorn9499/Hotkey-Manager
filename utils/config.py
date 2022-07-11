import os
from utils import fileIO
import sys

def load(name):
    temp = None
    try:
        temp = fileIO.fileLoad(name)
    except FileNotFoundError:
        print("Please copy {0}.sample to {0} and configure!".format(name))
        sys.exit()
    return temp





